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
                     course_id = "90641002", 
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


def init():
    init_student()
    init_teacher()
    init_course()
    init_section()
    init_enrollment()