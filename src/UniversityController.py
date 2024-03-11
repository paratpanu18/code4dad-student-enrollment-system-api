from fastapi import APIRouter, HTTPException, Depends

from Student import Student
from Teacher import Teacher
from Admin import Admin
from Course import Course
from Section import Section
from Faculty import Faculty
from Major import Major
from Grade import Grade
from Transcript import Transcript
from Util import get_current_semester, get_current_academic_year, time_is_intersect
import Schema

university_router = APIRouter(tags=["university"])
authenticator_router = APIRouter(tags=["authenticator"])
student_router = APIRouter(tags=["student"])
teacher_router = APIRouter(tags=["teacher"])
admin_router = APIRouter(tags=["admin"])
course_router = APIRouter(tags=["course and section"])

class University():
    def __init__(self, name):
        self.__name = name
        self.__user_list = []
        self.__faculty_list = []
        self.__course_list = []
        self.__max_credit = 27

    def get_student_by_student_id(self, student_id):
        for user in self.__user_list:
            if isinstance(user, Student) and user.student_id == student_id:
                return user
        return None
    
    def get_student_data_by_student_id(self, student_id):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student.to_dict()

    def login(self, username, password):
        for user in self.__user_list:
            if user.username == username and user.password_is_correct(password):
                return user.create_token()
        raise HTTPException(status_code=404, detail="Login credentials are incorrect")

    def add_student(self, student_id, password, email, name, citizen_id, major, faculty):
        if self.get_student_by_student_id(student_id) is not None:
            raise HTTPException(status_code=400, detail="Student ID already exists")

        new_student = Student(student_id, password, email, name, citizen_id, major, faculty)
        self.__user_list.append(new_student)
        return new_student.to_dict()
    
    def enroll_student_to_section(self, student_id, course_id, section_number, semester = get_current_semester(), year = get_current_academic_year()):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        # Check if student is already enrolled in the course
        for section in course.section_list:
            if student in section.student_list:
                raise HTTPException(status_code=400, detail="Student already enrolled in course")

        section = course.get_section_by_section_number_semester_year(section_number, semester, year)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        # Check if student passed the pre-requisite courses
        for pre_requisite_course in course.pre_requisite_course_list:
            if student.is_passed_course(pre_requisite_course) is False:
                raise HTTPException(status_code=400, detail=f'Student has not passed the pre-requisite course: ({pre_requisite_course.course_id}) {pre_requisite_course.course_name}')
            
        student_transcript = student.get_transcript_by_semester_and_year(section.semester, section.year)
        if student_transcript is not None and \
           student_transcript.current_credit + section.course.credit > self.__max_credit:
            raise HTTPException(status_code=400, detail="Cannot enroll to the section. The student has reached the maximum credit")

        # Check if time schedule is overlapped
        if student_transcript:
            new_section_schedule = section.schedule
            for enrollment in student_transcript.enrollment_list:
                existing_section_schedule = enrollment.section.schedule
                if time_is_intersect(new_section_schedule, existing_section_schedule):
                    raise HTTPException(status_code=400, detail=f'Cannot enroll to the section. Time schedule is overlapped with the existing section ({enrollment.section.course.course_id}) {enrollment.section.course.course_name}')

        # Enroll student to the section and add the enrollment to the student's transcript and do again for co-requisite courses
        if section.add_student_to_section(student):
            student.enroll_to_section(section)
        else:
            return {"message": "Student is added to the wait list. Current number of students in the wait list: " + str(len(section.wait_list))}

        if course.co_requisite_course is not None:
            co_requisite_course_section = course.co_requisite_course.get_section_by_section_number_semester_year(section.co_requisite_section.section_number, semester, year)
            if co_requisite_course_section is not None:
                co_requisite_course_section.add_student_to_section(student)
                student.enroll_to_section(co_requisite_course_section)
                return student_transcript.to_dict()
            
        if len(section.student_list) > section.max_student:
            return {"message": "Student is added to the wait list. Current number of students in the wait list: " + str(len(section.wait_list))}

        return student.get_transcript_by_semester_and_year(section.semester, section.year).to_dict()
    
    def drop_student_from_section(self, student_id, course_id, section_number, semester = get_current_semester(), year = get_current_academic_year()):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        section = course.get_section_by_section_number_semester_year(section_number, semester, year)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        if student not in section.student_list:
            raise HTTPException(status_code=400, detail="Student is not enrolled in section")
        
        student_transcript = student.get_transcript_by_semester_and_year(semester, year)
        
        section.drop_student_from_section(student)
        student_transcript.drop_enrollment_from_transcript(section)
        
        if course.co_requisite_course is not None:
            co_requisite_course_section = course.co_requisite_course.get_section_by_section_number_semester_year(section.co_requisite_section.section_number, semester, year)
            if co_requisite_course_section is not None:
                co_requisite_course_section.drop_student_from_section(student)
                student_transcript.drop_enrollment_from_transcript(co_requisite_course_section)

        next_student_in_wait_list = section.get_next_student_in_wait_list()

        if next_student_in_wait_list:
            self.enroll_student_to_section(next_student_in_wait_list.student_id, course.course_id, section.section_number)
        
        return student_transcript.to_dict()

    def change_student_section(self, student_id, course_id, old_section_number, new_section_number):
        self.drop_student_from_section(student_id, course_id, old_section_number)
        return self.enroll_student_to_section(student_id, course_id, new_section_number)

    def get_student_transcript_by_semester_and_year(self, student_id, semester, year):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        transcript = student.get_transcript_by_semester_and_year(semester, year)

        if transcript is not None:
            return transcript.to_dict()
        
        raise HTTPException(status_code=404, detail="Transcript not found")
    
    def get_all_student_transcript_by_student_id(self, student_id):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        return student.get_all_transcripts()

    def get_teacher_by_teacher_id(self, teacher_id):
        for user in self.__user_list:
            if isinstance(user, Teacher) and user.teacher_id == teacher_id:
                return user
        return None
    
    def get_teacher_data_by_teacher_id(self, teacher_id):
        teacher = self.get_teacher_by_teacher_id(teacher_id)
        if teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return teacher.to_dict()

    def add_teacher(self, teacher_id, password, email, name, citizen_id):
        if self.get_teacher_by_teacher_id(teacher_id) is not None:
            raise HTTPException(status_code=400, detail="Teacher ID already exists")
        
        new_teacher = Teacher(teacher_id, password, email, name, citizen_id)
        self.__user_list.append(new_teacher)
        return new_teacher.to_dict()

    def assign_grade_to_student(self, student_id, course_id, section_number, grade, semester = get_current_semester(), year = get_current_academic_year()):
        student = self.get_student_by_student_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        section = course.get_section_by_section_number_semester_year(section_number, semester, year)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        if student not in section.student_list:
            raise HTTPException(status_code=400, detail="Student is not enrolled in section")
        
        student_transcript = student.get_transcript_by_semester_and_year(section.semester, section.year)

        return student_transcript.assign_grade_to_enrollment(section, grade)
    
    def assign_grade_and_score_to_multiple_student(self, grade_and_score: Schema.GradeAndScoreAssignment):
        course = self.get_course_by_course_id(grade_and_score.course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        section = course.get_section_by_section_number_semester_year(grade_and_score.section_number, grade_and_score.semester, grade_and_score.year)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        grade_and_score_dict = grade_and_score.grade_and_score_dict
        
        for student_id, score_data in grade_and_score_dict.items():
            student = self.get_student_by_student_id(student_id)
            if student is None:
                raise HTTPException(status_code=404, detail="Student not found")
            
            if student not in section.student_list:
                raise HTTPException(status_code=400, detail="Student is not enrolled in section")
            
            student_transcript = student.get_transcript_by_semester_and_year(section.semester, section.year)
            student_transcript.assign_grade_to_enrollment(section, score_data["grade"])

            for score_name, score in score_data["score"].items():
                student_transcript.assign_score_to_enrollment(section, score_name, score)

        return section.get_grade_and_score_student()
    
    def add_course(self, course_name, course_id, credit, course_type, grading_type):
        if self.get_course_by_course_id(course_id) is not None:
            raise HTTPException(status_code=400, detail="Course ID already exists")

        new_course = Course(course_id, course_name, credit, course_type, grading_type)
        self.__course_list.append(new_course)
        return new_course.to_dict()
    
    def add_section(self, course_id, section_number, teacher_id, max_student, location, schedule, semester, year):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        teacher = self.get_teacher_by_teacher_id(teacher_id)
        if teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        new_section = Section(course, section_number, teacher, max_student, location, schedule, semester, year)
        course.add_section(new_section)

        teacher.add_taught_section(new_section)

        return new_section.to_dict()
    
    def get_course_by_course_id(self, course_id):
        for course in self.__course_list:
            if course.course_id == course_id:
                return course
        return None
    
    def get_course_data_by_course_id(self, course_id):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        return course.to_dict()
    
    def get_all_sections_data_by_course_id(self, course_id):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        return [section.to_dict() for section in course]
    
    def get_all_faculties(self):
        return [faculty.to_dict() for faculty in self.__faculty_list]
    
    def get_faculty_by_faculty_name(self, faculty_name):
        for faculty in self.__faculty_list:
            if faculty.faculty_name == faculty_name:
                return faculty
        return None
    
    def get_faculty_data_by_faculty_name(self, faculty_name):
        faculty = self.get_faculty_by_faculty_name(faculty_name)
        if faculty is None:
            raise HTTPException(status_code=404, detail="Faculty not found")
        return faculty.to_dict()
    
    def add_faculty(self, faculty_name):
        if self.get_faculty_by_faculty_name(faculty_name) is not None:
            raise HTTPException(status_code=400, detail="Faculty already exists")
        
        new_faculty = Faculty(faculty_name)
        self.__faculty_list.append(new_faculty)
        return new_faculty.to_dict()
    
    def get_major_by_major_name(self, major_name):
        for faculty in self.__faculty_list:
            major = faculty.get_major_by_major_name(major_name)
            if major is not None:
                return major
        return None
    
    def get_major_in_faculty(self, faculty_name, major_name):
        faculty = self.get_faculty_by_faculty_name(faculty_name)
        if faculty is None:
            raise HTTPException(status_code=404, detail="Faculty not found")
        
        major = faculty.get_major_by_major_name(major_name)
        if major is None:
            raise HTTPException(status_code=404, detail="Major not found")
        
        return major.to_dict()
    
    def add_major(self, major_name, academic_fees, faculty_name):
        faculty = self.get_faculty_by_faculty_name(faculty_name)
        if faculty is None:
            raise HTTPException(status_code=404, detail="Faculty not found")
        
        major = self.get_major_by_major_name(major_name)
        if major is not None:
            raise HTTPException(status_code=400, detail="Major already exists")
        
        new_major = Major(major_name, academic_fees)
        faculty.add_major(new_major)
        return new_major.to_dict()
    
    def add_course_to_major(self, faculty_name, major_name, course_id, course_group):
        faculty = self.get_faculty_by_faculty_name(faculty_name)
        if faculty is None:
            raise HTTPException(status_code=404, detail="Faculty not found")
        
        major = faculty.get_major_by_major_name(major_name)
        if major is None:
            raise HTTPException(status_code=404, detail="Major not found")
        
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        if course_group == "Core Course":
            major.add_core_course(course)
        elif course_group == "Elective Course":
            major.add_elective_course(course)
        else:
            raise HTTPException(status_code=400, detail="Invalid course type. Course type must be one of the following: Core, Elective")
        
        return major.to_dict()
    
    def get_course_by_course_type(self, faculty_name, major_name, course_type, semester = get_current_semester(), year = get_current_academic_year()):
        faculty = self.get_faculty_by_faculty_name(faculty_name)
        if faculty is None:
            raise HTTPException(status_code=404, detail="Faculty not found")
        
        major = faculty.get_major_by_major_name(major_name)
        if major is None:
            raise HTTPException(status_code=404, detail="Major not found")
        
        course_list = []
        for course in self.__course_list:
            if course.get_section_by_semester_year(semester, year) and course.course_type == course_type:
                course_list.append(course.to_dict())
        
        return course_list
    
    def get_all_course_in_major(self, faculty_name, major_name):
        faculty = self.get_faculty_by_faculty_name(faculty_name)
        if faculty is None:
            raise HTTPException(status_code=404, detail="Faculty not found")
        
        major = faculty.get_major_by_major_name(major_name)
        if major is None:
            raise HTTPException(status_code=404, detail="Major not found")
        
        course_list = []
        for course in self.__course_list:
            if course in major.core_course_list or course in major.elective_course_list:
                course_list.append(course.to_dict())
        
        return course_list

    
    def get_all_sections_taught_by_teacher_id(self, teacher_id, semester, year):
        teacher = self.get_teacher_by_teacher_id(teacher_id)
        if teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        return teacher.get_all_sections_taught_by_semester_and_year(semester, year)
                
    def get_all_section_by_semester_and_year(self, semester, year):
        result = []
        for course in self.__course_list:
            for section in course.section_list:
                if section.semester == semester and section.year == year:
                    result.append(section.to_dict())
        return result
    
    def add_pre_requisite_to_course(self, course_id, pre_requisite_course_id):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        pre_requisite_course = self.get_course_by_course_id(pre_requisite_course_id)
        if pre_requisite_course is None:
            raise HTTPException(status_code=404, detail="Pre-requisite course not found")
        
        return course.add_pre_requisite_course(pre_requisite_course)
    
    def add_co_requisite_to_course_section(self, course_id, section_number, co_requisite_course_id, co_requisite_section_number, semester = get_current_semester(), year = get_current_academic_year()):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        section = course.get_section_by_section_number_semester_year(section_number, semester, year)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        co_requisite_course = self.get_course_by_course_id(co_requisite_course_id)
        if co_requisite_course is None:
            raise HTTPException(status_code=404, detail="Co-requisite course not found")
        
        co_requisite_section = co_requisite_course.get_section_by_section_number_semester_year(co_requisite_section_number, semester, year)
        if co_requisite_section is None:
            raise HTTPException(status_code=404, detail="Co-requisite section not found")
        
        section.add_co_requisite_section(co_requisite_section)
        course.add_co_requisite_course(co_requisite_course)

        return {"message": "Co-requisite is added"}
    
    def get_co_requisite_to_course_section(self, course_id, section_number, semester, year):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        section = course.get_section_by_section_number_semester_year(section_number, semester, year)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        return section.get_co_requisite_section()
    
    def get_detail_student_in_section(self, course_id, section_number, semester = get_current_semester(), year = get_current_academic_year()):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        section = course.get_section_by_section_number_semester_year(section_number, semester, year)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        return section.get_grade_and_score_student()
    
    def get_all_student_in_major(self, faculty_name, major_name):
        faculty = self.get_faculty_by_faculty_name(faculty_name)
        if faculty is None:
            raise HTTPException(status_code=404, detail="Faculty not found")
        
        major = faculty.get_major_by_major_name(major_name)
        if major is None:
            raise HTTPException(status_code=404, detail="Major not found")
        
        student_in_major_list = []
        for student in self.__user_list:
            if isinstance(student, Student) and student.major == major_name and student.faculty == faculty_name:
                student_in_major_list.append(student.to_dict())
        
        return student_in_major_list
    
    def get_admin_by_admin_id(self, admin_id):
        for user in self.__user_list:
            if isinstance(user, Admin) and user.admin_id == admin_id:
                return user
        return None
    
    def get_data_admin_by_admin_id(self, admin_id):
        admin = self.get_admin_by_admin_id(admin_id)
        if admin is None:
            raise HTTPException(status_code=404, detail="Admin not found")
        return admin.to_dict()
       
    def add_admin(self, admin_id, password, email, name, citizen_id):
        if self.get_admin_by_admin_id(admin_id) is not None:
            raise HTTPException(status_code=400, detail="Admin ID already exists")
        
        new_admin = Admin(admin_id, password, email, name, citizen_id)
        self.__user_list.append(new_admin)
        return new_admin.to_dict()
    
    def delete_user_by_username(self, username):
        for user in self.__user_list:
            if user.username == username:
                self.__user_list.remove(user)
                return {"message": "User is deleted"}
        raise HTTPException(status_code=404, detail="User not found")
    
    def delete_course_by_course_id(self, course_id):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        self.__course_list.remove(course)
        return {"message": "Course is deleted"}
    
    def delete_section_from_course(self, course_id, section_number, semester, year):
        course = self.get_course_by_course_id(course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        section = course.get_section_by_section_number_semester_year(section_number, semester, year)
        if section is None:
            raise HTTPException(status_code=404, detail="Section not found")
        
        if course.remove_section(section):
            return {"message": "Section is deleted"}
        else:
            raise HTTPException(status_code=400, detail="Something went wrong")

    def change_password(self, username, old_password, new_password):
        user = self.get_user_by_username(username)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        if not user.password_is_correct(old_password):
            raise HTTPException(status_code=400, detail="Old password is incorrect")
        
        user.change_password(new_password)
        return {"message": "Password is changed"}

kmitl = University(name="KMITL")


# Student
@student_router.post("/add_student")
async def add_student(student: Schema.InsertStudent):
    return kmitl.add_student(student.student_id, 
                             student.password, 
                             student.email, 
                             student.name, 
                             student.citizen_id, 
                             student.major, 
                             student.faculty)

@student_router.get("/get_student_by_student_id/{student_id}")
async def get_student_by_student_id(student_id: str):
    return kmitl.get_student_data_by_student_id(student_id)

@student_router.post("/enroll")
async def enroll(enroll: Schema.Enroll):
    return kmitl.enroll_student_to_section(enroll.student_id, enroll.course_id, enroll.section_number)

@student_router.post("/drop")
async def drop(drop: Schema.Enroll):
    return kmitl.drop_student_from_section(drop.student_id, drop.course_id, drop.section_number)

@student_router.post("/change_section")
async def change_section(change: Schema.ChangeSection):
    return kmitl.change_student_section(change.student_id, change.course_id, change.old_section_number, change.new_section_number)

@student_router.get("/get_student_transcript_by_semester_and_year/{student_id}/{semester}/{year}")
async def get_student_transcript_by_semester_and_year(student_id: str, semester: int, year: int):
    return kmitl.get_student_transcript_by_semester_and_year(student_id, semester, year)

@student_router.get("/get_all_student_transcripts/{student_id}")
def get_all_student_transcript(student_id: str):
    return kmitl.get_all_student_transcript_by_student_id(student_id)

# Teacher
@teacher_router.post("/add_teacher")
async def add_teacher(teacher: Schema.InsertTeacher):
    return kmitl.add_teacher(teacher_id=teacher.teacher_id,
                            password=teacher.password,
                            email=teacher.email,
                            name=teacher.name,
                            citizen_id=teacher.citizen_id)

@teacher_router.get("/get_teacher_by_teacher_id/{teacher_id}")
async def get_teacher_by_teacher_id(teacher_id: str):
    return kmitl.get_teacher_data_by_teacher_id(teacher_id)

@teacher_router.post("/assign_grade_to_student")
def assign_grade_to_student(grade: Schema.GradeAssignment):
    return kmitl.assign_grade_to_student(grade.student_id, grade.course_id, grade.section_number, grade.grade)\

@teacher_router.post("/assign_grade_and_score_to_multiple_student")
async def assign_grade_and_score_to_multiple_student(grade: Schema.GradeAndScoreAssignment):
    return kmitl.assign_grade_and_score_to_multiple_student(grade)


@teacher_router.get("/get_all_sections_taught_by_teacher_id/{teacher_id}/{semester}/{year}")
def get_all_sections_taught_by_teacher_id(teacher_id: str, semester: int, year: int):
    return kmitl.get_all_sections_taught_by_teacher_id(teacher_id, semester, year)

# Course
@course_router.get("/get_course_by_course_id/{course_id}")
async def get_course_by_course_id(course_id: str):
    return kmitl.get_course_data_by_course_id(course_id)

@course_router.get("/get_course_by_course_type/{faculty_name}/{major_name}/{course_type}")
async def get_course_by_course_type(faculty_name: str, major_name: str, course_type: str):
    return kmitl.get_course_by_course_type(faculty_name, major_name, course_type)

@course_router.post("/add_course")
async def add_course(course: Schema.InsertCourse):
    return kmitl.add_course(course.course_name, 
                            course.course_id, 
                            course.credit, 
                            course.course_type, 
                            course.grading_type)

@course_router.post("/add_section")
async def add_section(section: Schema.InsertSection):
    return kmitl.add_section(section.course_id, 
                            section.section_number, 
                            section.teacher_id, 
                            section.max_student,
                            section.location, 
                            section.schedule, 
                            section.semester, 
                            section.year)

@course_router.get("/get_all_sections_by_course_id/{course_id}")
async def get_all_sections_by_course_id(course_id: str):
    return kmitl.get_all_sections_data_by_course_id(course_id)

@course_router.get("/get_all_section_by_semester_and_year/{semester}/{year}")
async def get_all_section_by_semester_and_year(semester: int, year: int):
    return kmitl.get_all_section_by_semester_and_year(semester, year)

@course_router.post("/add_pre_requisite_to_course")
async def add_pre_requisite_to_course(pre_requisite: Schema.InsertPreRequisite):
    return kmitl.add_pre_requisite_to_course(pre_requisite.course_id, pre_requisite.pre_requisite_course_id)

@course_router.get("/get_detail_student_in_section/{course_id}/{section_number}/{semester}/{year}")
async def get_detail_student_in_section(course_id: str, section_number: int, semester: int, year: int):
    return kmitl.get_detail_student_in_section(course_id, section_number, semester, year)

@course_router.post("/add_co_requisite_to_course_section")
async def add_co_requisite_to_course_section(co_requisite: Schema.InsertCoRequisite):
    return kmitl.add_co_requisite_to_course_section(co_requisite.course_id, co_requisite.section_number, co_requisite.co_requisite_course_id, co_requisite.co_requisite_section_number)

@course_router.get("/get_co_requisite_to_course_section/{course_id}/{section_number}")
async def get_co_requisite_to_course_section(course_id: str, section_number: int):
    return kmitl.get_co_requisite_to_course_section(course_id, section_number)

# Authenticator
@authenticator_router.post("/login")
async def login(credentials: Schema.LoginCredentials):
    return kmitl.login(credentials.username, credentials.password)

@authenticator_router.put("/change_password")
async def change_password(credentials: Schema.ChangePasswordRequest):
    return kmitl.change_password(credentials.username, credentials.old_password, credentials.new_password)

# University
@university_router.get("/get_all_course_in_major/{faculty_name}/{major_name}")
async def get_all_course_in_major(faculty_name: str, major_name: str):
    return kmitl.get_all_course_in_major(faculty_name, major_name)

@university_router.get("/get_all_faculties")
async def get_all_faculties():
    return kmitl.get_all_faculties()

@university_router.get("/get_faculty_by_faculty_name/{faculty_name}")
async def get_faculty_by_faculty_name(faculty_name: str):
    return kmitl.get_faculty_data_by_faculty_name(faculty_name)

@university_router.get("/get_major_in_faculty/{faculty_name}/{major_name}")
async def get_major_in_faculty(faculty_name: str, major_name: str):
    return kmitl.get_major_in_faculty(faculty_name, major_name)

@university_router.post("/add_faculty")
async def add_faculty(faculty: Schema.InsertFaculty):
    return kmitl.add_faculty(faculty.faculty_name)

@university_router.post("/add_major")
async def add_major(major: Schema.InsertMajor):
    return kmitl.add_major(major.major_name, 
                          major.academic_fees,  
                          major.faculty_name)

@university_router.post("/add_course_to_major")
async def add_course_to_major(course: Schema.InsertCourseToMajor):
    return kmitl.add_course_to_major(course.faculty_name, 
                                    course.major_name, 
                                    course.course_id, 
                                    course.course_group)

@university_router.get("/get_all_student_in_major/{faculty_name}/{major_name}")
async def get_all_student_in_major(faculty_name: str, major_name: str):
    return kmitl.get_all_student_in_major(faculty_name, major_name)

@university_router.get("/get_current_semester_and_year")
async def get_current_semester_and_year():
    return {"semester": get_current_semester(), "year": get_current_academic_year()}

# Admin
@admin_router.post("/add_admin")
async def add_admin(admin: Schema.InsertAdmin):
    return kmitl.add_admin(admin.teacher_id, 
                          admin.password, 
                          admin.email, 
                          admin.name, 
                          admin.citizen_id)

@admin_router.get("/get_admin_by_admin_id/{admin_id}")
async def get_admin_by_admin_id(admin_id: str):
    return kmitl.get_data_admin_by_admin_id(admin_id)

@admin_router.delete("/delete_user_by_username/{username}")
async def delete_user_by_username(username: str):
    return kmitl.delete_user_by_username(username)

@admin_router.delete("/delete_course_by_course_id/{course_id}")
async def delete_course_by_course_id(course_id: str):
    return kmitl.delete_course_by_course_id(course_id)

@admin_router.delete("/delete_section_from_course/{course_id}/{section_number}/{semester}/{year}")
async def delete_section_from_course(course_id: str, section_number: int, semester: int, year: int):
    return kmitl.delete_section_from_course(course_id, section_number, semester, year)
