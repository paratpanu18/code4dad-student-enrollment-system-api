class Grade():
    def __init__(self, grade =None , score1 = None, score2 = None, score3 = None, score4 = None):
        self.__grade = None
        self.__score1 = None
        self.__score2 = None
        self.__score3 = None
        self.__score4 = None
        self.__status_grade = False

    @property
    def grade(self):
        return self.__grade
    @property.setter
    def grade(self, grade):
        self.__grade = grade
    
    @property
    def score1(self):
        return self.__score1
    @property.setter
    def score1(self, score1):
        self.__score1 = score1
    
    @property
    def score2(self):
        return self.__score2
    @property.setter
    def score2(self, score2):
        self.__score2 = score2

    @property
    def score3(self):
        return self.__score3
    @property.setter
    def score3(self, score3):
        self.__score3 = score3
    
    @property
    def score4(self):
        return self.__score4
    @property.setter
    def score4(self, score4):
        self.__score4 = score4
    
    @property
    def status_grade(self):
        return self.__status_grade
    @property.setter
    def status_grade(self, status_grade):
        self.__status_grade = status_grade

    def get_data(self):
        return {
            "grade" : self.__grade,
            "score1" : self.__score1,
            "score2" : self.__score2,
            "score3" : self.__score3,
            "score4" : self.__score4,
            "status_grade" : self.__status_grade
        }
    

        