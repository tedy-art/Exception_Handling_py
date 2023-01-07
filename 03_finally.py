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