
questions = [
	"I feel that I am a person of worth, at least on an equal plane with others.",
	"I feel that I have a number of good qualities.",
	"All in all, I am inclined to feel that I am a failure.",
	"I am able to do things as well as most other people.",
	"I feel I do not have much to be proud of.",
	"I take a positive attitude toward myself.",
	"On the whole, I am satisfied with myself.",
	"I wish I could have more respect for myself.",
	"I certainly feel useless at times.",
	"At times I think I am no good at all.",
]
reversed_questions = [2, 4, 7, 8, 9]
possible_answers = ["D", "d", "a", "A"]

def quiz(i):
	print(f"{i+1}. {questions[i]}")
	answer = input("   Enter D, d, a, or A: ")
	while not answer in possible_answers:
		print("Invalid answer. Try again.")
		answer = input("Enter D, d, a, or A: ")
	answer_num = possible_answers.index(answer)
	if i in reversed_questions:
		answer_num = 3 - answer_num
	return answer_num

def main():
	print("This program is an implementation of the Rosenberg\nSelf-Esteem Scale. This program will show you ten\nstatements that you could possibly apply to yourself.\nPlease rate how much you agree with each of the\nstatements by responding with one of these four letters:")
	print("D: Strongly Disagree\nd: Disgree\na: Agree\nA: Strongly Agree")
	score = 0
	for i in range(len(questions)):
		score += quiz(i)
	print(f"Your score: {score}")
	print("Get a score below 15 and you should call this number: +1 208-356-7070")

main()
