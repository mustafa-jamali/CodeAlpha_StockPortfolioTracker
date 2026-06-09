# Step 1: Stocks aur unki prices ki dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "AMZN": 175,
    "GOOG": 150
}

# User ke portfolio ko store karne ke liye empty dictionary
user_portfolio = {}

print("--- Welcome to  Stock Portfolio Tracker  ---")

# Step 2: User se stocks aur unki quantity ka input lena
while True:
    print("\nAvailable Stocks:", list(stock_prices.keys()))
    stock_name = input("Write your stock name (or 'exit' for end the program): ").upper()
    
    if stock_name == 'EXIT':
        break
        
    # Check karna ke stock hamari list mein hai ya nahi
    if stock_name in stock_prices:
        try:
            quantity = int(input(f"how many {stock_name} you have? "))
            if quantity <= 0:
                print("Quantity  must be greater than 0!")
                continue
            
            # Portfolio mein add ya update karna
            if stock_name in user_portfolio:
                user_portfolio[stock_name] += quantity
            else:
                user_portfolio[stock_name] = quantity
                
            print(f"{stock_name} ({quantity} shares) added to your portfolio.")
        except ValueError:
            print("wrong input! Please number (integer) .")
    else:
        print("Sorry! this is not available in the list. try again.")

# Step 3: Total Investment calculate aur display karna
print("\n" + "="*35)
print("       YOUR STOCK PORTFOLIO       ")
print("="*35)

total_portfolio_value = 0

# Portfolio ka data check karna
for stock, quantity in user_portfolio.items():
    price = stock_prices[stock]
    current_value = quantity * price
    total_portfolio_value += current_value
    
    print(f"- {stock}: {quantity} Shares x ${price} = ${current_value}")

print("-" * 35)
print(f"Total Investment Value: ${total_portfolio_value}")
print("="*35)


# Step 4: Data ko text file mein save karna
filename = "portfolio_summary.txt"

try:
    with open(filename, "w") as file:
        file.write("=====================================\n")
        file.write("       STOCK PORTFOLIO SUMMARY       \n")
        file.write("=====================================\n")
        
        for stock, quantity in user_portfolio.items():
            price = stock_prices[stock]
            current_value = quantity * price
            file.write(f"- {stock}: {quantity} Shares x ${price} = ${current_value}\n")
            
        file.write("-------------------------------------\n")
        file.write(f"Total Investment Value: ${total_portfolio_value}\n")
        file.write("=====================================\n")
        
    print(f"\n[Mubarak Ho!] your portfolia  '{filename}'  save in the file.")

except Exception as e:
    print(f"having issue in file saving?: {e}")