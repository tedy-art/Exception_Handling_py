Exception Handling :-

    -> Unwanted, unexpected even which distrub the normal flow of program 
       is called exception.

    -> Exception is nothing but run time error.

    -> At the time of exception program terminates abnormally(AT = Abnormal
       Termination).

    -> In program there is no error and my total program executed without 
       error is called NT(Normal Termination).

Exception Handling :-

    "defining the alternative way to continue my rest of program so that at
     the end will get NT(Normal Termination)."


4 Important key words in exception handling:-
    1) try
    2) except
    3) else
    4) finally

if we want to define our own error:
    5) raise -> define our own error

try :-

    -> To write risky code.
    -> The code which may raise error that code is risky code.
    -> The code which raise error tjat code we have write inside try block
    
    syntax:-
        try:
            riskey code
        except ExceptionName:
            error handling logic
            Note: Exception handling is optional

    e.g.
    a = 10
    b = 20

    # b = 0 # try it

    try:
        # If there is no error then try block execute
        c = a/b
        print(c)

    except Exception as e:
        # If try block throws error then except block will execute.
        print(e)
        print("Pls dont divide by Zero")

    print('Its over')
    print("bye bye")


except :-

    -> Error handling logic.
    -> If there is an error in try block then and then only except block 
       will execute.
    -> When we use try block then it is mendeatory to use except block.

    syntax:-
        try:
            riskey code
        except ExceptionName:
            error handling logic
            Note: Exception handling is optional

    e.g.
    a = 10
    b = 20

    # b = 0 # try it

    try:
        # If there is no error then try block execute
        c = a/b

    except ZeroDivisionError as e:
        # If try block throws error then except block will execute.
        print(e)
        print("Plz dont divide by zero")

    print("It's over")
    print("Bye Bye")
       

else :-

    -> If there is no error then else block will execute.
    -> It is not compulsary.

    syntax:-
        try:
            riskey code
        except ExceptionName:
            error handling logic
            Note: Exception handling is optional
        else:
            If there is no error in try block then execute these group of statement.

    e.g.
            a = 10
            b = 20

            # b = 0 # try it

            try:
                # If there is no error then try block execute
                c = a/b

            except ZeroDivisionError as e:
                # If try block throws error then except block will execute.
                print(e)
                print("Plz dont divide by zero")

            else:
                # If try execute successfully then else block will run
                print(c)

            print("It's over")
            print("Bye Bye")

finally :-
    -> This finally will excute always.
    -> Irrespective of error it will execute.
    -> clean-up activity.

    syntax:-
        try:
            riskey code
        
        except ExceptionName:
            error handling logic
            Note: Exception handling is optional
        
        else:
            If there is no error in try block then execute these group of statement.

        finally:
            clean-up code

    e.g.
        a = 10
        # b = 20

        b = 0 # try it

        try:
            # If there is no error then try block will execute
            c = a/b

        except ZeroDivisionError as e:
            # If try block throws error then except block will execute.
            print(e)
            print("Plz dont divide by zero")

        else:
            # If try execute successfully then else block will run
            print(c)

        finally:
            # Finally always run
            print("It's over")
            print("Bye Bye")

There are two types of exception:-
    1] In-built
    2] Customize or user define exception

1] In-built exception:-
    ZeroDivisionError, ValueError, FileNotFoundError, etc...

2] Customize or user defined exception:-
-> We can create our own exception

    Q. How to create  user defined exception?? 
    -> One python exception is equal to one exception(error).

    -> we can raise error by using raise keyword

    syntax:

    class class_name(Exception):
        def __init__(self, msg):
            self.msg = msg

    syntax for raise:-
        raise class_name('msg')
    
    e.g. 
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


    e.g.
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