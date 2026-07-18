print("Welcome to Quiz Game!")
score = 0

answer = input("1. What is the capital of India? ")

if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. Who developed Python? ")

if answer.lower() == "guido van rossum":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. What is 5 + 5? ")

if answer == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuiz Finished!")
print("Your Score:", score, "/ 3")


