# Question 1:
question_1 = ("What is the capital of France?", "a) Paris", "b) Rome", "c) Berlin")
correct_answer_1 = "a"

print("\n".join(question_1))
answer_q1 = input("Your answer: ")

if answer_q1.lower() == correct_answer_1:
    print("Correct! Paris is the capital of France.")
else:
    if answer_q1.lower() == "b":
        print("Incorrect. Rome is not the capital of France.")
    elif answer_q1.lower() == "c":
        print("Incorrect. Berlin is not the capital of France.")
    else:
        print(f"Invalid input. Please choose {correct_answer_1}) Paris, b) Rome, or c) Berlin.")

# Question 2:
question_2 = ("Which programming language is known for its readability and simplicity?",
               "a) Java", "b) Python", "c) C++")
correct_answer_2 = "b"

print("\n".join(question_2))
answer_q2 = input("Your answer: ")

if answer_q2.lower() == correct_answer_2:
    print("Correct! Python is known for its readability and simplicity.")
else:
    if answer_q2.lower() == "a":
        print("Incorrect. Java is not the language known for its readability and simplicity.")
    elif answer_q2.lower() == "c":
        print("Incorrect. C++ is not the language known for its readability and simplicity.")
    else:
        print(f"Invalid input. Please choose {correct_answer_2}) Python, a) Java, or c) C++.")

# Question 3:
question_3 = ("What is the result of 2 + 3 * 4?", "a) 20", "b) 14", "c) 18")
correct_answer_3 = "b"

print("\n".join(question_3))
answer_q3 = input("Your answer: ")

if answer_q3.lower() == correct_answer_3:
    print("Correct! The result of 2 + 3 * 4 is 14.")
else:
    if answer_q3.lower() == "a":
        print("Incorrect. The result of 2 + 3 * 4 is not 20.")
    elif answer_q3.lower() == "c":
        print("Incorrect. The result of 2 + 3 * 4 is not 18.")
    else:
        print(f"Invalid input. Please choose {correct_answer_3}) 14, a) 20, or c) 18.")