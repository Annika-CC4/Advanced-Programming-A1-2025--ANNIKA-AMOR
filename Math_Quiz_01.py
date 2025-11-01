#!!used windows powershell to run code

#import a function that generates random given selection 
import random

#prints 3 difficulty levels.
def Option():
   print ('Select difficulty level: \n1. Easy \n2. Medium \n3.Hard ')
   while True:
        Selection = input("Enter the letter of your chosen difficulty:")
        if Selection in ['1', '2', '3']:#checks if input matches the selection
            return int(Selection)
        print("Invalid choice. Try again.")


def randomInt(difficulty): #!!I got the syntax with the help of ChatGPT!!
    if difficulty == 1:
        return random.randint(0, 9)#ramdon is the imported syntax, randit is inside the random module and generates random integers between a and b variable/placeholder. # This code generates two random numbers for an operation between 1-9 
    elif difficulty == 2:
        return random.randint(10, 99)#generates two random numbers for an operation between 10-99 
    else:
        return random.randint(1000, 9999)#generates two random numbers for an operation between 1000-9999 


def operation():#defined a function that decides what operator to use; addition or subtraction
    return random.choice(['+', '-'])


def question(a, b, op):#function that makes the question
    while True:
        try:
            ans = int(input(f"{a} {op} {b} = "))#a= first number, op=operation, b=secodn number
            return ans
        except ValueError:#checks if th einput is an integer; if not it will print--
            print("Please enter a valid integer.")


def checker(a, b, op, answer):#function that checks if an answer is correct
    true = a + b if op == '+' else a - b
    return answer == true, true 


def final_points(points): #function that displays your rank on the end of the quiz
    print(f"\nYour final score is {points}/100")
    if points >= 90: #if you got greater than 90 points
        print("Rank: A+")# you get A+
    elif points >= 75:#if you got greater than 90 points
        print("Rank: A")#you get A
    elif points >= 50:#if you got greater than 90 points
        print("Rank: B")#you get B
    else:# if you get less than 50
        print("Rank: C")#you get C


def quiz():#after defining each parts of the quiz, time to combine all of them and create a flow
    while True:#while loop to create replayable rounds when the user still wants to play
        points = 0 #set points to 0
        difficulty = Option() #calls the function OPtion()
        for i in range(10): #for loop that generates 10 questions, one at a time
            a = randomInt(difficulty)
            b = randomInt(difficulty)
            op = operation()# generates random numbers in a and b container and operator.
            
            answer = question(a, b, op)#first try
            correct, true = checker(a, b, op, answer)#question() function is inside answer variable to make a syntax
            if correct:
                print("Correct! +10 points")
                points += 10 #if correct, 10 will be added in points variable.
            else:
                print("Incorrect. Try once more.")# if incorrect, no points will be added and proceed to give a SECOND CHANCE
               

                answer = question(a, b, op)#second try for the same number
                correct, true = checker(a, b, op, answer)
                if correct:
                    print("Correct! +5 points") #if correct, 5 will be added in points variable.
                    points += 5
                else:
                    print(f"Wrong again. The correct answer was {true}.")#if still incorrect, no points will be added and proceed to go to the NEXT QUESTION
        
        final_points(points)
        
        # Play again?
        replay = input("\nDo you want to play again?: 'y' for yes: ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

# Start the quiz
if __name__ == "__main__":
    quiz()
