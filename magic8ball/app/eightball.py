import random


class EightBall:
    yesNoResponses = ["No", "yes", "Maybe", "idk go ask you mother "]
    whenResponses = ["Now", "yesterday", "In exactly 12 minutes", "tomorrow", "never"]
    allResponses = yesNoResponses + whenResponses

    def ask_question(self, input_question):
        question = input_question.lower().split(" ")
        first_word = question[0]
        if first_word == "should" or first_word == "can" or first_word == "will" or first_word == "what":
            return random.choice(self.yesNoResponses)

        elif first_word == "when":
            return random.choice(self.whenResponses)
        else:
            return random.choice(self.allResponses)


if __name__ == "__main__":
    question = input("Ask me a question ")

    eightball = EightBall()
    answer = eightball.ask_question(question)
    print(answer)
