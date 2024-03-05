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

def init_course():

    GRADE = 0
    SATISFACTORY = 1

    GENED = 0
    FACULTY = 1
    CURRICULUM = 2

    # Engineering courses
    kmitl.add_course(course_name = "Calculus 1", 
                     course_id = "01076140", 
                     credit = 3, 
                     course_type = CURRICULUM, 
                     grading_type = GRADE)
    
    kmitl.add_course(course_name = "Calculus 2",
                        course_id = "01076141", 
                        credit = 3, 
                        course_type = CURRICULUM, 
                        grading_type = GRADE)
    
    kmitl.add_pre_requisite_to_course("01076141", "01076140")       # Calculus 2 requires Calculus 1
    

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
    
    kmitl.add_course(course_name = "Foundation English1",
                     course_id = "90641002", 
                     credit = 3, 
                     course_type = GENED, 
                     grading_type = SATISFACTORY)
    
    kmitl.add_course(course_name = "Foundation English2",
                        course_id = "90641003", 
                        credit = 3, 
                        course_type = GENED, 
                        grading_type = SATISFACTORY)
    
    kmitl.add_pre_requisite_to_course("90641003", "90641002")       # Foundation English2 requires Foundation English1
    
    # Science courses
    kmitl.add_course(course_name="Physics 1",
                     course_id="02076001",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Chemistry 1",
                     course_id="02076002",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Biology 1",
                     course_id="02076003",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    # Architecture courses
    kmitl.add_course(course_name="Architectural Design 1",
                     course_id="03076001",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Architectural History",
                     course_id="03076002",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Structural Mechanics",
                     course_id="03076003",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    # Industrial Education courses
    kmitl.add_course(course_name="Industrial Design",
                     course_id="04076001",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Manufacturing Processes",
                     course_id="04076002",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Quality Control",
                     course_id="04076003",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    # Information Technology courses
    kmitl.add_course(course_name="Database Management Systems",
                     course_id="05076001",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Web Programming",
                     course_id="05076002",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Cybersecurity Fundamentals",
                     course_id="05076003",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    # Agro-Industry courses
    kmitl.add_course(course_name="Agricultural Economics",
                     course_id="06076001",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Crop Science",
                     course_id="06076002",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Food Technology",
                     course_id="06076003",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    # Management Science courses
    kmitl.add_course(course_name="Principles of Management",
                     course_id="07076001",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Organizational Behavior",
                     course_id="07076002",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

    kmitl.add_course(course_name="Business Ethics",
                     course_id="07076003",
                     credit=3,
                     course_type=CURRICULUM,
                     grading_type=GRADE)

def init_section():
    # Calculus 1 - Section 16
    kmitl.add_section(course_id = "01076140",
                        section_number = 16,
                        teacher_id = "teacher1",
                        max_student = 50,
                        location = "ECC-802",
                        schedule = "Mon 09:00 - 12:00",
                        semester = 1,
                        year = 2024)

    # Calculus 1 - Section 17
    kmitl.add_section(course_id = "01076140",
                        section_number = 17,
                        teacher_id = "teacher1",
                        max_student = 50,
                        location = "ECC-802",
                        schedule = "Mon 13:00 - 16:00",
                        semester = 1,
                        year = 2024)
    
    # Calculus 2 - Section 16
    kmitl.add_section(course_id = "01076141",
                        section_number = 16,
                        teacher_id = "teacher1",
                        max_student = 50,
                        location = "ECC-802",
                        schedule = "Tue 09:00 - 12:00",
                        semester = 1,
                        year = 2024)
    
    # Calculus 2 - Section 17
    kmitl.add_section(course_id = "01076141",
                        section_number = 17,
                        teacher_id = "teacher1",
                        max_student = 50,
                        location = "ECC-802",
                        schedule = "Tue 13:00 - 16:00",
                        semester = 1,
                        year = 2024)

    # Introduction to Computer Engineering - Section 16
    kmitl.add_section(course_id = "01076001",
                        section_number = 16,
                        teacher_id = "teacher2",
                        max_student = 50,
                        location = "ECC-811",
                        schedule = "Wed 13:00 - 16:30",
                        semester = 1,
                        year = 2024)
    
    # Introduction to Computer Engineering - Section 17
    kmitl.add_section(course_id = "01076001",
                        section_number = 17,
                        teacher_id = "teacher2",
                        max_student = 50,
                        location = "ECC-811",
                        schedule = "Wed 08:30 - 12:00",
                        semester = 1,
                        year = 2024)
    
    # Programming Fundamental - Section 16
    kmitl.add_section(course_id = "01076002",
                        section_number = 16,
                        teacher_id = "teacher3",
                        max_student = 50,
                        location = "ECC-810",
                        schedule = "Mon 13:00 - 16:00",
                        semester = 1,
                        year = 2024)
    
    # Programming Fundamental - Section 17
    kmitl.add_section(course_id = "01076002",
                        section_number = 17,
                        teacher_id = "teacher3",
                        max_student = 50,
                        location = "ECC-810",
                        schedule = "Mon 09:00 - 12:00",
                        semester = 1,
                        year = 2024)

def init_enrollment():
    # 66010542
    kmitl.enroll_student_to_section(student_id = "66010542",
                                    course_id = "01076140",     # Calculus 1
                                    section_number = 16)
    
    kmitl.enroll_student_to_section(student_id = "66010542",
                                    course_id = "01076001",     # Introduction to Computer Engineering
                                    section_number = 16)
    
    kmitl.enroll_student_to_section(student_id = "66010542",
                                    course_id = "01076002",     # Programming Fundamental
                                    section_number = 16)
    

    # 66010572
    kmitl.enroll_student_to_section(student_id = "66010572",
                                    course_id = "01076140",     # Calculus 1
                                    section_number = 17)
    
    kmitl.enroll_student_to_section(student_id = "66010572",
                                    course_id = "01076001",     # Introduction to Computer Engineering
                                    section_number = 17)
    
    kmitl.enroll_student_to_section(student_id = "66010572",
                                    course_id = "01076002",     # Programming Fundamental
                                    section_number = 17)
    

    # 66010533
    kmitl.enroll_student_to_section(student_id = "66010533",
                                    course_id = "01076140",     # Calculus 1
                                    section_number = 16)
    
    kmitl.enroll_student_to_section(student_id = "66010533",
                                    course_id = "01076001",     # Introduction to Computer Engineering
                                    section_number = 16)
    

    # 66010587
    kmitl.enroll_student_to_section(student_id = "66010587",
                                    course_id = "01076140",
                                    section_number = 17)
    
    kmitl.enroll_student_to_section(student_id = "66010587",
                                    course_id = "01076001",
                                    section_number = 17)
    
    
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
    #Computer Engineering
    kmitl.add_course_to_major(faculty_name = "Engineering", 
                              major_name = "Computer Engineering", 
                              course_id = "01076140", 
                              course_group = "Core")
    kmitl.add_course_to_major(faculty_name = "Engineering", 
                              major_name = "Computer Engineering", 
                              course_id = "01076001", 
                              course_group = "Core")
    kmitl.add_course_to_major(faculty_name = "Engineering", 
                              major_name = "Computer Engineering", 
                              course_id = "01076002", 
                              course_group = "Core")
    kmitl.add_course_to_major(faculty_name = "Engineering", 
                              major_name = "Computer Engineering", 
                              course_id = "01076003", 
                              course_group = "Core")
    kmitl.add_course_to_major(faculty_name = "Engineering", 
                              major_name = "Computer Engineering", 
                              course_id = "01076004", 
                              course_group = "Elective")
    kmitl.add_course_to_major(faculty_name = "Engineering", 
                              major_name = "Computer Engineering", 
                              course_id = "01076005", 
                              course_group = "Elective")
    kmitl.add_course_to_major(faculty_name = "Engineering", 
                              major_name = "Computer Engineering", 
                              course_id = "90641002", 
                              course_group = "Elective")
    kmitl.add_course_to_major(faculty_name = "Engineering", 
                              major_name = "Computer Engineering", 
                              course_id = "90641003", 
                              course_group = "Elective")

    # Science - Physics
    kmitl.add_course_to_major(faculty_name="Science",
                               major_name="Physics",
                               course_id="02076001",
                               course_group="Core")

    # Science - Chemistry
    kmitl.add_course_to_major(faculty_name="Science",
                               major_name="Chemistry",
                               course_id="02076002",
                               course_group="Core")

    # Science - Biology
    kmitl.add_course_to_major(faculty_name="Science",
                               major_name="Biology",
                               course_id="02076003",
                               course_group="Core")

    # Architecture - Architecture
    kmitl.add_course_to_major(faculty_name="Architecture",
                               major_name="Architecture",
                               course_id="03076001",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Architecture",
                               major_name="Architecture",
                               course_id="03076002",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Architecture",
                               major_name="Architecture",
                               course_id="03076003",
                               course_group="Core")

    # Industrial Education - Industrial Education
    kmitl.add_course_to_major(faculty_name="Industrial Education",
                               major_name="Industrial Education",
                               course_id="04076001",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Industrial Education",
                               major_name="Industrial Education",
                               course_id="04076002",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Industrial Education",
                               major_name="Industrial Education",
                               course_id="04076003",
                               course_group="Core")

    # Information Technology - Information Technology
    kmitl.add_course_to_major(faculty_name="Information Technology",
                               major_name="Information Technology",
                               course_id="05076001",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Information Technology",
                               major_name="Information Technology",
                               course_id="05076002",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Information Technology",
                               major_name="Information Technology",
                               course_id="05076003",
                               course_group="Core")

    # Agro-Industry - Agro-Industry
    kmitl.add_course_to_major(faculty_name="Agro-Industry",
                               major_name="Agro-Industry",
                               course_id="06076001",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Agro-Industry",
                               major_name="Agro-Industry",
                               course_id="06076002",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Agro-Industry",
                               major_name="Agro-Industry",
                               course_id="06076003",
                               course_group="Core")

    # Management Science - Management Science
    kmitl.add_course_to_major(faculty_name="Management Science",
                               major_name="Management Science",
                               course_id="07076001",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Management Science",
                               major_name="Management Science",
                               course_id="07076002",
                               course_group="Core")
    kmitl.add_course_to_major(faculty_name="Management Science",
                               major_name="Management Science",
                               course_id="07076003",
                               course_group="Core")

                    
def init():
    init_student()
    init_teacher()
    init_course()
    init_section()
    init_enrollment()
    init_faculty()
    init_major()
    init_add_course_to_major()