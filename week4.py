import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def display_question(self):
        question = self.questions[self.current_question_index]
        print(question.text)
        for option in question.options:
            print(option)

    def get_player_response(self):
        response = input("Enter your choice (A/B/C/D): ").upper()
        return response

    def evaluate_response(self, response):
        question = self.questions[self.current_question_index]
        if response == question.correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        self.current_question_index += 1

    def display_score(self):
        print("Your current score is:", self.score)


class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer


class Player:
    def __init__(self, name):
        self.name = name


def main():
    # Example questions
    questions = [
        Question("What is the capital of France?", ["A. London", "B. Paris", "C. Rome", "D. Berlin"], "B"),
        Question("Who wrote 'Romeo and Juliet'?", ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"], "A"),
        # Add more questions as needed
    ]

    # Shuffle the questions
    random.shuffle(questions)

    quiz = Quiz(questions)

    print("Welcome to the Online Quiz Game!")

    player_name = input("Enter your name: ")
    player = Player(player_name)

    print(f"Hello {player.name}! Let's start the quiz.")

    conduct_quiz(quiz)

    print("Quiz ended. Here are your final results:")
    quiz.display_score()


def conduct_quiz(quiz):
    while quiz.current_question_index < len(quiz.questions):
        quiz.display_question()
        response = quiz.get_player_response()
        quiz.evaluate_response(response)
        quiz.display_score()


if __name__ == "__main__":
    main()
