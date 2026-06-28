""""
Project Name : Python Escape Room
Description  : Crack puzzles, unlock doors, ans escape using Python logic
Author       : Trishitha
"""

import random
max_lives=3 #life of player
def intro():
    print("Welcome to the python escape room")
    print("Solve the challenges using logic to escape")
def door_one_math_puzzle():
    answer = int(input("Door 1: what is 7 * 6 + 8"))
    return True if answer == 50 else False
def door_two_pattern_puzzle(attempts = 2):
    secret = "mystery"
    tries = 0
    while tries<attempts:
        guess = input("Door 2: guess the secret word ").lower()
        if guess == "":
            continue
        if guess == secret:
            return True
        tries += 1
        print("Wrong Answer")
    return False

#door 3
def door_three_code(start = 1, end = 5):
    lucky = random.randint(start, end)
    for i in range(2):
        guess = int(input("Door 3: Guess the luck number (1-5):"))
        if guess == lucky:
            return True
        return False
def reward_badge(*badges):
    """Variable length arguments"""
    return random.choice(badges)
def escape_room():
    """main game engine (infinite loop)"""
    lives = max_lives
    collected_badges = set()
    while True:
        print("\nChoose a door:")
        print("1. Math Door")
        print("2. Pattern Door")
        print("3. Lucky Door")
        print("4. Exit Game")

        choice = input("Your choice: ")

        if choice == "1":
            if door_one_math_puzzle():
                collected_badges.add(reward_badge("Logic Master","Math Whiz"))
                print("Door unlocked!")
            else:
                lives -= 1
        elif choice == "2":
            if door_two_pattern_puzzle():
                collected_badges.add(reward_badge("Pattern Pro", "Code Breaker"))
                print("Door unlocked")
            else:
                lives -=1
        elif choice == "3":
            if door_three_code():
                collected_badges.add(reward_badge("Lucky Star", "Risk Taker"))
                print("Door unlocked!")
            else:
                lives -= 1
        elif choice == "4":
            break

        else:
            print("Invalid door!")
        print(f"Lives left: {lives}")
        print(f"Badges collected: {collected_badges}")
        if lives == 0:
            print("Game Over!")
            break
    print(" Escape Room Ended. Thanks for playing!")
def main():
    intro()
escape_room()


#%%
