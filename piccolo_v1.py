# Piccolo: simple programme to make Grande Omega exercises of Hogeschool Rotterdam
# This first version (v1) contains only multiple choice question, but gives already more feedback than Grande Omega.
# Copyleft 2020: Jan Kroon, Hogeschool Rotterdam

# Questions and Answers

quiz = [
    {"question": "Who created the Python programming language?",
     "options": {"A": "Steve Jobs", "B": "John Cleese", "C": "Guido van Rossum", "D": "Salazar Slytherin"}},
    {"question": "What is the main advantage of software development in Python?", 
     "options": {"A": "Quick programming", "B": "Quick execution", "C": "Type safety", "D": "Downward compatability"}}
    ]

# Run quiz
index = 0
while True:
   print(quiz[index]["question"])
   for option in ["A", "B", "C", "D"]:
      print(option, quiz[index]["options"][option])
   answer = input('Answer: ')
   index += 1
