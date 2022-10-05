#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invitedNames:
    names = invitedNames.readline()

with open("./Input/Letters/starting_letter.txt") as letterFile:
    letters = letterFile.read()
    for name in names:
        strippedName = name.strip()
        newLetter = letters.replace(PLACEHOLDER, strippedName)
        with open(f"./Output/ReadyToSend/letter_for_{strippedName}.txt", mode="w") as completedLetter:
            completedLetter.write(newLetter)
