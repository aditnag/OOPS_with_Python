# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

sal, yr = list(map(int, input("Enter sal and yr: ").strip().split()))[:2]
if yr > 5:
    print(f"Bonus = {1.05 * sal}")
else:
    print(f"Bonus = {sal}")


