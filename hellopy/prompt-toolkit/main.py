'''
    https://python-prompt-toolkit.readthedocs.io/en/3.0.52/pages/getting_started.html

    pip install prompt-toolkit

    Works over SSH sessions:

    Enter your name: 4
    Enter your age: v
    Hello, 4! You are v years old.
    Please select a dish:
        1. Pizza with mushrooms
        2. Salad with tomatoes
    >  3. Sushi
    3
    Your favorite color is Green.
    Choose a color (RGB): Red
    You typed Red
'''

from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import choice
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.validation import Validator, ValidationError

# Define a style for the prompts
style = Style.from_dict({
    'prompt': 'bg:#ansiblue #ffffff',  # Blue background, white text
})

# Create a validator for non-empty input
class NonEmptyValidator(Validator):
    def validate(self, document):
        if not document.text.strip():
            raise ValidationError(message="Input cannot be empty")

# Create a PromptSession with the style
session = PromptSession(style=style)

# Ask the first question
name = session.prompt("Enter your name: ", validator=NonEmptyValidator(), validate_while_typing=False)

# Ask the second question
age = session.prompt("Enter your age: ", validator=NonEmptyValidator(), validate_while_typing=False)

# Print the results
print(f"Hello, {name}! You are {age} years old.")

# Define options for the first question
color_options = [
    (0, "Red"),
    (1, "Blue"),
    (2, "Green"),
]

# Define options for the second question
food_options = [
    (0, "Pizza"),
    (1, "Sushi"),
    (2, "Pasta"),
]

# Ask the first question (color selection)
color = choice(
        message=HTML("<u>Please select a dish</u>:"),
        options=[
            (1, "Pizza with mushrooms"),
            (2, HTML("<ansigreen>Salad</ansigreen> with <ansired>tomatoes</ansired>")),
            (3, "Sushi"),
        ],
    style=style,
)

# Ask the second question (food selection)
# food = choice_input(
#     title="Choose your favorite food:",
#     values=food_options,
#     style=style,
# )

# Print the results
print(color)
print(f"Your favorite color is {color_options[color-1][1]}.")


from prompt_toolkit.completion import WordCompleter
session = PromptSession("Choose a color (RGB): ", completer=WordCompleter(["Red", "Blue", "Green"]), style=style)
color = session.prompt()
print("You typed", color)

