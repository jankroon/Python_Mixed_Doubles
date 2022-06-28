# Fourth version of Mixed-Doubles software product lesson 1
# Copyleft 2022, Jan Kroon (Rotterdam University of Applied Sciences)

# Results
anna_results = "Anna scored a 5.2 for the theory exam and a 7.5 for the practical assignment."
bert_results = "Bert scored a 8.1 for the theory exam and a 7.5 for the practical assignment."
charley_results = "Charley scored a 3.7 for the theory exam and a 4.5 for the practical assignment."
denise_results = "Denise scored a 7.1 for the theory exam and a 9.2 for the practical assignment."
esther_results = "Esther scored a 8.5 for the theory exam and a 7.2 for the practical assignment."
fritz_results = "Fritz scored a 5.5 for the theory exam and a 5.4 for the practical assignment."
george_results = "George scored a 5.4 for the theory exam and a 5.6 for the practical assignment."

# User Interaction

print("*** OSIRIS ***")

student_name = input("Student naam? ")

if student_name == "Anna":
    print(anna_results)
if student_name == "Bert":
    print(bert_results)
if student_name == "Charley":
    print(charley_results)
if student_name == "Denise":
    print(denise_results)
if student_name == "Esther":
    print(esther_results)
if student_name == "Fritz":
    print(fritz_results)
if student_name == "George":
    print(george_results)
if (student_name != "Anna" and student_name != "Bert" and student_name != "Charley" and 
    student_name != "Denise" and student_name != "Esther" and student_name != "Fritz" and
    student_name != "George"):
    print("Er zijn geen gegevens gevonden van ", student_name)
