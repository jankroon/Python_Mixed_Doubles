# Fifth version of Mixed-Doubles software product lesson 1
# Copyleft 2022, Jan Kroon (Rotterdam University of Applied Sciences)

# Results
anna_results = [5.2, 7.5]
bert_results = [8.1, 7.5]
charley_results = [3.7, 4.5]
denise_results = [7.1, 9.2]
esther_results = [8.5, 7.2]
fritz_results = [5.5, 5.4]
george_results = [5.4, 5.6]

# User Interaction

print("*** OSIRIS ***")

student_name = input("Student naam? ")

if student_name == "Anna":
    print(f"{student_name} heeft een {anna_results[0]} gehaald voor theorie en een {anna_results[1]} voor praktijk.")
    print(f"Gemiddeld komt dit uit op eindcijfer {(anna_results[0] + anna_results[1])/2}.")
if student_name == "Bert":
    print(f"{student_name} heeft een {bert_results[0]} gehaald voor theorie en een {bert_results[1]} voor praktijk.")
    print(f"Gemiddeld komt dit uit op eindcijfer {(bert_results[0] + bert_results[1])/2}.")
if student_name == "Charley":
    print(f"{student_name} heeft een {charley_results[0]} gehaald voor theorie en een {charley_results[1]} voor praktijk.")
    print(f"Gemiddeld komt dit uit op eindcijfer {(charley_results[0] + charley_results[1])/2}.")
if student_name == "Denise":
    print(f"{student_name} heeft een {denise_results[0]} gehaald voor theorie en een {denise_results[1]} voor praktijk.")
    print(f"Gemiddeld komt dit uit op eindcijfer {(denise_results[0] + denise_results[1])/2}.")
if student_name == "Esther":
    print(f"{student_name} heeft een {denise_results[0]} gehaald voor theorie en een {denise_results[1]} voor praktijk.")
    print(f"Gemiddeld komt dit uit op eindcijfer {(esther_results[0] + esther_results[1])/2}.")
if student_name == "Fritz":
    print(f"{student_name} heeft een {fritz_results[0]} gehaald voor theorie en een {fritz_results[1]} voor praktijk.")
    print(f"Gemiddeld komt dit uit op eindcijfer {(fritz_results[0] + fritz_results[1])/2}.")
if student_name == "George":
    print(f"{student_name} heeft een {george_results[0]} gehaald voor theorie en een {george_results[1]} voor praktijk.")
    print(f"Gemiddeld komt dit uit op eindcijfer {(george_results[0] + george_results[1])/2}.")
if (student_name != "Anna" and student_name != "Bert" and student_name != "Charley" and 
    student_name != "Denise" and student_name != "Esther" and student_name != "Fritz" and
    student_name != "George"):
    print("Er zijn geen gegevens gevonden van ", student_name)
