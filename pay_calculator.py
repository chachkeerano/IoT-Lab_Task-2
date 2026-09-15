# Program to calculate employee pay based on hours worked

hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    total_pay = hours * rate
else:
    overtime_hours = hours - 40
    total_pay = (40 * rate) + (overtime_hours * rate * 1.5)

print("\n----- PAY SUMMARY -----")
print(f"Hours Worked : {hours}")
print(f"Hourly Rate  : {rate}")
print(f"Total Pay    : {total_pay:.2f}")
