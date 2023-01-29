# 22D TMA03 Q2 EXTENDED AURA

"""
This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks an entry from all glossary
entries. Then the program randomly picks either the entry or the definition
and displays it. After the user presses return, the program shows the
definition or entry of that particular flashcard.
The user can repeatedly ask for an entry and also
has the option to quit the program instead of seeing
another entry.
"""

from random import *

# *** Modify the body of the show_flashcard function so that it
# implements yout algorithm from part i. Also modify the docstring
# for the program and the docstring for the function, to take 
# account of the changes and their effect. ***

def show_flashcard():
    """ Show the user a random entry or definition and ask them
        to define it. Show the definition/entry
        when the user presses return.    
    """
    # It selects at random an entry from all the glossary entries
    
    random_key = choice(list(glossary))
    
    # It selects at random the entry or the definition from random_key
    
    random_key_or_definition = choice([random_key, glossary[random_key]])
    
    # Condition to show the user the corresponding definition if the entry
    # was displayed first or the corresponding entry if the definition was
    # displayed first
    
    if random_key_or_definition == random_key:
        print('What is the definition for the entry?: ', random_key_or_definition)
        input('Press return to see the definition')
        print(glossary[random_key])
    else:
        print('What is the entry for the definition?: ' , random_key_or_definition)
        input_entry = input('Please type the entry: ')
        if input_entry == random_key:
            print('Well done! ', random_key, 'is the entry.')
        else:
            print('Sorry, maybe next time! ', random_key, 'was the entry')

# Set up the glossary

glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
                       
