# Piccolo: simple programme to make Grande Omega exercises of Hogeschool Rotterdam
# This second version (v2) contains only mmultiple choice question, and gives already more feedback on wrong answers than Grande Omega.
# The questions, answers and feeback will be read frrom file in case an argument is provided.
# Copyleft 2021: Jan Kroon, Hogeschool Rotterdam

# Questions and Answers

quiz = [
    {"question": "Who created the Python programming language?",
     "options": {"A": "Steve Jobs", "B": "John Cleese", "C": "Guido van Rossum", "D": "Salazar Slytherin"},
     "feedback": {"A": "Steve Jobs was one of the founders op Apple Computer.",
                  "B": "John Cleese is a comedian, one of the founders of Monty Python.",
                  "C": "Correct answer!",
                  "D": "Salazar Slytherin is the founder of one of the houses in Hogwarts school of witchcraft and wizardry."
                 }
     },
    {"question": "What is the main advantage of software development in Python?", 
     "options": {"A": "Quick programming", "B": "Quick execution", "C": "Type safety", "D": "Downward compatability"},
     "feedback": {"A": "Steve Jobs was one of the founders op Apple Computer.",
                  "B": "John Cleese is a comedian, one of the founders of Monty Python.",
                  "C": "Correct answer!",
                  "D": "Salazar Slytherin is the founder of one of the houses in Hogwarts school of witchcraft and wizardry."
                  }
    }
]

# Run quiz

# Check if an external file with questions, answers and feedback is provided. If so, use that information.


index = 0
while True:
   print(quiz[index]["question"])
   for option in ["A", "B", "C", "D"]:
      print(option, quiz[index]["options"][option])
   answer = input('Answer: ')
   print(quiz[index]["feedback"][answer])
   index += 1
