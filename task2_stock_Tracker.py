"""
CodeAlpha Internship - Python Programming
TASK 2: Stock Portfolio Tracker

"""

import csv

# ============================================================
# STOCK PRICE DICTIONARY
# ============================================================

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 185
}


# ============================================================
# GET VALID QUANTITY
# ============================================================

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                return quantity
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a whole number.")


# ============================================================
# SAVE PORTFOLIO TO TXT
# ============================================================

def save_summary_txt(portfolio, total):
    filename = "portfolio_summary.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("CODEALPHA STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 45 + "\n\n")
        for stock, quantity, price, value in portfolio:
            file.write(f"Stock: {stock}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Price: ${price:.2f}\n")
            file.write(f"Investment: ${value:.2f}\n")
            file.write("-" * 45 + "\n")
        file.write(f"\nTotal investment: ${total:.2f}\n")
    print(f"\n Portfolio saved to '{filename}'.")


# ============================================================
# SAVE PORTFOLIO TO CSV (Second OPTION the user can choose)
# ============================================================

def save_summary_csv(portfolio, total):
    filename = "portfolio_summary.csv"
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Investment"])
        for stock, quantity, price, value in portfolio:
            writer.writerow([stock, quantity, f"${price:.2f}", f"${value:.2f}"])
        writer.writerow(["TOTAL", "", "", f"${total:.2f}"])
    print(f"\n Portfolio saved to '{filename}'.")


# ============================================================
# MAIN STOCK TRACKER Program
# ============================================================

def run_tracker():
    portfolio = []
    total_investment = 0

    print("=" * 55)
    print("CODEALPHA - STOCK PORTFOLIO TRACKER")
    print("=" * 55)

    print("\nHard-coded stock prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"{stock}: ${price:.2f}")

    print("\nEnter DONE when you have finished.")

    while True:
        stock = input("\nEnter stock name: ").strip().upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("Stock not found in the hard-coded stock price dictionary.")
            continue

        quantity = get_quantity()
        price = STOCK_PRICES[stock]
        investment = price * quantity
        portfolio.append((stock, quantity, price, investment))
        total_investment += investment

        print(f"Added {quantity} shares of {stock}.")
        print(f"Investment: ${investment:.2f}")

    if not portfolio:
        print("\nNo stocks were entered. Program finished.")
        return

    print("\n" + "=" * 65)
    print("PORTFOLIO SUMMARY")
    print("=" * 65)

    for stock, quantity, price, value in portfolio:
        print(f"{stock}: {quantity} shares × ${price:.2f} = ${value:.2f}")
    print("-" * 65)
    print(f"TOTAL INVESTMENT: ${total_investment:.2f}")
    print("=" * 65)

    # --------------------------------------------------------
    # OPTIONAL FILE OUTPUT for the user (TXT and/or CSV)
    # --------------------------------------------------------
    choice = input("\nSave the result to a file? (yes/no): ").strip().lower()
    if choice in ["yes", "y"]:
        print("\nChoose format:")
        print("  1. TXT")
        print("  2. CSV")
        fmt = input("Enter 1 or 2: ").strip()
        if fmt == "1":
            save_summary_txt(portfolio, total_investment)
        elif fmt == "2":
            save_summary_csv(portfolio, total_investment)
        else:
            print("Invalid choice. Portfolio not saved.")
    else:
        print("\nPortfolio was not saved.")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    run_tracker()