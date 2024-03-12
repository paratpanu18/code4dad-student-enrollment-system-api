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
    
    kmitl.add_student(student_id = "66010544",
                      password = "12345",
                      email = "66010544@kmitl.ac.th",
                      name = "Pasut Siriwan",
                      citizen_id = "1234567890123",
                      major = "Computer Engineering",
                      faculty = "Engineering")

def init_teacher():
    kmitl.add_teacher(teacher_id = "teacher1",
                        password = "12345",
                        email = "teacher1@kmitl.ac.th",
                        name = "Sakchai Thipchaksurat",
                        citizen_id = "1234567890123")
    
    kmitl.add_teacher(teacher_id = "teacher2",
                        password = "12345",
                        email = "teacher2@kmitl.ac.th",
                        name = "Jirasak Sittigorn",
                        citizen_id = "1234567890124")
    
    kmitl.add_teacher(teacher_id = "teacher3",
                        password = "12345",
                        email = "teacher3@kmitl.ac.th",                      
                        name = "Thananchai Threepak",
                        citizen_id = "1458758962557")
    
    kmitl.add_teacher(teacher_id = "teacher4",
                        password = "12345",
                        email = "teacher4@gmail.com",
                        name = "Chutima Waiyasurasingha",
                        citizen_id = "1234567890123")
    
    kmitl.add_teacher(teacher_id = "teacher5",
                        password = "12345",
                        email = "teacher5@kmitl.ac.th",
                        name = "Thana Hongsuwan",
                        citizen_id = "1234567890123")
    
    kmitl.add_teacher(teacher_id = "teacher6",
                        password = "12345",
                        email = "teacher6@kmitl.ac.th",
                        name = "Orachat Chitsobhuk",
                        citizen_id = "1234567890123")
    
    kmitl.add_teacher(teacher_id = "teacher7",
                        password = "12345",
                        email = "teacher7@kmitl.ac.th",
                        name = "Amnarch Kaone",
                        citizen_id = "1234567890123")
    
    kmitl.add_teacher(teacher_id = "teacher8",
                        password = "12345",
                        email = "teacher8@kmitl.ac.th",
                        name = "Soraphong Wachirarattanapronkul",
                        citizen_id = "1234567890123")
    
    kmitl.add_teacher(teacher_id = "teacher9",
                        password = "12345",
                        email = "teacher9@kmitl.ac.th",
                        name = "CHINEBETH BORJA",
                        citizen_id = "1234567890123")
    
    kmitl.add_teacher(teacher_id = "teacher10",
                        password = "12345",
                        email = "teacher10@kmitl.ac.th",
                        name = "Kleddao Satcharoen",
                        citizen_id = "1234567890123")
    
def init_admin():
    kmitl.add_admin(admin_id = "admin1",
                    password = "12345",
                    email = "admin1@kmitl.ac.th",
                    name = "Admin1",
                    citizen_id = "1234567890123")
    

def init_course():

    GRADE = 0
    SATISFACTORY = 1

    GENED = 0
    FACULTY = 1
    CURRICULUM = 2

    # Year 1 - Semester 1
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

    kmitl.add_course(course_name = "Programming Fundamental",
                     course_id = "01076103", 
                     credit = 2, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    
    kmitl.add_course(course_name = "Programming Project",
                     course_id = "01076104", 
                     credit = 1, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)

    kmitl.add_course(course_name = "Digital Intelligence Quotient",  
                     course_id = "90641002", 
                     credit = 3, 
                     course_type = GENED, 
                     grading_type = SATISFACTORY)
    
    kmitl.add_course(course_name = "Pre-Activity Engineering",
                     course_id = "90642036", 
                     credit = 1, 
                     course_type = FACULTY, 
                     grading_type = GRADE)

    kmitl.add_course(course_name = "Foundation English1",
                     course_id = "90644007", 
                     credit = 3, 
                     course_type = GENED, 
                     grading_type = SATISFACTORY)
    
    # Year 1 - Semester 2
    kmitl.add_course(course_name = "Calculus 2",
                        course_id = "01076141", 
                        credit = 3, 
                        course_type = CURRICULUM, 
                        grading_type = GRADE)
    kmitl.add_pre_requisite_to_course("01076141", "01076140")       # Calculus 2 requires Calculus 1
    
    kmitl.add_course(course_name = "Object-Oriented Programming",
                     course_id = "01076105", 
                     credit = 2, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    kmitl.add_pre_requisite_to_course("01076105", "01076103")       # Object-Oriented Programming requires Programming Fundamental

    kmitl.add_course(course_name = "Object-Oriented Programming Project",
                     course_id = "01076106", 
                     credit = 1, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    kmitl.add_pre_requisite_to_course("01076106", "01076103")       # Object-Oriented Programming requires Programming Fundamental

    kmitl.add_course(course_name = "Circuit and Electronics",
                     course_id = "01076107", 
                     credit = 3, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    kmitl.add_pre_requisite_to_course("01076107", "01076001")       # Circuit and Electronics requires Introduction to Computer Engineering
    
    kmitl.add_course(course_name = "Circuit and Electronics in Practice",
                     course_id = "01076108", 
                     credit = 3, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    kmitl.add_pre_requisite_to_course("01076108", "01076001")       # Circuit and Electronics in Practice requires Introduction to Computer Engineering
    
    kmitl.add_course(course_name = "Foundation English 2",
                        course_id = "90641003", 
                        credit = 3, 
                        course_type = GENED, 
                        grading_type = SATISFACTORY)
    kmitl.add_pre_requisite_to_course("90641003", "90641002")       # Foundation English 2 requires Foundation English 1
    
    kmitl.add_course(course_name = "Discrete Structure",
                     course_id = "01076012", 
                     credit = 3, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    
    kmitl.add_course(course_name = "Charm School",
                     course_id = "90642999", 
                     credit = 3, 
                     course_type = FACULTY, 
                     grading_type = SATISFACTORY)
    
def init_section():
    # Year 1 - Semester 1
    # Introduction to Computer Engineering - Section 16
    kmitl.add_section(course_id = "01076001",
                        section_number = 16,
                        teacher_id = "teacher2",
                        max_student = 40,
                        location = "ECC-811",
                        schedule = "Tue 13:00 - 15:00",
                        semester = 1,
                        year = 2023)

    # Introduction to Computer Engineering - Section 17
    kmitl.add_section(course_id = "01076001",
                        section_number = 17,
                        teacher_id = "teacher2",
                        max_student = 40,
                        location = "ECC-811",
                        schedule = "Thu 09:00 - 12:00",
                        semester = 1,
                        year = 2023)

    # Programming Fundamental - Section 16
    kmitl.add_section(course_id = "01076103",
                        section_number = 16,
                        teacher_id = "teacher3",
                        max_student = 40,
                        location = "ECC-808",
                        schedule = "Mon 13:30 - 15:30",
                        semester = 1,
                        year = 2023)

    # Programming Fundamental - Section 17
    kmitl.add_section(course_id = "01076103",
                        section_number = 17,
                        teacher_id = "teacher3",
                        max_student = 40,
                        location = "ECC-808",
                        schedule = "Mon 09:30 - 11:30",
                        semester = 1,
                        year = 2023)

    # Programming Project - Section 116
    kmitl.add_section(course_id = "01076104",
                        section_number = 116,
                        teacher_id = "teacher3",
                        max_student = 40,
                        location = "ECC-708",
                        schedule = "Tue 09:00 - 12:00",
                        semester = 1,
                        year = 2023)

    # Programming Project - Section 117
    kmitl.add_section(course_id = "01076104",
                        section_number = 117,
                        teacher_id = "teacher3",
                        max_student = 40,
                        location = "ECC-708",
                        schedule = "Tue 13:00 - 16:00",
                        semester = 1,
                        year = 2023)

    # Calculus 1 - Section 16
    kmitl.add_section(course_id = "01076140",
                        section_number = 16,
                        teacher_id = "teacher1",
                        max_student = 40,
                        location = "ECC-802",
                        schedule = "Mon 09:00 - 12:00",
                        semester = 1,
                        year = 2023)

    # Calculus 1 - Section 17
    kmitl.add_section(course_id = "01076140",
                        section_number = 17,
                        teacher_id = "teacher1",
                        max_student = 40,
                        location = "ECC-802",
                        schedule = "Mon 13:00 - 16:00",
                        semester = 1,
                        year = 2023)

    # Digital Intelligence Quotient - Section 105
    kmitl.add_section(course_id = "90641002",
                        section_number = 105,
                        teacher_id = "teacher4",
                        max_student = 40,
                        location = "E12-508",
                        schedule = "Wed 09:00 - 12:00",
                        semester = 1,
                        year = 2023)
    
    # Foundation English 1 - Section 971
    kmitl.add_section(course_id = "90644007",
                        section_number = 971,
                        teacher_id = "teacher9",
                        max_student = 40,
                        location = "พระเทพ C-201A",
                        schedule = "Fri 09:00 - 12:00",
                        semester = 1,
                        year = 2023)

    # Year 1 - Semester 2
    # Discrete Structure - Section 16
    kmitl.add_section(course_id = "01076012",
                        section_number = 16,
                        teacher_id = "teacher3",
                        max_student = 40,
                        location = "ECC-810",
                        schedule = "Wed 13:00 - 16:00",
                        semester = 2,
                        year = 2023)
    
    # Discrete Structure - Section 17
    kmitl.add_section(course_id = "01076012",
                        section_number = 17,
                        teacher_id = "teacher3",
                        max_student = 40,
                        location = "ECC-810",
                        schedule = "Fri 13:00 - 16:00",
                        semester = 2,
                        year = 2023)
    
    # Object-Oriented Programming - Section 16
    kmitl.add_section(course_id = "01076105",
                        section_number = 16,
                        teacher_id = "teacher6",
                        max_student = 40,
                        location = "ECC-808",
                        schedule = "Tue 13:00 - 15:00",
                        semester = 2,
                        year = 2023)
    
    # Object-Oriented Programming Project - Section 116
    kmitl.add_section(course_id = "01076106",
                        section_number = 116,
                        teacher_id = "teacher6",
                        max_student = 40,
                        location = "ECC-808",
                        schedule = "Tue 15:00 - 18:00",
                        semester = 2,
                        year = 2023)
    
    # Object-Oriented Programming - Section 17
    kmitl.add_section(course_id = "01076105",
                        section_number = 17,
                        teacher_id = "teacher5",
                        max_student = 40,
                        location = "ECC-811",
                        schedule = "Wed 13:00 - 15:00",
                        semester = 2,
                        year = 2023)
    
    # Object-Oriented Programming Project - Section 117
    kmitl.add_section(course_id = "01076106",
                        section_number = 117,
                        teacher_id = "teacher5",
                        max_student = 40,
                        location = "ECC-811",
                        schedule = "Wed 15:00 - 18:00",
                        semester = 2,
                        year = 2023)
    
    # Circuit and Electronics - Section 16
    kmitl.add_section(course_id = "01076107",
                        section_number = 16,
                        teacher_id = "teacher7",
                        max_student = 40,
                        location = "ECC-502",
                        schedule = "Mon 13:00 - 16:00",
                        semester = 2,
                        year = 2023)
    
    # Circuit and Electronics in Practice - Section 116
    kmitl.add_section(course_id = "01076108",
                        section_number = 116,
                        teacher_id = "teacher8",
                        max_student = 40,
                        location = "ECC-502",
                        schedule = "Tue 09:00 - 12:00",
                        semester = 2,
                        year = 2023)
    
    # Circuit and Electronics - Section 17
    kmitl.add_section(course_id = "01076107",
                        section_number = 17,
                        teacher_id = "teacher7",
                        max_student = 40,
                        location = "ECC-502",
                        schedule = "Mon 09:00 - 12:00",
                        semester = 2,
                        year = 2023)
    
    # Circuit and Electronics in Practice - Section 117
    kmitl.add_section(course_id = "01076108",
                        section_number = 117,
                        teacher_id = "teacher8",
                        max_student = 40,
                        location = "ECC-502",
                        schedule = "Tue 13:00 - 16:00",
                        semester = 2,
                        year = 2023)
    
    # Calculus 2 - Section 16
    kmitl.add_section(course_id = "01076141",
                        section_number = 16,
                        teacher_id = "teacher1",
                        max_student = 40,
                        location = "ECC-802",
                        schedule = "Mon 09:00 - 12:00",
                        semester = 2,
                        year = 2023)
    
    # Calculus 2 - Section 17
    kmitl.add_section(course_id = "01076141",
                        section_number = 17,
                        teacher_id = "teacher1",
                        max_student = 40,
                        location = "ECC-802",
                        schedule = "Mon 13:00 - 16:00",
                        semester = 2,
                        year = 2023)
    
    # Foundation English 2 - Section 984
    kmitl.add_section(course_id = "90641003",
                        section_number = 984,
                        teacher_id = "teacher9",
                        max_student = 40,
                        location = "พระเทพ C-201B",
                        schedule = "Fri 09:00 - 12:00",
                        semester = 2,
                        year = 2023)
    

    # Charm School - Section 904
    kmitl.add_section(course_id = "90642999",
                        section_number = 904,
                        teacher_id = "teacher10",
                        max_student = 40,
                        location = "พระเทพ D-109",
                        schedule = "Wed 09:00 - 12:00",
                        semester = 2,
                        year = 2023)

def init_enrollment():
    # Year 1 - Semester 1
    # 66010542 - Paratpanu Pechsaman
    kmitl.enroll_student_to_section(student_id = "66010542",
                                        course_id = "01076001", # Introduction to Computer Engineering
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010542",
                                    course_id = "01076001",
                                    section_number = 16,
                                    grade = "A",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010542",
                                        course_id = "01076103", # Programming Fundamental
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    
    kmitl.assign_grade_to_student(student_id = "66010542",
                                    course_id = "01076103",
                                    section_number = 16,
                                    grade = "A",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010542",
                                        course_id = "01076104", # Programming Project
                                        section_number = 116,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010542",
                                    course_id = "01076104",
                                    section_number = 116,
                                    grade = "A",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010542",
                                        course_id = "01076140", # Calculus 1
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010542",
                                    course_id = "01076140",
                                    section_number = 16,
                                    grade = "A",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010542",
                                        course_id = "90641002", # Digital Intelligence Quotient
                                        section_number = 105,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010542",
                                    course_id = "90641002",
                                    section_number = 105,
                                    grade = "S",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010542",
                                        course_id = "90644007", # Foundation English 1
                                        section_number = 971,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010542",
                                    course_id = "90644007",
                                    section_number = 971,
                                    grade = "S",
                                    semester = 1,
                                    year = 2023)
    
    # 66010533 - Prompipat Thongtub
    kmitl.enroll_student_to_section(student_id = "66010533",
                                        course_id = "01076001", # Introduction to Computer Engineering
                                        section_number = 17,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010533",
                                    course_id = "01076001",
                                    section_number = 17,
                                    grade = "C",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010533",
                                        course_id = "01076103", # Programming Fundamental
                                        section_number = 17,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010533",
                                    course_id = "01076103",
                                    section_number = 17,
                                    grade = "D+",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010533",
                                        course_id = "01076104", # Programming Project
                                        section_number = 117,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010533",
                                    course_id = "01076104",
                                    section_number = 117,
                                    grade = "B",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010533",
                                        course_id = "01076140", # Calculus 1
                                        section_number = 17,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010533",
                                    course_id = "01076140",
                                    section_number = 17,
                                    grade = "D",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010533",
                                        course_id = "90641002", # Digital Intelligence Quotient
                                        section_number = 105,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010533",
                                    course_id = "90641002",
                                    section_number = 105,
                                    grade = "S",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010533",
                                        course_id = "90644007", # Foundation English 1
                                        section_number = 971,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010533",
                                    course_id = "90644007",
                                    section_number = 971,
                                    grade = "S",
                                    semester = 1,
                                    year = 2023)
    
    # 66010572 - Pipatpong Panpreuak
    kmitl.enroll_student_to_section(student_id = "66010572",
                                        course_id = "01076001", # Introduction to Computer Engineering
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010572",
                                    course_id = "01076001",
                                    section_number = 16,
                                    grade = "B",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010572",
                                        course_id = "01076103", # Programming Fundamental
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010572",
                                    course_id = "01076103",
                                    section_number = 16,
                                    grade = "A",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010572",
                                        course_id = "01076104", # Programming Project
                                        section_number = 116,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010572",
                                    course_id = "01076104",
                                    section_number = 116,
                                    grade = "A",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010572",
                                        course_id = "01076140", # Calculus 1
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010572",
                                    course_id = "01076140",
                                    section_number = 16,
                                    grade = "F",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010572",
                                        course_id = "90641002", # Digital Intelligence Quotient
                                        section_number = 105,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010572",
                                    course_id = "90641002",
                                    section_number = 105,
                                    grade = "S",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010572",
                                        course_id = "90644007", # Foundation English 1
                                        section_number = 971,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010572",
                                    course_id = "90644007",
                                    section_number = 971,
                                    grade = "S",
                                    semester = 1,
                                    year = 2023)
    
    # 66010587 - Pearapat Kumsing
    kmitl.enroll_student_to_section(student_id = "66010587",
                                        course_id = "01076001", # Introduction to Computer Engineering
                                        section_number = 17,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010587",
                                    course_id = "01076001",
                                    section_number = 17,
                                    grade = "F",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010587", 
                                        course_id = "01076103", # Programming Fundamental
                                        section_number = 17,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010587",
                                    course_id = "01076103",
                                    section_number = 17,
                                    grade = "F",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010587",
                                        course_id = "01076104", # Programming Project
                                        section_number = 117,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010587",
                                    course_id = "01076104",
                                    section_number = 117,
                                    grade = "F",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010587",
                                        course_id = "01076140", # Calculus 1
                                        section_number = 17,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010587",
                                    course_id = "01076140",
                                    section_number = 17,
                                    grade = "F",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010587",
                                        course_id = "90641002", # Digital Intelligence Quotient
                                        section_number = 105,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010587",
                                    course_id = "90641002",
                                    section_number = 105,
                                    grade = "U",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010587",
                                        course_id = "90644007", # Foundation English 1
                                        section_number = 971,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010587",
                                    course_id = "90644007",
                                    section_number = 971,
                                    grade = "S",
                                    semester = 1,
                                    year = 2023)
    
    # 66010544 - Pasut Siriwan
    kmitl.enroll_student_to_section(student_id = "66010544",
                                        course_id = "01076001", # Introduction to Computer Engineering
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010544",
                                    course_id = "01076001",
                                    section_number = 16,
                                    grade = "C",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010544",
                                        course_id = "01076103", # Programming Fundamental
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010544",
                                    course_id = "01076103",
                                    section_number = 16,
                                    grade = "B",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010544",
                                        course_id = "01076104", # Programming Project
                                        section_number = 116,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010544",
                                    course_id = "01076104",
                                    section_number = 116,
                                    grade = "A",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010544",
                                        course_id = "01076140", # Calculus 1
                                        section_number = 16,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010544",
                                    course_id = "01076140",
                                    section_number = 16,
                                    grade = "F",
                                    semester = 1,
                                    year = 2023)
    
    kmitl.enroll_student_to_section(student_id = "66010544",
                                        course_id = "90641002", # Digital Intelligence Quotient
                                        section_number = 105,
                                        semester = 1,
                                        year = 2023)
    kmitl.assign_grade_to_student(student_id = "66010544",
                                    course_id = "90641002",
                                    section_number = 105,
                                    grade = "S",
                                    semester = 1,
                                    year = 2023)

def init_faculty():
    kmitl.add_faculty(faculty_name = "Engineering")
    kmitl.add_faculty(faculty_name = "Architecture")
    kmitl.add_faculty(faculty_name = "Science")
    kmitl.add_faculty(faculty_name = "Industrial Education")
    kmitl.add_faculty(faculty_name = "Information Technology")
    kmitl.add_faculty(faculty_name = "Agro-Industry")
    kmitl.add_faculty(faculty_name = "Management Science")

def init_major():
    kmitl.add_major(major_name = "Computer Engineering", 
                    academic_fees= 25000, 
                    faculty_name = "Engineering")
    kmitl.add_major(major_name = "Civil Engineering", 
                    academic_fees= 25000, 
                    faculty_name = "Engineering")
    kmitl.add_major(major_name = "Architecture", 
                    academic_fees= 25000, 
                    faculty_name = "Architecture")
    kmitl.add_major(major_name = "Physics", 
                    academic_fees= 25000, faculty_name = "Science")
    kmitl.add_major(major_name = "Chemistry", 
                    academic_fees= 25000, 
                    faculty_name = "Science")
    kmitl.add_major(major_name = "Biology", 
                    academic_fees= 25000, 
                    faculty_name = "Science")
    kmitl.add_major(major_name = "Industrial Education", 
                    academic_fees= 25000, 
                    faculty_name = "Industrial Education")
    kmitl.add_major(major_name = "Information Technology", 
                    academic_fees= 25000, 
                    faculty_name = "Information Technology")
    kmitl.add_major(major_name = "Agro-Industry", 
                    academic_fees= 25000, 
                    faculty_name = "Agro-Industry")
    kmitl.add_major(major_name = "Management Science", 
                    academic_fees= 25000, 
                    faculty_name = "Management Science")

def init_add_course_to_major():
    pass

def init_co_requisite():
    kmitl.add_co_requisite_to_course_section(course_id = "01076105",
                                             section_number= 17,
                                            co_requisite_course_id = "01076106",
                                            co_requisite_section_number= 117)
    
    kmitl.add_co_requisite_to_course_section(course_id = "01076106",
                                            section_number= 117,
                                            co_requisite_course_id = "01076105",
                                            co_requisite_section_number= 17)
    
    kmitl.add_co_requisite_to_course_section(course_id = "01076107",
                                            section_number= 17,
                                            co_requisite_course_id = "01076108",
                                            co_requisite_section_number= 117)
    
    kmitl.add_co_requisite_to_course_section(course_id = "01076108",
                                            section_number= 117,
                                            co_requisite_course_id = "01076107",
                                            co_requisite_section_number= 17)
    
    kmitl.add_co_requisite_to_course_section(course_id = "01076107",
                                            section_number= 16,
                                            co_requisite_course_id = "01076108",
                                            co_requisite_section_number= 116)
    
    kmitl.add_co_requisite_to_course_section(course_id = "01076108",
                                            section_number= 116,
                                            co_requisite_course_id = "01076107",
                                            co_requisite_section_number= 16)
    
    
def init():
    init_student()
    init_teacher()
    init_admin()
    init_course()
    init_section()
    init_enrollment()
    init_faculty()
    init_major()
    init_add_course_to_major()
    init_co_requisite()