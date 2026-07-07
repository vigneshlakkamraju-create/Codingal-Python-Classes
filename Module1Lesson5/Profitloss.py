#Write to check if a person is buying oranges at 100 rs and later seeing it at 120 rs. Find that he has profit or loss?
actual_cost = float(input(" Please Enter the actual product price: "))
sale_amount = float(input(" Please enter the sales amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit")
          