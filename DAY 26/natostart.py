# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# #TODO 1. Create a dictionary in this format:
natoPhoneticDict = {row.letter: row.code for (index, row) in data.iterrows()}


# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic():
    word = input("Enter a word: ").upper()
    try:
        outputData = [natoPhoneticDict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        phonetic()
    else:
        print(outputData)


phonetic()
