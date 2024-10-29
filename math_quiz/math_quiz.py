import random


# Function to generate a random number
def RandomNumberGen(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

# Function to generate a random operation
def OperationGen():
    return random.choice(['+', '-', '*'])

# Function to generate a math problem
def ProblemGen(num1, num2, operation):
    problem = f"{num1} {operation} {num2}"
    if operation == '+': answer = num1 + num2
    elif operation == '-': answer = num1 - num2
    else: answer = num1 * num2
    return problem, answer


# Main function of the quiz
def math_quiz():

    # Initialize variables: score and total questions
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the total number of questions and ask the user to solve the math problems
    for _ in range(total_questions):

        # Generate random numbers and operation using the helper functions
        num1 = RandomNumberGen(1, 10); 
        num2 = RandomNumberGen(1, 6); 
        operation = OperationGen()

        # Generate the math problem and the real answer
        PROBLEM, ANSWER = ProblemGen(num1, num2, operation)
        print(f"\nQuestion: {PROBLEM}")

        # Ask the user for the answer and validate the input with a try-except 
        while True:
            try:
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Check if the user's answer is correct and provide feedback        
        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
            
    # Print the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

# Run the math quiz game
if __name__ == "__main__":
    math_quiz()
