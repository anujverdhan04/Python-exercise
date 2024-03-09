import random

def get_user_choice():
    valid_choices = {'1', '2', '3'}
    print("Choose:\n 1.For Rock\n 2.For Paper\n 3.For Scissors")
    while True:
        user_input = input("Enter your choice (1/2/3): ")
        if user_input in valid_choices :
            return int(user_input)
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
