print("Kaun Banega Lakhpati")
print("Are you ready to play the game")

def kbc():
    a = "Game over"
    price= 0
    amount=0
    choice = input("Enter your choice YES/NO: ")
    
    if "YES" in choice:
        print("Let's Play")
        
        # Question 1
        print("Question 1 is on your terminal")
        print("Question 1: What is the capital of India?")
        print("Options: \n A. Berlin \n B. Uttarakhand \n C. Delhi \n D. Mumbai")
        
        answer1 = input("Tell me your choice (A, B, C, D): ").upper()
        
        if answer1 == "C":
            print("Right Answer!")
            print("You won 100")
            amount=price+100
            print("Total amount you won ",amount)
        else:
            print("Oops, you lose!")
            print(a)
            return

        # Question 2
        print("Question 2 is on your terminal")
        print("Question 2: Which programming language is this code written in?")
        print("Options: \n A. Python \n B. Java \n C. C++ \n D. JavaScript")
        
        answer2 = input("Tell me your choice (A, B, C, D): ").upper()
        
        if answer2 == "A":
            print("Right Answer!")
            print("You won 100")
            amount=amount+100
            print("Total amount you won ",amount) 
        else:
            print("Oops, you lose!")
            print(a)
            return

        # Question 3
        print("Question 3 is on your terminal")
        print("Question 3: What is the largest planet in our solar system?")
        print("Options: \n A. Earth \n B. Jupiter \n C. Mars \n D. Venus")
        
        answer3 = input("Tell me your choice (A, B, C, D): ").upper()
        
        if answer3 == "B":
            print("Right Answer!")
            print("You won 100")
            amount=amount+100
            print("Total amount you won ",amount)
        else:
            print("Oops, you lose!")
            print(a)
            return

    elif "NO" in choice:
        print("Thank you")
        print("Game over")

kbc()



