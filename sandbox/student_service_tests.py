import unittest
import datetime
import common as c, student_service as s

class Student_ctor(unittest.TestCase):
    __number:int = 1
    __surname = "Doe" 
    __firstName = "John"
    __dateOfBirth = datetime.date(2010,1,1)

    def test_raises_exception_on_null_number(self):
        with self.assertRaises(c.ValidationException):
            s.Student(None, self.__surname, self.__firstName, self.__dateOfBirth)

    def test_raises_exception_on_null_surname(self):
        with self.assertRaises(c.ValidationException):
            s.Student(self.__number, None, self.__firstName, self.__dateOfBirth)

    def test_raises_exception_on_null_firstname(self):
        with self.assertRaises(c.ValidationException):
            s.Student(self.__number, self.__surname, None, self.__dateOfBirth)

    def test_raises_exception_on_null_dateOfBirth(self):
        with self.assertRaises(c.ValidationException):
            s.Student(self.__number,self.__surname, self.__firstName, None)

    def test_assigns_values_correctly(self):
        student = s.Student(self.__number, self.__surname, self.__firstName, self.__dateOfBirth)
   
        self.assertEqual(self.__number, student.Number)
        self.assertEqual(self.__surname, student.Surname)
        self.assertEqual(self.__firstName, student.FirstName)
        self.assertEqual(self.__dateOfBirth, student.DateOfBirth)

if __name__ == '__main__':
    unittest.main()