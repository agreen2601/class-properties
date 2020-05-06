class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort = 0

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return "First Name Attribute Error"

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("Provide a string for the first name.")

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return "Last Name Attribute Error"

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("Provide a string for the last name.")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return "Age Attribute Error"

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Provide an integer for the age.")

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return "Cohort Attribute Error"

    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError("Provide an integer for the cohort.")

    @property
    def full_name(self):
        try:
            return self.first_name + " " + self.last_name
        except AttributeError:
            return "Full Name Attribute Error"

    def __str__(self):
        return(f'My name is {self.full_name}, I am {self.age} years old and I am in cohort {self.cohort}.')

andrew = Student()
andrew.first_name = "Andrew"
andrew.last_name = "Green"
andrew.age = 31
andrew.cohort = 38

print(andrew)
