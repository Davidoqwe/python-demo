questions = [
    ["What is the capital of France?", "paris"],
    ["What is 5 + 7?", "12"],
    ["What is the color of the sky?", "blue"]
]

score = 0
for q in questions:
    ans = input(q[0] + " ").lower()
    if ans == q[1]:
        score += 1

print(f"Your score: {score}/{len(questions)}")
