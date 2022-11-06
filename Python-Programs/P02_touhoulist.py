# Current: Japanese Word List Creator
# Originally: Touhou Name List Creator
# Created May 2022 by Harrison Low
# Current: Creates a text file with utf-16 encoding which lists the english spelling of a name/meaning or a word and the japanese spelling of said name or word in either hiragana or katakana(should also work with Kanji). User can add to the file, delete from the file, update an entry or quit out and the file should be organized alphabetically. For now, names will be capitalized, and words will be in lower case as that will make it easier to differentiate.
# Originally: Should create a text file which lists the character's romanized name, japanese name in either hiragana or katakana which is sorted alphabetically

import os.path
import sys
from quicksort import quicksort, partition

# an object of this class represents a list of words containing the English and Japanese spelling
class characterList:
    def __init__(self, filename):
        self.__file = filename
        self.__list = {}
        self.update_list()
        
    def add(self, romname, janame):
        '''
        Adds the English and Japanese name pair to the file and list
        inputs: 
           romname - (str): The romanized spelling/English meaning of a word/name
           janame - (str): The Japanese spelling of a word/name
        returns: None
        '''
        # Checks if the name is not in the file then appends to file
        if romname not in self.__list: 
            with open(self.__file, 'a', encoding = 'utf-16') as file:
                file.write('{0} {1}\n'.format(romname, janame))
        else:
            print('Word already in file')
        # Updates the classes word list
        self.update_list()
        self.sort_file()
            
    def update_list(self):
        '''
        Updates the word list based on the given file
        inputs: None
        returns: None
        '''
        # Checks if the file exists in the same location as this program
        if os.path.exists(self.__file):
            self.__list = {}
            with open(self.__file, 'r', encoding = 'utf-16') as file:
                for line in file:
                    line = line.strip('\n')
                    if line != 'Words':
                        name_length = 0
                        data = line.split()
                        # Checks if the character uses ascii
                        for i in range(len(data)):
                            if data[i][0].isascii():
                                name_length += 1
                        key_name = " ".join(data[0:name_length])   # The key of the dictionary is the English part of the line in the file
                        value_name = ' '.join(data[name_length:])   # The value of the dictionary is the Japanese part of the line in the file
                        self.__list[key_name] = value_name
        # Creates a new file with encoding utf-16 if file does not already exist in the same location as this program
        else:
            with open(self.__file, 'wb') as new_file:
                new_file.write('Words\n'.encode('utf-16')) 
                
    def sort_file(self):
        '''
        Sorts the word list file in alphabetical order
        inputs: None
        returns: None
        '''
        key_list = list(self.__list.keys())
        # Sorts the list of keys in alphabetical order
        quicksort(0, len(key_list), key_list)
        # Creates a new file named the exact same as the original to replace it
        with open(self.__file, 'wb') as sorted_file:
            sorted_file.write('Words\n'.encode('utf-16'))
        # Appends the entries of the sorted list into the file
        with open(self.__file, 'a', encoding = 'utf-16') as sorted_file:
            for item in key_list:
                sorted_file.write("{0} {1}\n".format(item, self.__list[item]))
        # Updates the list(Note, the file is already updated)
        self.update_list()
            
    def delete_value(self, keyname):
        '''
        Deletes the entry from the list and updates the file accordingly
        inputs:
           keyname - (str): The English name/meaning being removed
        returns: None
        '''
        # Checks if the key is in the dictionary
        if keyname in self.__list:
            del self.__list[keyname]   # Deletes the key
            self.sort_file()
        else:
            raise Exception('Name not found')
        
    def update_value(self, keyname, new_value):
        '''
        Updates an entry's value(Japanese word) and updates the file accordingly
        inputs:
           keyname - (str): The English name/meaning linked to the original value
           new_value - (str): The new Japanese word which will be linked to the key
        returns: None
        '''
        # Checks if the key is in the dictionary
        if keyname in self.__list:
            self.__list[keyname] = new_value   # Updates the keys value
            self.sort_file()
        else:
            raise Exception('Name not found')
        
    def update_key(self, oldkey, newkey):
        '''
        Updates an entry's key(English word) and updates the file accordingly
        inputs:
           oldkey - (str): The original English name/meaning
           newkey - (str): The new English name/meaning
        returns: None
        '''
        # Checks if the original key exists in the dictionary
        if oldkey in self.__list:
            # Adds the new key to the dictionary with the original's value
            self.__list[newkey] = self.__list[oldkey]
            del self.__list[oldkey]   # Deletes the old key value
            self.sort_file()
        else:
            raise Exception('Name not found')
    
    def __str__(self):
        # String representation is a multiline string
        str_representation = """"""
        with open(self.__file, 'r', encoding = 'utf-16') as file:
            # Appends each line to the string representation
            for line in file:   # Note, keeping the newline character for each line
                str_representation += line
        return str_representation
        
def user_choice():
    '''
    Prompts user whether they wish to add, update, delete from the word list or quit out of program
    inputs: None
    returns: String containing the user's choice
    '''
    valid_choice = False
    choices = ['a', 'u', 'd', 'q']   # Not sure if I should keep the implementation with hard coded options here
    # Prompts user for input until a valid option is chosen
    while not valid_choice:
        choice = input("Would you like to add, update, delete, or quit out(a/u/d/q)? ").lower()
        if choice in choices:
            valid_choice = True
        else:
            print('Invalid Input')
    return choice

def add_name(list_name):
    '''
    Obtains user input for romanized and Japanese spelling then adds it to the word list file
    inputs:
       list_name - (characterList): The name of the character list object being editted
    returns: Boolean False if returning to main user choice and True if quitting out of program
    '''
    quit = False
    complete = False
    # While loop until return or quit is chosen
    while not complete:
        valid_selection = False 
        # Prompts user for romanized word and Japanese spelling
        romanized_name = input('Please input the romanized name/English meaning: ')
        japanese_name = input('Please input the Japanese name/word: ')
        while not valid_selection:
            confirmation = input('({0} {1}) Confirm if this is correct, return or quit out(y/n/r/q): '.format(romanized_name, japanese_name)).lower()
            if confirmation == 'y':
                list_name.add(romanized_name, japanese_name)
                valid_selection = True
            elif confirmation == 'n':
                valid_selection = True
            elif confirmation == 'r':
                return quit
            elif confirmation == 'q':
                quit = True
                return quit
                
def update_entry(list_name):
    '''
    Prompts user whether they want to update the English word or Japanese word for the file then updates accordingly
    inputs:
       list_name - (characterList): The name of the character list object being editted
    returns: Boolean False if returning to main user choice and True if quitting out of program
    '''
    quit = False
    complete = False
    # While loop until return or quit is chosen
    while not complete:
        valid = False
        option = input('Want to update the English spelling, Japanese spelling, print a list of current words,\nreturn, or quit out(e/j/p/r/q)?: ').lower()   # Newline character for better view
        # Updates the English word(key)
        if option == 'e':
            prev_name = input('Please input the previous English spelling: ')
            new_name = input('Please input the new English spelling: ')
            while not valid:
                confirmation = input('(Old-{0} New-{1}) Confirm if this is correct(y/n): '.format(prev_name, new_name)).lower()
                if confirmation == 'y':
                    # Try except to check if the key exists in the list or not
                    try:
                        list_name.update_key(prev_name, new_name)
                    except Exception as data_error:
                        print(data_error.args[0])        
                    valid = True
                elif confirmation == 'n':
                    valid = True
        # Updates the Japanese word(value)
        elif option == 'j':
            key = input('Please input English spelling/meaning: ')
            new_name = input('Please input the new Japanese spelling: ')
            while not valid:
                confirmation = input('(Eng-{0} NewJp-{1}) Confirm if this is correct(y/n): '.format(key, new_name)).lower()
                if confirmation == 'y':
                    # Try except to check if the key exists in the list or not
                    try:
                        list_name.update_value(key, new_name)
                    except Exception as data_error:
                        print(data_error.args[0])
                    valid = True
                elif confirmation == 'n':
                    valid = True
        # Prints the list of words
        elif option == 'p':
            print(list_name)
        elif option == 'r':
            return quit
        elif option == 'q':
            quit = True
            return quit
        
def delete_entry(list_name):
    '''
    Prompts user whether they would like to delete an entry in the file then updates accordingly
    inputs:
       list_name - (characterList): The name of the character list object being editted
    returns: Boolean False if returning to main user choice and True if quitting out of program
    '''
    quit = False
    valid = False
    # While loop until return or quit is chosen
    while not valid:
        choice = input('Would you like to delete, print current words, return or quit out(d/p/r/q): ').lower()
        # Deletes the entry from the file
        if choice == 'd':
            # Prompts the user for the English word
            key = input('Input the English spelling of the word being deleted: ')
            # Try except to check if the key exists in the list
            try:
                list_name.delete_value(key)
            except Exception as data_error:
                print(data_error.args[0])
        # Prints current list of words
        elif choice == 'p':
            print(list_name)
        elif choice == 'r':
            return quit
        elif choice =='q':
            quit = True
            return quit
        
def main():
    exit = False
    # Creates the word list object and file
    chrlist = characterList('words.txt')
    # While loop until user quits out
    while not exit:
        # Prompts user for which action to take
        choice = user_choice()
        # Adds an entry to the file
        if choice == 'a':
            exit = add_name(chrlist)
        # Updates an entry in the file
        elif choice == 'u':
            exit = update_entry(chrlist)
        # Deletes an entry from the file
        elif choice == 'd':
            exit = delete_entry(chrlist)
        elif choice == 'q':
            exit = True
    print('Now quitting out...')    
main()
