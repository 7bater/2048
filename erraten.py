import random

def guess_the_number():
    print("Willkommen zum Zahlenratespiel!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Rate eine Zahl zwischen 1 und 100: "))
            attempts += 1
            if guess < number:
                print("Zu niedrig!")
            elif guess > number:
                print("Zu hoch!")
            else:
                print(f"Richtig! Du hast die Zahl in {attempts} Versuchen erraten.")
                break
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

if __name__ == "__main__":
    guess_the_number()