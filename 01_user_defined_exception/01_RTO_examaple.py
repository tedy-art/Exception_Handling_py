class AgeTooSmallError(Exception):
    def __init__(self, msg):
        self.msg = msg

class AgeTooBigError(Exception):
    def __init__(self, msg):
        self.msg = msg

age = eval(input("Enter your age :"))
if age < 18:
    raise AgeTooSmallError("Your age is too small for RTO Lincence..")

if age > 65:
    raise AgeTooBigError("Your age is too big for RTO Lincence..")