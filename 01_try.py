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