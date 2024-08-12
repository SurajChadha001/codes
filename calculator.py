def calculate_meal_price(cost, tax_rate, tip_percentage):
    tax = cost * tax_rate
    tip = cost * tip_percentage
    total_cost = cost + tax + tip
    return total_cost
meal_cost = 50.00
tax_rate = 0.08
tip_percentage = 0.15
total_cost = calculate_meal_price(meal_cost, tax_rate, tip_percentage)

print("The total cost of meal including tax and tip is $", total_cost)
