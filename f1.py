def roi_calculator(cost,annual_rent,years,appreciation):
    rent_profit = annual_rent * years
    value_profit = cost*(appreciation/100)
    total_profit = rent_profit + value_profit
    roi = (total_profit/cost)*100
    return roi

# Example usage
cost = float(input("enter property cost:"))
annual_rent = float(input("enter annual rent:"))
years = int(input("enter number of years:"))
appreciation = float(input(:"expected price increase %:"))

roi = roi_calculator(cost, annual_rent, years, appreciation)
print(f"your total roi over{years} years is {roi:2f}%")