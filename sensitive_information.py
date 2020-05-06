class Patient:
    def __init__(self, ssn, dob, health_ins_acc_num, first_name, last_name, address):
        self.ssn = ssn
        self.dob = dob
        self.health_ins_acc_num = health_ins_acc_num
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    @property
    def ssn(self):
        try:
            return self.__ssn
        except AttributeError:
            return 0

    @ssn.setter
    def ssn(self, ssn):
        if self.ssn is 0 and type(ssn) is str:
            self.__ssn = ssn
        elif self.ssn is not 0:
            raise AttributeError("Cannot change SSN")
        elif type(ssn) is not str:
            raise TypeError("SSN must be a string")


androoper = Patient("123-45-6789", "12/34/56", "1234567890", "Androoper", "Grichols", "123 Road St.")

androoper.dob = "2"
# androoper.ssn = "this should raise the attribute error"

print(f'SSN: {androoper.ssn}')
