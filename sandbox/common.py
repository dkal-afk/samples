import datetime

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class SystemClock:
    def Now(self):
       return datetime.date

class Person(object):
    def __init__(self, surname:str, firstname:str, dateOfBirth:datetime.date):
        if(surname is None):
            raise ValidationException("surname required") 
        self.Surname = surname

        if(firstname is None):
            raise ValidationException("firstname required")
        self.FirstName = firstname
        
        if(dateOfBirth is None):
            raise ValidationException("dateofBirth required")
        self.DateOfBirth = dateOfBirth
