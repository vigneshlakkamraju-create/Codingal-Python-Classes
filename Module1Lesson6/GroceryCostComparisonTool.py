# Grocery Cost Comparison Tool
 
# ---------------------------------
# PART 1: Calculate a Grocery Basket
# ---------------------------------
 
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4
 
# Parentheses are calculated first
basket_cost_per_person = (
    (rice_price + milk_price + fruit_price)
    * number_of_baskets
    / family_members
)
 
print("Grocery basket cost per person:", basket_cost_per_person)
 
 
# ---------------------------------
# PART 2: Check Equal Distribution
# ---------------------------------
 
total_items = int(
    input("\nEnter the total number of grocery items: ")
)
 
people = int(
    input("Enter the number of family members: ")
)
 
# Use the modulus operator to check divisibility
if total_items % people == 0:
    print(
        total_items,
        "items can be divided equally among",
        people,
        "people."
    )
else:
    print(
        total_items,
        "items cannot be divided equally among",
        people,
        "people."
    )
 
 
# ---------------------------------
# PART 3: Correct a Grocery Average
# ---------------------------------
 
recorded_average = 65
wrong_week_cost = 50
correct_week_cost = 80
total_weeks = 4
 
# Find the total using the recorded average
recorded_total = recorded_average * total_weeks
 
print("\nRecorded grocery total:", recorded_total)
 
# Replace the incorrect weekly cost
corrected_total = (
    recorded_total
    - wrong_week_cost
    + correct_week_cost
)
 
print("Corrected grocery total:", corrected_total)
 
# Calculate the corrected weekly average
corrected_average = corrected_total / total_weeks
 
print("Corrected weekly average:", corrected_average)
 
 
# ---------------------------------
# PART 4: Compare Three Store Prices
# ---------------------------------
 
store_a_average = 70
store_b_average = 75
store_c_average = 80
 
print("\nStore A average:", store_a_average)
print("Store B average:", store_b_average)
print("Store C average:", store_c_average)
 
# Compare the corrected average with three values
if (
    corrected_average < store_a_average
    and corrected_average < store_b_average
    and corrected_average < store_c_average
):
    print(
        "Your corrected grocery average is lower "
        "than all three store averages."
    )
 
elif (
    corrected_average > store_a_average
    and corrected_average > store_b_average
    and corrected_average > store_c_average
):
    print(
        "Your corrected grocery average is higher "
        "than all three store averages."
    )
 
else:
    print(
        "Your corrected grocery average is between "
        "the three store averages."
    )
