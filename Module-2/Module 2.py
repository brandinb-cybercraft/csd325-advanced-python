print("Welcome to Brandi's Fiber Optic Installation Calculator!")

company_name = input("Please enter your company name: ")
feet = float(input("Enter the number of feet of fiber optic cable to be installed: "))


if feet > 500:
    cost_per_foot = 0.50
elif feet > 250:
    cost_per_foot = 0.70
elif feet > 100:
    cost_per_foot = 0.80
else:
    cost_per_foot = 0.87

total_cost = feet * cost_per_foot


print("\nInstallation Summary:")
print("Company Name:", company_name)
print("Feet of fiber to be installed:", feet)
print("Cost per foot: $" + str(cost_per_foot))
print("Total cost: $" + str(round(total_cost, 2)))