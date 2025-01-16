from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str | None:
    question: list[str] = [question for question in questions]
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    if matches:
        return matches[0]

def chat_bot(knowledge: dict):
    while True:
        user_input: str = input("You: ")
        best_match: str = get_best_match(user_input, knowledge)
        if answer := knowledge.get(best_match):
            print(f"Bot: {answer}")
        else:
            print("Bot: I do not understand")

if __name__ == '__main__':
    brain: dict = {"hello": "Hey there",
                   "how are you": "I am good, thanks!",
                   "what time is it": "don't know",
                   "bye": "see you"
                   }
    chat_bot(knowledge=brain)
