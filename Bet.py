import random

symbols = ["🍓", "🍒", "🍉", "🍊", "🌸"]

def spin_row():
    """Returnează un rând de 3 simboluri alese random"""
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    """Afișează un rând de simboluri"""
    print(" | ".join(row))

def payout(row, bet):
    """Calculează câștigul pe baza simbolurilor"""
    if row.count(row[0]) == 3:  # toate 3 la fel
        return bet * 5
    elif row.count(row[0]) == 2 or row.count(row[1]) == 2:  # două la fel
        return bet * 2
    return -5

def main():
    varsta = int(input("Your age: "))
    if varsta < 18:
        print("❌ You don't have access!")
        return
    else:
        print("✅ OK, you can play!\n")

    balance = 100
    print("🎰 Welcome to Slot Machine game! 🎰")
    print("Symbols: 🍓 🍒 🍉 🍊 🌸")

    while balance > 0:
        print(f"\n💰 Current balance: ${balance}")

        bet_str = input("Bet amount: ")

        if not bet_str.isdigit():
            print("❌ Enter a valid number!")
            continue

        bet = int(bet_str)

        if bet > balance:
            print("❌ Insufficient funds")
            continue
        elif bet <= 0:
            print("❌ You must bet greater than 0")
            continue

        # rulează spin
        row = spin_row()
        print_row(row)

        winnings = payout(row, bet)
        if winnings > 0:
            print(f"🎉 You won ${winnings}!")
        else:
            print("😢 No win this time.")

        balance -= bet
        balance += winnings

    print("\nGame Over! Balance = $0")

if __name__ == "__main__":
    main()
