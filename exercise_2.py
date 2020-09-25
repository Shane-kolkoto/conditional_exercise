#Bright Light Company increase
print("Bright Light Company")
Annual_salary = int(input("Please enter your annual salary: "))
Monthly_salary= (Annual_salary/12)
print('Monthly salary: ', 'R', + Monthly_salary)
code = input("Please enter class group: ")
#class increase
a = 0.072
b = 0.068
c = 0.063

if code == "a":
    print('new salary: ', Monthly_salary * a + Monthly_salary)

elif code == "b":
    print('new salary: ', Monthly_salary * b + Monthly_salary)

elif code == "c":
    print('new salary: ', + Monthly_salary * c + Monthly_salary)
