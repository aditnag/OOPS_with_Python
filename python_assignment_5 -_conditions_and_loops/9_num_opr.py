# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quant = int(input())
if quant * 100 > 1000:
    print(f"CP = {0.9 * (quant * 100)}")
else:
    print(f"CP = {quant * 100}")