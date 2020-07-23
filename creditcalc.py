from math import log, ceil, floor
from sys import argv
interest = None
monthly_payment = None
principal_credit = None
periods = None
calc_type = None

def error_exit():
    print("Incorrect parameters")
    exit()

for arg in argv[1:]:
    if arg.startswith("--type"):
        calc_type = arg[7:]
        if calc_type != "annuity" and calc_type != "diff":
            error_exit()
    elif arg.startswith("--payment"):
        try:
            monthly_payment = int(arg[10:])
        except ValueError:
            error_exit()
    elif arg.startswith("--principal"):
        try:
            principal_credit = int(arg[12:])
        except ValueError:
            error_exit()
    elif arg.startswith("--periods"):
        try:
            periods = int(arg[10:])
        except ValueError:
            error_exit()
    elif arg.startswith("--interest"):
        try:
            interest = float(arg[11:])
        except ValueError:
            error_exit()
arguments = [calc_type, monthly_payment, principal_credit, periods, interest]

# checks for correct arguments:
if calc_type == "diff" and monthly_payment is not None:  # to do: apply none to optional variables
    error_exit()
if interest is None or calc_type is None:
    error_exit()
else:
    i = interest / 1200
argu_count = 5
for argu in arguments:
    if argu is None:
        argu_count -=1
    elif (type(argu) is int or type(argu) is float) and argu < 0:
        error_exit()
if argu_count < 4:
    error_exit()

if calc_type == "diff":
    total = 0
    for period in range(periods):
        period += 1
        print(period, i, periods, principal_credit)
        differenciated_payment = ceil(principal_credit / periods + i * (principal_credit - (principal_credit * (period - 1)) / periods))
        print(f"Month {period}: paid out", differenciated_payment)
        total += differenciated_payment
    print("\nOverpayment =", total - principal_credit)

elif calc_type == "annuity":
    if principal_credit is None:
        principal_credit = monthly_payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
        overpayment = ceil(monthly_payment * periods - principal_credit)
        print(f"Your credit principal = {floor(principal_credit)}!")
        print("Overpayment =", overpayment)
    elif periods is None:
        plural = "s"
        ifyears = ""
        ifmonth = ""
        months = log(monthly_payment / (monthly_payment - i * principal_credit), 1 + i)
        if months % 1 != 0:
            months = int(months) + 1
        periods = months
        if months < 12:
            years = ""
            if months == 1:
                plural = ""
            ifmonth = " month" + plural
        elif months == 12:
            ifyears = " year "
            years = 1
            months = ""
        elif months % 12 == 0:
            ifyears = " years"
            years = months // 12
            months = ""
        else:
            ifyears = " years and "
            years = int(months // 12)
            months = months % 12
            if months % 1 != 0:
                months = int(months) + 1
            if months == 1:
                plural = ""
            ifmonth = " month" + plural

        print(f"You need {years}{ifyears}{months}{ifmonth} to repay this credit!")
        overpayment = periods * monthly_payment - principal_credit
        print(f"Overpayment = {overpayment}")
    elif monthly_payment is None:
        monthly_payment = ceil(principal_credit * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
        print("Your monthly payment is", monthly_payment)
        print("Overpayment =", monthly_payment * periods - principal_credit)