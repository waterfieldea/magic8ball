import random

class EightBall:
	yesNoResponses = ["No", "yes", "Maybe", "idk go ask you mother "]
	whenResponses = ["Now", "yesterday", "In exactly 12 minutes", "tomorrow", "never"]
	allResponses = yesNoResponses + whenResponses


	def ask_question(self):
		question = input("Ask me a question ").lower().split(" ")
		first_word = question[0]
		if first_word == "should" or first_word == "can" or first_word == "will" or first_word == "what":
			print(random.choice(self.yesNoResponses))
	
		elif first_word == "when":
			print(random.choice(self.whenResponses))
		else:
			print(random.choice(self.allResponses))
	
		
if __name__ == "__main__":
	eightball = EightBall()
	eightball.ask_question()