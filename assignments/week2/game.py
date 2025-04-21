import time
import sys

def typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)

typing("Welcome to the Study Method Quiz!📚")
time.sleep(1)
typing("What is your name?")
name = input("\nEnter your name: ")
time.sleep(1)
typing("Hello " + str(name) + ", based on questions about your preferred learning style this program will provide you with the best study method for you!")
typing("\nLet's start.🚀\n")
time.sleep(1)

# Initial scores of the study methods
scores = {"Pomodoro": 0,
    "Feynman": 0,
    "Spaced Repetition": 0,
    "Active Recall": 0,
    "Mind Mapping": 0}

# Asking questions to evaluate the perfect study method
print ("\nDo you prefer structure or flexibility in your study sessions?")
print ("1) I prefer structured study routines.")
print ("2) I prefer flexible study sessions.\n")
style = int(input("Choose (1 or 2): "))

if style == "1":
    print ("\n Great! Let's explore some structured study methods.")
    print ("How do you organize your study sessions?")
    print ("1) Timed sessions with breaks.")
    print ("2) Repeated reviews over a certain period of time.\n")
    branching_point = int(input("Choose (1 or 2): "))
    if branching_point == "1":
        scores["Pomodoro"] += 1
    elif branching_point == "2":
        scores["Spaced Repetition"] += 1

elif style == "2":
    print ("\n Great! Let's explore some flexible study sessions.")
    print ("What do you do during your study sessions?")
    print ("1) Draw diagrams or visual overviews.")
    print ("2) Explain concepts out loud to yourself or others.")
    print ("3) Try to recall everything you've studied after a certain period of time.\n")
    branching_point = int(input("Choose (1-3): "))

    if branching_point == "1":
        scores["Mind Mapping"] += 1
    elif branching_point == "2":
        scores["Feynman"] += 1
    elif branching_point == "3":
        scores["Active Recall"] += 1

while True:
    focus_time = int(input("\nHow long can you focus before losing attention?🎧 (Enter a number between 15 and 90 minutes:) "))
    if 15 <= focus_time <= 90:
        break
    else:
        print ("Please enter a number between 15 and 90.\n")

if 15 <= focus_time <= 25:
    scores["Pomodoro"] += 1
    scores["Spaced Repetition"] += 1
elif 26 <= focus_time <= 40:
    scores["Active Recall"] += 1
elif 41 <= focus_time <= 60:
    scores["Mind Mapping"] += 1
elif 61 <= focus_time <= 90:
    scores["Feynman"] += 1


print ("\nHow do you feel after studying for long hours without breaks?📖")
print ("1) I lose focus quickly.")
print ("2) I manage fine, especially if I use visuals.")
print ("3) I prefer to study myself frequently instead.")
print ("4) I'm okay as long as I break it up across days.")
print ("5) I like to use breaks to stop and explain the learned material to myself.\n")
study = int(input("Choose (1-5): "))

if study == "1":
    scores["Pomodoro"] += 1
elif study == "2":
    scores["Mind Mapping"] += 1
elif study == "3":
    scores["Active Recall"] += 1
elif study == "4":
    scores["Spaced Repetition"] += 1
elif study == "5":
    scores["Feynman"] += 1


print ("\nWhat frustrates you most about studying?😣")
print ("1) Studying too long without a break.")
print ("2) Not knowing if I really understood the topic.")
print ("3) Forgetting things after a few days.")
print ("4) Realizing I can’t answer simple questions without looking at my material after studying for hours.")
print ("5) Messy or unstructured material. Losing the thread of what connects the topics.\n")
problem = int(input("Choose (1-5): "))

if problem == "1":
    scores["Pomodoro"] += 1
elif problem == "2":
    scores["Feynman"] += 1
elif problem == "3":
    scores["Spaced Repetition"] += 1
elif problem == "4":
    scores["Active Recall"] += 1
elif problem == "5":
    scores["Mind Mapping"] += 1

print ("\nAfter studying, how do you reflect on what you learned?🔁")
print ("1) I check how much I got done in a set time.")
print ("2) I try teaching it or summarizing it aloud.")
print ("3) I look at my notes and diagrams/ pictures to see connections.")
print ("4) I test myself to check what stuck.")
print ("5) I review it again the next day to see what I remember.\n")
reflection = int(input("Choose (1-5): "))

if reflection == 1:
    scores["Pomodoro"] += 1
elif reflection == 2:
    scores["Feynman"] += 1
elif reflection == 3:
    scores["Mind Mapping"] += 1
elif reflection == 4:
    scores["Active Recall"] += 1
elif reflection == 5:
    scores["Spaced Repetition"] += 1

# Finding the study method with the highest score
best_method = max(scores, key=scores.get)
time.sleep(1)
print ("🎉Based on your answers, the best study method for you " + str(name) + " is:")
time.sleep(2)
typing("\033[91m" + best_method + "\033[0m")
time.sleep(2)
# Explaining the method
if best_method == "Pomodoro":
    print ("\n🧠This technique involves breaking your work into timed intervals, typically 25 minutes in length, called 'Pomodoros', separated by short breaks.")
elif best_method == "Feynman":
    print ("\n🧠This technique involves breaking down a concept into simple parts and then explaining it in your own words, as if you were teaching it to someone else. \nThe idea is to summarize what you've learned and try to explain it in a way even a child could understand. \nThis helps you identify gaps in your knowledge and truly understand the topic.")
elif best_method == "Active Recall":
    print ("\n🧠This technique involves actively trying to remember information from memory instead of just rereading it. \nYou study a topic, then test yourself by recalling the material without looking at your notes. \nIt works best when combined with other methods like flashcards or the Leitner System.")
elif best_method == "Mind Mapping":
    print ("\n🧠This technique involves visually organizing your thoughts by placing a main idea in the center and branching out with related concepts.")
elif best_method == "Spaced Repetition":
    print ("\n🧠This technique involves reviewing information at increasing intervals, with more time between reviews as you become more confident with the material. \nThis method is designed to help the brain retain information for longer by spreading out your studies over time instead of doing too much at once.")