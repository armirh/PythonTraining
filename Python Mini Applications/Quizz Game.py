#function to begin the new game
def new_game():

    #list of guesses
    guesses = [] # a list to store our guesses

    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("-------------------------------")#line breakbetween each question
        print(key)
        for i in options[question_num]:
            print(i)
        #user input
        guess = input("Enter (A,B,C or D): ").upper()
        #compare our guesses to the answer
        guesses.append(guess) #we append our guess to the list of guesses

        #since we return a value, we should assign the point to the variable correct guesses
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)
#-------------------------------
#function to check our answer
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#--------------------------------
#function to display our score
def display_score(correct_guesses,guesses):
    print("-------------------------------")
    print("Results")
    print("-------------------------------")

    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")

#---------------------------------
#def to ask us to play again
def play_again():
    response = input("Do you want to play again? (yes/no): ").upper()
    if response == "YES":
        return True
    else:
        return False

#dictionary would be our best option for the quiz, every key corresponds to a value
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "What is python referred to?: ": "C",
    "Is python useful?:": "D"
}
#a place to hold our answers
options = [["A.Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2002"],
           ["A. Mouse", "B. Lizard", "C. Snake", "D. Elephant"],
           ["A. Yes", "B. No", "C. Yessir", "D. Hell yeah"]]


#call the function
new_game()

#if we want to play again
while play_again():
    new_game()

print("You have a good day!")

