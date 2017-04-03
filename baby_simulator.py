from random import choice

questions = ["What is sun yellow ?", "Why is sky blue ?", "Where are all the dinosaurs ?"]

question = choice(questions)

answer = input(question + " ").strip().lower()

while answer != "just because":
    answer = input("But Why ? ").strip().lower()

print("Oh... Okay")