import datetime
import common
from common import Person

class Student(Person):
    def __init__(self, number:int, surname:str, firstname:str, dateOfBirth:datetime.date):
        super().__init__(surname, firstname, dateOfBirth)

        if(number is None):
            raise common.ValidationException("number required.")        
        self.Number = number