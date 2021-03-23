income = int(input())
percent = 0
if 15528 <= income <= 42707:
    percent = 15
if 42708 <= income <= 132406:
    percent = 25
if income >= 132407:
    percent = 28
calculated_tax = income / 100 * percent
print("The tax for {income} is {percent}%. That is {calculated_tax} dollars!".format(
    income=income,
    percent=percent,
    calculated_tax=round(calculated_tax)
))
