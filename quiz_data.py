# quiz_data.py
#
# Same idea as the mastery assessment: each question is stored as a
# dictionary, and every dictionary is collected into one list.
# This file only holds data -- no logic, no loops. That part lives
# in dict_loop_demo.py, which imports from here.

# A single standalone dictionary, same shape as a real quiz question,
# used only for practicing generic dictionary-looping (dict_loop_demo.py).
# Kept separate from the real quiz so the two don't get confused.
example = {
    "question": "Which island is Honolulu, Hawaii's capital, located on?",
    "a": "Maui",
    "b": "Oahu",
    "c": "Kauai",
    "answer": "b"
}

questions = [
    {
        "question": "How do Hawaiians greet each other?",
        "a": "Throw da shaka",
        "b": "Shake a thumbs up",
        "c": "Wave palm forward back and forth",
        "answer": "a"
    },
    {
        "question": "In what year did Hawaii become the 50th U.S. state?",
        "a": "1949",
        "b": "1959",
        "c": "1969",
        "answer": "b"
    },
    {
        "question": "What is Hawaii's official state fish?",
        "a": "Humuhumunukunukuapua'a",
        "b": "Mahi-mahi",
        "c": "Ono",
        "answer": "a"
    },
    {
        "question": "What is Hawaii's state bird?",
        "a": "Chicken",
        "b": "Mynah",
        "c": "Albatross",
        "answer": "a"
    },
    {
        "question": "What is the 8th Hawaiian island?",
        "a": "Niihau",
        "b": "Kahoolawe",
        "c": "Las Vegas",
        "answer": "c"
    }
]

print("quiz_data was loaded")
