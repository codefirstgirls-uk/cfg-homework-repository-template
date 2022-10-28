"""
Create required phrase.
----------------------
You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.
NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.
FOR EXAMPLE:
    characters = "cbacba"
    phrase = "aabbccc"
    In this case you CANNOT create required phrase, because you are 1 character short!
IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.
    You can always generate an empty string.
"""
from collections import Counter

def generate_phrase(letters: str, phrase: str) -> bool:
    phrase_counter = Counter(phrase.lower())
    characters_counter = Counter(letters.lower())

    if not phrase_counter and not characters_counter:
        return True

    if len(phrase) > len(letters):
        return False

    for ch, cnt in phrase_counter.items():

        if ch in characters_counter and cnt <= characters_counter.get(ch):
            continue
        else:
            return False

    return True


if __name__ == '__main__':
    characters = "cbacba"
    phrase = "aabbccc"

    print(generate_phrase(characters, phrase))

    print(generate_phrase('you name it M1/P9', 'my name 1'))


