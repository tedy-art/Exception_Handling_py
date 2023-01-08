print("Student presenty report")

class studentIneligiblePresenty(Exception):
    def __init__(self, msg):
        self.msg = msg

class studentIsNotPresentInMock(Exception):
    def __init__(self, msg):
        self.msg = msg

presenty = eval(input("Enter student presenty : "))
mock = input("Did the student take the mock exam[y/n] : ")

if presenty < 75:
    raise studentIneligiblePresenty("Studnet is Ineligible for exam.")

elif  mock.lower() != 'y':
    raise studentIsNotPresentInMock("Student is Ineligible for exam")
else:
    print("Studnet is eligible for exam.")