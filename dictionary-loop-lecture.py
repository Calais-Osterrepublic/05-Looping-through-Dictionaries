from quiz_data import example, questions

print("=== WHILE LOOP VERSION (the real solution) ===")
print()

i = 0
score = 0

while i < len(questions):
    current = questions[i]          # current is ONE dictionary

    print(current["question"])
    print("a)", current["a"])
    print("b)", current["b"])
    print("c)", current["c"])

    player_answer = input("Your answer (a/b/c): ")

    if player_answer in ("a", "b", "c"):          # is it even a real choice?
        if player_answer == current["answer"]:
            print("Correct!")
            score = score + 1
        else:
            print("Nope. The correct answer was", current["answer"])
    else:
        print("That's not a valid choice -- pick a, b, or c.")

    print()

    i = i + 1            # if we forget this line, the loop never ends

print("While loop score:", score, "out of", len(questions))
print()
