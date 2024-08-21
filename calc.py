#declare temperature
# temp = int(input("What is your current temperature? "))
# if temp > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temp > 20:
#     print("It's a nice day.")
# elif temp > 10:
#     print("It's a bit cold.")
# else:
#     print("Keep warm.")


#weight calculator
#this program asks you to input your weight and converts it to either kilograms or pounds
weight = int(input("What is your weight:? "))
unit = input("Is this in (K)g or (L)bs? ")
if unit.upper() == "K":
    converted_weight = weight / 0.45
    print(f"Weight in Lbs:", {converted_weight})
else:
    converted_weight = weight * 0.45
    print(f"Weight in Kgs:", {converted_weight})