import datetime

from Account import Account
from Transcript import Transcript
from Enrollment import Enrollment

class Student(Account):
    def __init__(self, student_id, password, email, student_name, citizen_id, major, faculty, year_entered = datetime.datetime.now().year):
        super().__init__(username = student_id, 
                         password = password,
                         email = email,
                         name = student_name,
                         citizen_id = citizen_id, 
                         user_type = "student")
        
        self.__student_id = student_id 
        self.__major = major 
        self.__faculty = faculty
        self.__year_entered = year_entered
        self.__transcript_list = []
    
    def to_dict(self):
        return {
            "student_id": self.__student_id,
            "email": super().email,
            "name": super().name,
            "citizen_id": super().citizen_id,
            "major": self.__major,
            "faculty": self.__faculty,
            "year_entered": self.__year_entered
        }

    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def major(self):
        return self.__major
    
    @property
    def faculty(self):
        return self.__faculty
    
    @property
    def year_entered(self):
        return self.__year_entered
    
    def enroll_to_section(self, section):
        transcript = self.get_transcript_by_semester_and_year(section.semester, section.year)

        # If the student does not have a transcript for the semester and year, create a new transcript
        if transcript is None:
            new_transcript = Transcript(section.semester, section.year)
            self.__transcript_list.append(new_transcript)

            return new_transcript.add_enrollment(self, section)

        return transcript.add_enrollment(self, section)
    
    def get_transcript_by_semester_and_year(self, semester, year):
        for transcript in self.__transcript_list:
            if transcript.semester == semester and transcript.year == year:
                return transcript
            
        return None
    
    def get_all_transcripts(self):
        result = []
        for transcript in self.__transcript_list:
            result.append(transcript.to_dict())
        return result
    
    def is_passed_course(self, course):
        for transcript in self.__transcript_list:
            for enrollment in transcript.enrollment_list:
                if enrollment.section.course == course and (enrollment.grade != "N/A" or enrollment.grade != "F"):
                    return True
        return False
    
    def get_grade_and_score_by_section(self, section):
        for transcript in self.__transcript_list:
            for enrollment in transcript.enrollment_list:
                if enrollment.section == section:
                    return enrollment.to_dict_with_student()
        return None
    