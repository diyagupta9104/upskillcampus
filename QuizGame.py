import json

def load_questions(filename):
    with open(filename, "r") as file:
        return json.load(file)

def quiz_game():
    questions = load_questions("quiz_data.json")
    score = 0

    for idx, q in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was {q['answer']}.")

    print(f"\nQuiz finished! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    quiz_game()
