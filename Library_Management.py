import random
print("--------------------------**********--------------------------")
print("Library Management System")
print("--------------------------**********--------------------------")


class entity:
    def user_type(self):
        print("Select your identity \n Options are \n 1: Student \n 2: Adminstration ")
        identity = int(input("Enter the number of your identity "))
        if (identity == 1):
           print("**Student**")
           print("-----------------------------------------------------------")
           computer_id = random.randint(0, 999)
           print("Computer generated ID =", computer_id)
           user_generated_id = input("Enter your ID: ")

           if int(user_generated_id) == computer_id:
               print("Authorized")
           else:
              print("Unauthorized")
              return False   
        
           print("Please enter your name")
           name= str(input())
           print("Enter your Department")
           dept= str(input())
           print("-----------------------------------------------------------")
        else:
           print("**Adminstration**")
           print("-----------------------------------------------------------")
           computer_id = random.randint(0, 999)
           print("Computer generated ID =", computer_id)
           user_generated_id = input("Enter your ID: ")

           if int(user_generated_id) == computer_id:
                print("Authorized")
           else:
                print("Unauthorized")
                return False
           print("Enter your Department")
           dept = str(input())  
           print("-----------------------------------------------------------")
        
   
    def books(self):   
        print("Select Department for selecting books")
        print("1. CS")
        print("2. Mathematics")
        print("3. Physics")

        selection = input("Enter the number corresponding to the department: ")

        Dept ={

            "CS":[
                "Python Programming for Everybody",
                "Data Structures and Algorithms in Python",
                "Introduction to Computer Science and Programming"
              ],
            "Mathematics":[
                "Calculus",
                "Linear Algebra and Differential",
                "Equations",
                "Discrete Mathmatical Structures",
                "Applications & Problems"
                        ],
            "Physics":[
                "Physics of Fluids",
                "Classical Mechanics",
                "Electricity and Magnetism",
                "Thermodynamics"
                   ],
        }
        if selection in Dept:
            selected_department = Dept[selection]
            print(f"Books in the {selection} department:")
            for book in selected_department:
                print("- " + book)
        else:
            print("Invalid selection. Please choose a valid department.")
 
  

           
   

run = entity()
run.user_type()
run.books()


