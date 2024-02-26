from Student import Student
from Teacher import Teacher
from Course import Course
from Section import Section
from University import kmitl  

def init_user():
    # Create Student
    kmitl.add_student( Student(name="Pooh", citizen_id="12345678", email="66010572@kmitl.ac.th",      
                               password="1234", student_id="66010572",
                               major="Computer", faculty="Engineering"))
    kmitl.add_student( Student(name="Oak", citizen_id="12345679", email="66010542@kmitl.ac.th",
                               password="1234", student_id="66010542",
                               major="Computer", faculty="Engineering"))
    kmitl.add_student( Student(name="Yo", citizen_id="12345680", email="66010533@kmitl.ac.th",
                               password="1234", student_id="66010533",
                                 major="Computer", faculty="Engineering"))
    kmitl.add_student( Student(name="Pea", citizen_id="12345681", email="66010587@kmitl.ac.th",
                               password="1234", student_id="66010587",
                                 major="Computer", faculty="Engineering"))
    
    # Create Teacher
    kmitl.add_teacher( Teacher(name="Thana", citizen_id="123425245", email="45778@kmitl.ac.th", password="1234", teacher_id="45778"))
    kmitl.add_teacher( Teacher(name="Jirasak", citizen_id="123425245", email="45779@kmitl.ac.th", password="1234", teacher_id="45779"))

def init_course():
    kmitl.add_course( Course(name = "OOP", id = "01076001", credit = 3,course_type= "Curriculum Course", grading_type="Normal" ))  
    kmitl.add_course( Course(name = "Discrete Math", id = "01076002", credit = 3,course_type= "Curriculum Course", grading_type="Normal" ))
    kmitl.add_course( Course(name = "Introduction to Computer Engineering", id = "01076003", credit = 3,course_type= "Curriculum Course", grading_type="Normal" ))
    kmitl.add_course( Course(name = "Charm School", id = "01076004", credit = 3,course_type= "GenEd", grading_type="Pass/Fail" ))
    kmitl.add_course( Course(name = "Foundation English 1 ", id = "01076005", credit = 3,course_type= "GenEd", grading_type="Pass/Fail" ))
    kmitl.add_course( Course(name = "Foundation English 2", id = "01076006", credit = 3,course_type= "GenEd", grading_type="Pass/Fail" ))

  
def init():
    init_user()
    init_course()