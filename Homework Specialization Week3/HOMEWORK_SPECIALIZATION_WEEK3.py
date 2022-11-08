"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
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


def generate_phrase(characters, phrase):
    # creating a count variable
    count = 0
    # if length of characters is less than phrase return false
    if len(characters) < len(phrase):
        return False
    # else if the length of the phrase is equal to zero and character
    # length is greater than zero then we create a phrase and return true
    elif len(phrase) == 0 and len(characters) > 0:
        return True
    # else check for each letter of phrase occur in the characters,
    # so we can create phrase
    else:
        # loop to go through each word of phrase and characters
        for i in phrase:
            for j in characters:
                # if letters in phrase matches letters in character
                if i == j:
                    # then increment the count variable
                    count = count + 1
                    # and break the loop
                    break
        # if count is equal to length of phrase
        # return true
        if count == len(phrase):
            return True
        # otherwise return false
        else:
            return False


# Test case 1 -- True
characters = "HRWEVBIOLGDYUIG"
phrase = "OVERBUILD"
print(generate_phrase(characters, phrase))

# Test case 2 -- False
characters = "ophny"
phrase = "python"
print(generate_phrase(characters, phrase))

# Test case 3 -- False
characters = ""
phrase = "eb yhppa"
print(generate_phrase(characters, phrase))

# Test case 4 -- True
characters = "doce iftrs iglrs"
phrase = ""
print(generate_phrase(characters, phrase))
