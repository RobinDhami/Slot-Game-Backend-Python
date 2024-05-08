MAX_LINES = 3

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
    bet = input("Enter the bet you want to place ")
def main():
    deposit_amount = deposit()
    num_lines = get_lines()
    print(f"Deposit amount: ${deposit_amount}")
    print(f"Number of lines: {num_lines}")

main()
