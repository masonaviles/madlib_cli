# import ReGex module
import re

# to output welcome message and rules of the game to the screen
def start_text():
    text = """
    **************************************************************
    **   Welcome to Mad Libs, where every word makes            **
    **   sense as long it's the correct part of speech.         **
    **   Wamalamakingpong. All you have to do is answer some    **
    **   questions and I'll give you an interesting story.      **
    **   Let's play.                                            **
    **************************************************************
    """
    print(text)

start_text()

# def test_read_template_returns_stripped_string():
#     actual = read_template("assets/dark_and_stormy_night.txt")
#     expected = "It was a {Adjective} and {Adjective} {Noun}."
#     assert actual == expected

# that takes in a path to text file and returns a stripped string of the file’s contents.
# should raise a FileNotFoundError if path is invalid
def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

template_file = read_template('template_madlib.txt')

# def test_parse_template():
#     actual_stripped, actual_parts = parse_template(
#         "It was a {Adjective} and {Adjective} {Noun}."
#     )
#     expected_stripped = "It was a {} and {} {}."
#     expected_parts = ("Adjective", "Adjective", "Noun")

#     assert actual_stripped == expected_stripped
#     assert actual_parts == expected_parts

# function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
def parse_template(contents):
    actual_stripped = ""
    actual_parts = []
    in_brackets = False
    temp_word_string = ""

    # The count() method returns the number of elements with the specified value.
    num_brackets = contents.count('{') + contents.count('}')
    if (num_brackets > 0 and num_brackets % 2 == 0):
        for char in contents:
            if char == '{':
                actual_stripped += char
                in_brackets = True
            elif char == '}':
                actual_stripped += char
                in_brackets = False
                actual_parts.append(temp_word_string)
                temp_word_string = ""
            elif in_brackets:
                temp_word_string += char
            else:
                actual_stripped += char
    else:
        raise Exception("Incorrect template format")
    
    return (actual_stripped, tuple(actual_parts))

# def test_merge():
#     actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
#     expected = "It was a dark and stormy night."
#     assert actual == expected

# function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template

def merge(string_to_fill, responses):
    # The format() method formats the specified value(s) and insert them inside the string's placeholder. The placeholder is defined using curly brackets: {}.
    return string_to_fill.format(*responses)