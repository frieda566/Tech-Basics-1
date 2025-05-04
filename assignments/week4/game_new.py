import time
import sys

# Constants:
TYPING_SPEED = 0.08
MIN_FOCUS = 15
MAX_FOCUS = 90

STUDY_METHODS = {
    "Pomodoro": 0,
    "Feynman": 0,
    "Spaced Repetition": 0,
    "Active Recall": 0,
    "Mind Mapping": 0
}


# Utility Functions:
def typing(text):
    # simulating typing effect
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)


def ask_question(prompt, options):
    # displaying a prompt with options + validated choice
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = int(input("Choose an option: "))
        if 1 <= choice <= len(options):
            return choice
        else:
            print(f"Please choose an option from {options}.")


def explain_method(method):
    # prints explanation of the recommended study method
    explanations = {
        "Pomodoro": "\n🧠This technique involves breaking your work into timed intervals, typically 25 minutes in length, called 'Pomodoros', separated by short breaks.",
        "Feynman": "\n🧠This technique involves breaking down a concept into simple parts and then explaining it in your own words, as if you were teaching it to someone else. \nThe idea is to summarize what you've learned and try to explain it in a way even a child could understand. \nThis helps you identify gaps in your knowledge and truly understand the topic.",
        "Active Recall": "\n🧠This technique involves actively trying to remember information from memory instead of just rereading it.\nYou study a topic, then test yourself by recalling the material without looking at your notes.\nIt works best when combined with other methods like flashcards or the Leitner System.",
        "Mind Mapping": "\n🧠This technique involves visually organizing your thoughts by placing a main idea in the center and branching out with related concepts.",
        "Spaced Repetition": "\n🧠This technique involves reviewing information at increasing intervals, with more time between reviews as you become more confident with the material. \nThis method is designed to help the brain retain information for longer by spreading out your studies over time instead of doing too much at once.",
    }

    explanation = explanations.get(method)
    if explanation:
        print(f"\n Here's why {method} suits you:\n{explanation}")
    else:
        print("No explanation available.")


# Quiz Function
def questions(scores):
    # handles all quiz questions and updates the scores accordingly

    def style_preference():
        choice = ask_question(
            "Do you prefer structure or flexibility in your study sessions?",
            [
                "Structured routines",
                "Flexible sessions"
            ])

        if choice == 1:
            sub = ask_question("How do you organize your study sessions?",
                               [
                                   "Timed sessions with breaks",
                                   "Repeated reviews over a certain period of time"
                               ])
            if sub == 1:
                scores["Pomodoro"] += 1
            else:
                scores["Spaced Repetition"] += 1

        else:
            sub = ask_question("What do you do during your study sessions?",
                               [
                                   "Draw diagrams or visual overviews.",
                                   "Explain concepts out loud to yourself or others.",
                                   "Try to recall everything you've studied after a certain period of time.\n"
                               ])

            if sub == 1:
                scores["Mind Mapping"] += 1
            elif sub == 2:
                scores["Feynman"] += 1
            elif sub == 3:
                scores["Active Recall"] += 1

    def focus_duration():
        while True:
            focus = int(input(f"\nHow long can you focus?🎧 ({MIN_FOCUS} - {MAX_FOCUS} minutes): "))
            if MIN_FOCUS <= focus <= MAX_FOCUS:
                break
            else:
                print("Enter a number between {MIN_FOCUS} and {MAX_FOCUS}.")
        if 15 <= focus <= 25:
            scores["Pomodoro"] += 1
            scores["Spaced Repetition"] += 1
        elif 26 <= focus <= 40:
            scores["Active Recall"] += 1
        elif 41 <= focus <= 60:
            scores["Mind Mapping"] += 1
        elif 61 <= focus <= 90:
            scores["Feynman"] += 1

    def study_fatigue():
        choice = ask_question("\nHow do you feel after studying for long hours without breaks?📖",
                              [
                                  "I lose focus quickly.",
                                  "I manage fine, especially if I use visuals.",
                                  "I prefer to study myself frequently instead.",
                                  "I'm okay as long as I break it up across days.",
                                  "I like to use breaks to stop and explain the learned material to myself.\n"
                              ]
                              )
        mapping = {
            1: "Pomodoro",
            2: "Mind Mapping",
            3: "Active Recall",
            4: "Spaced Repetition",
            5: "Feynman",
        }
        scores[mapping[choice]] += 1

    def study_frustration():
        choice = ask_question("\nWhat frustrates you most about studying?😣",
                              [
                                  "Studying too long without a break.",
                                  "Not knowing if I really understood the topic.",
                                  "Forgetting things after a few days.",
                                  "Realizing I can’t answer simple questions without looking at my material after studying for hours.",
                                  "Messy or unstructured material. Losing the thread of what connects the topics.\n"
                              ])
        mapping = {
            1: "Pomodoro",
            2: "Feynman",
            3: "Spaced Repetition",
            4: "Active Recall",
            5: "Mind Mapping",
        }
        scores[mapping[choice]] += 1

    def reflection_style():
        choice = ask_question("\nAfter studying, how do you reflect on what you learned?🔁",
                              [
                                  "I check how much I got done in a set time.",
                                  "I try teaching it or summarizing it aloud.",
                                  "I look at my notes and diagrams/ pictures to see connections.",
                                  "I test myself to check what stuck.",
                                  "I review it again the next day to see what I remember.\n"
                              ])
        mapping = {
            1: "Pomodoro",
            2: "Feynman",
            3: "Mind Mapping",
            4: "Active Recall",
            5: "Spaced Repetition",
        }
        scores[mapping[choice]] += 1

    # run all functions for the quiz
    style_preference()
    focus_duration()
    study_fatigue()
    study_frustration()
    reflection_style()


# main
def main():
    typing("Welcome to the Study Method Quiz!📚")
    time.sleep(1)
    typing("What is your name?")
    name = input("\nEnter your name: ")
    time.sleep(1)

    typing(
        f"Hello {name}, based on questions about your preferred learning style this program will provide you with the best study method for you!")
    typing("\nLet's start.🚀\n")
    time.sleep(1)

    scores = STUDY_METHODS.copy()
    questions(scores)
    best_method = max(scores, key=scores.get)
    time.sleep(1)

    print(f"\n🎉Based on your answers, the best study method for you, {name}, is:")
    time.sleep(2)
    typing(f"\033[91m{best_method}\033[0m")
    time.sleep(1)
    explain_method(best_method)


# run program
if __name__ == "__main__":
    main()
