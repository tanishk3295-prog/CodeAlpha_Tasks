# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 170
}

total_investment = 0

# Number of stocks user wants to enter
n = int(input("How many different stocks do you own? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"{stock_name} = ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("Result saved in portfolio.txt")