from Student import Student
from Teacher import Teacher


from UniversityController import kmitl

def init_student():
    kmitl.add_student(student_id = "66010542", 
                      password = "12345", 
                      email = "66010542@kmitl.ac.th", 
                      name = "Paratpanu Pechsaman", 
                      citizen_id = "1033825486492", 
                      major = "Computer Engineering", 
                      faculty = "Engineering")
    
    kmitl.add_student(student_id = "66010533", 
                      password = "12345", 
                      email = "66010533@kmitl.ac.th", 
                      name = "Prompipat Thongtub", 
                      citizen_id = "1126286680095", 
                      major = "Computer Engineering", 
                      faculty = "Engineering")
    

    kmitl.add_student(student_id = "66010572", 
                      password = "12345", 
                      email = "66010572@kmitl.ac.th", 
                      name = "Pipatpong Panpreuak", 
                      citizen_id = "1548329362896", 
                      major = "Computer Engineering", 
                      faculty = "Engineering")
    
    kmitl.add_student(student_id = "66010587", 
                      password = "12345", 
                      email = "66010587@kmitl.ac.th", 
                      name = "Pearaphat Kumsing", 
                      citizen_id = "5132523735261", 
                      major = "Computer Engineering", 
                      faculty = "Engineering")

def init_teacher():
    kmitl.add_teacher(teacher_id = "teacher1",
                        password = "12345",
                        email = "teacher1@kmitl.ac.th",
                        name = "Teacher 1",
                        citizen_id = "1234567890123")
    
    kmitl.add_teacher(teacher_id = "teacher2",
                        password = "12345",
                        email = "teacher2@kmitl.ac.th",
                        name = "Teacher 2",
                        citizen_id = "1234567890124")

def init_course():

    GRADE = 0
    SATISFACTORY = 1

    GENED = 0
    FACULTY = 1
    CURRICULUM = 2

    kmitl.add_course(course_name = "Calculus 1", 
                     course_id = "01076140", 
                     credit = 3, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    
    kmitl.add_course(course_name = "Introduction to Computer Engineering", 
                     course_id = "01076001", 
                     credit = 3, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    
    kmitl.add_course(course_name = "Digital Intelligence Quotient",  
                     course_id = "90641001", 
                     credit = 3, 
                     course_type = GENED, 
                     grading_type = SATISFACTORY)
    
    kmitl.add_course(course_name = "Programming Fundamental",
                     course_id = "01076002", 
                     credit = 2, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    
    kmitl.add_course(course_name = "Programming Project",
                     course_id = "01076003", 
                     credit = 1, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    
    kmitl.add_course(course_name = "Pre-Activity Engineering",
                     course_id = "01076004", 
                     credit = 1, 
                     course_type = FACULTY, 
                     grading_type = GRADE)
    
    kmitl.add_course(course_name = "Charm School",
                     course_id = "01076005", 
                     credit = 2, 
                     course_type = FACULTY, 
                     grading_type = SATISFACTORY)
    
    kmitl.add_course(course_name = "Fundation English1",
                     course_id = "90641002", 
                     credit = 3, 
                     course_type = GENED, 
                     grading_type = SATISFACTORY)
    
    kmitl.add_course(course_name = "Fundation English2",
                        course_id = "90641003", 
                        credit = 3, 
                        course_type = GENED, 
                        grading_type = SATISFACTORY)

def init_section():
    # Calculus 1 - Section 16
    kmitl.add_section(course_id = "01076140",
                        section_number = 16,
                        teacher_id = "teacher1",
                        max_student = 50,
                        location = "ECC-811",
                        schedule = "Mon 10:00-12:00",
                        semester = 1,
                        year = 2024)

    # Calculus 1 - Section 17
    kmitl.add_section(course_id = "01076140",
                        section_number = 17,
                        teacher_id = "teacher2",
                        max_student = 50,
                        location = "ECC-811",
                        schedule = "Mon 10:00-12:00",
                        semester = 1,
                        year = 2024)

    # Introduction to Computer Engineering - Section 16
    kmitl.add_section(course_id = "01076001",
                        section_number = 16,
                        teacher_id = "teacher1",
                        max_student = 50,
                        location = "ECC-811",
                        schedule = "Mon 10:00-12:00",
                        semester = 1,
                        year = 2024)
    
    # Introduction to Computer Engineering - Section 17
    kmitl.add_section(course_id = "01076001",
                        section_number = 17,
                        teacher_id = "teacher2",
                        max_student = 50,
                        location = "ECC-811",
                        schedule = "Mon 10:00-12:00",
                        semester = 1,
                        year = 2024)

def init_enrollment():
    kmitl.enroll_student_to_section(student_id = "66010542",
                                    course_id = "01076140",
                                    section_number = 16)
    
    kmitl.enroll_student_to_section(student_id = "66010533",
                                    course_id = "01076140",
                                    section_number = 16)
    
def init_faculty():
    kmitl.add_faculty(faculty_name = "Engineering")
    kmitl.add_faculty(faculty_name = "Architecture")
    kmitl.add_faculty(faculty_name = "Science")
    kmitl.add_faculty(faculty_name = "Industrial Education")
    kmitl.add_faculty(faculty_name = "Information Technology")
    kmitl.add_faculty(faculty_name = "Agro-Industry")
    kmitl.add_faculty(faculty_name = "Management Science")

def init_major():
    kmitl.add_major(major_name = "Computer Engineering", academic_fees= 25000, faculty_name = "Engineering")
    kmitl.add_major(major_name = "Civil Engineering", academic_fees= 25000, faculty_name = "Engineering")
    kmitl.add_major(major_name = "Architecture", academic_fees= 25000, faculty_name = "Architecture")
    kmitl.add_major(major_name = "Physics", academic_fees= 25000, faculty_name = "Science")
    kmitl.add_major(major_name = "Chemistry", academic_fees= 25000, faculty_name = "Science")
    kmitl.add_major(major_name = "Biology", academic_fees= 25000, faculty_name = "Science")
    kmitl.add_major(major_name = "Industrial Education", academic_fees= 25000, faculty_name = "Industrial Education")
    kmitl.add_major(major_name = "Information Technology", academic_fees= 25000, faculty_name = "Information Technology")
    kmitl.add_major(major_name = "Agro-Industry", academic_fees= 25000, faculty_name = "Agro-Industry")
    kmitl.add_major(major_name = "Management Science", academic_fees= 25000, faculty_name = "Management Science")

def init_add_course_to_major():
    kmitl.add_course_to_major(faculty_name = "Engineering", major_name = "Computer Engineering", course_id = "01076140", course_group = "Core")
    kmitl.add_course_to_major(faculty_name = "Engineering", major_name = "Computer Engineering", course_id = "01076001", course_group = "Core")
    kmitl.add_course_to_major(faculty_name = "Engineering", major_name = "Computer Engineering", course_id = "01076002", course_group = "Core")
    kmitl.add_course_to_major(faculty_name = "Engineering", major_name = "Computer Engineering", course_id = "01076003", course_group = "Core")
    kmitl.add_course_to_major(faculty_name = "Engineering", major_name = "Computer Engineering", course_id = "01076004", course_group = "Elective")
    kmitl.add_course_to_major(faculty_name = "Engineering", major_name = "Computer Engineering", course_id = "01076005", course_group = "Elective")
    kmitl.add_course_to_major(faculty_name = "Engineering", major_name = "Computer Engineering", course_id = "90641002", course_group = "Elective")
    kmitl.add_course_to_major(faculty_name = "Engineering", major_name = "Computer Engineering", course_id = "90641003", course_group = "Elective")

                    


def init():
    init_student()
    init_teacher()
    init_course()
    init_section()
    init_enrollment()
    init_faculty()
    init_major()
    init_add_course_to_major()