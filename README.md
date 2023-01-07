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