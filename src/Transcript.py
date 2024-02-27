class Transcript():
    def __init__(self, year, semester, total_credit ):
        self.__year = year
        self.__semester = semester
        self.__total_credit = total_credit
        self.__enrollment_list = []
        self.__total_credit = 0
        self.__GPA = None
        self.__GPS = None
    
    def get_data(self):
        return {
            "year" : self.__year,
            "semester" : self.__semester,
            "total_credit" : self.__total_credit,
            "GPA" : self.__GPA,
            "GPS" : self.__GPS
        }