contract_type =str(input("Please state your contract type: "))
if contract_type == "full time":
    income_tax = 0.295 #29.5% income tax
    Annual_salary = int(input("Please enter your annual salary: "))
    gross_monthly_salary = (Annual_salary / 12)
    print('gross monthly salary', gross_monthly_salary)
    tax_per_month = (gross_monthly_salary * income_tax)
    print('tax_per_month: ', tax_per_month)
    net_monthly_salary = (gross_monthly_salary - tax_per_month)
    print('monthly salary: ', net_monthly_salary)

elif contract_type == "casual":
    income_tax1 = 0.250 #29.5% income tax
    Annual_salary = int(input("Please enter your annual salary: "))
    gross_monthly_salary = (Annual_salary / 12)
    print('gross monthly salary', gross_monthly_salary)
    tax_per_month = (gross_monthly_salary * income_tax1)
    print('tax_per_month: ', tax_per_month)
    net_monthly_salary = (gross_monthly_salary - tax_per_month)
    print('monthly salary: ', net_monthly_salary)



