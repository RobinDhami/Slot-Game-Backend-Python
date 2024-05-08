MAX_LINES = 3
MAX_BET=100
MIN_BET =1 
def deposit():
    while True:
        amount = input("Please enter the amount you wish to deposit: $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Please enter a valid deposit amount (should be greater than 0)")
        else:
            print("The amount should be a whole number.")

def get_lines():
    while True:
        lines = input("Enter the number of lines you want to bet (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Line limit is between 1 and {MAX_LINES}.")
        else:
            print("Please enter a whole number for the lines you want to bet.")

def place_bet():
    amount = input("Enter the bet you want to place ")
    while True:
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f" Enter a bet between {MIN_BET} to {MAX_BET}")
        else:
            print("Enter a valid number ")  
    return amount              
def main():
    deposit_amount = deposit()
    num_lines = get_lines()
    bet=place_bet()
    print(f"Deposit amount: ${deposit_amount}")
    print(f"Number of lines: {num_lines}")
    print(f"Bet Placed : ${bet}")

main()
