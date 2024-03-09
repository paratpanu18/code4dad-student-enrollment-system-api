class Grade:
    def __init__(self, grade):
        self.__grade = grade
        self.__score_1 = None
        self.__score_2 = None 
        self.__score_3 = None
        self.__score_4 = None
    
    @property
    def grade(self):
        return self.__grade
    
    @property
    def score_1(self):
        return self.__score_1
    
    @property
    def score_2(self):
        return self.__score_2
    
    @property
    def score_3(self):
        return self.__score_3
    
    @property
    def score_4(self):
        return self.__score_4
    
    def to_dict(self):
        return {
            "grade": self.__grade,
            "score_1": self.__score_1,
            "score_2": self.__score_2,
            "score_3": self.__score_3,
            "score_4": self.__score_4
        }
    