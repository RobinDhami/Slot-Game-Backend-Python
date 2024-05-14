import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = {
    "A": 2, "B": 3, "C": 4, "D": 5, "E": 6
}

def slot_machine(ROWS, COLS, symbol):
    All_Symbols = []
    for key, value in symbols.items():
        for i in range(value):
            All_Symbols.append(key)
    print(All_Symbols)
    
    columns=[]
    for _ in range(COLS):
        columns=[]
        current_symbols = All_Symbols.copy()
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            columns.append(value)
        columns.append(columns)
    return columns
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
    while True:
        amount = input("Enter the bet you want to place: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Enter a bet between {MIN_BET} to {MAX_BET}")
        else:
            print("Enter a valid number.")

def main():
    balance = deposit()
    lines = get_lines()
    bet = place_bet()
    print(f"Deposit amount: ${balance}")
    print(f"Number of lines: {lines}")
    print(f"Bet Placed: ${bet}")

    while True:
        if bet > balance:
            print(f"You do not have sufficient balance, Your current balance is {balance}")
            bet = place_bet()
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet will be {bet * lines}")

main()
