from Student import Student
from Teacher import Teacher
from University import kmitl  

def init_user():
    # Create Student
    kmitl.add_student( Student(name="Pooh", citizen_id="12345678", email="66010572@kmitl.ac.th",      
                               password="1234", is_graduated=False, student_id="66010572",
                               major="Computer", faculty="Engineering"))
    kmitl.add_student( Student(name="Oak", citizen_id="12345679", email="66010542@kmitl.ac.th",
                               password="1234", is_graduated=False, student_id="66010542",
                               major="Computer", faculty="Engineering"))
    kmitl.add_student( Student(name="Yo", citizen_id="12345680", email="66010533@kmitl.ac.th",
                               password="1234", is_graduated=False, student_id="66010533",
                                 major="Computer", faculty="Engineering"))
    kmitl.add_student( Student(name="Pea", citizen_id="12345681", email="66010587@kmitl.ac.th",
                               password="1234", is_graduated=False, student_id="66010587",
                                 major="Computer", faculty="Engineering"))
    
    # Create Teacher
    kmitl.add_teacher( Teacher(name="Thana", citizen_id="123425245", email="45778@kmitl.ac.th", password="1234", teacher_id="45778"))
    kmitl.add_teacher( Teacher(name="Jirasak", citizen_id="123425245", email="45779@kmitl.ac.th", password="1234", teacher_id="45779"))

def init():
    init_user()