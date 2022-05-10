import requests
import random
import time
import sys
from bs4 import BeautifulSoup


class Hackterms:


    def __init__(self):
        # This program uses HackTerms as the source of programmer related words and definitions.
        self.url = "https://www.hackterms.com/"


    def get_random_word(self) -> str:
        '''
        Returns a random word from the codeword list.
        '''
        response = requests.get(self.url + "all-terms")
        filtered_terms = [term for term in response.json().get("terms") if len(term) > 4 and len(term) < 12]
        return filtered_terms[random.randint(0, len(filtered_terms))]


    def get_definition(self, term) -> str:
        '''
        Returns the definition of the given term.
        '''
        try:
            response = requests.post(self.url + "get-definitions/", data={"term": term, "user": False}) 
            return response.json().get("body")[0].get("body")
        except Exception as e:
            print(e)
            return "No defintion has been found."



class Game:


    def __init__(self):
        code = Hackterms()
        self.term = code.get_random_word()
        self.definition = code.get_definition(self.term)
        self.definition = self.definition.lower().replace(self.term, "[TERM]") # replace all occurances of the term in the definition with "[TERM]"
        self.attempts = 0

    def delay_print(self, text, delay=0.03) -> None:
        for char in text:
            print(char, end="", flush=True)
            time.sleep(.02)
    

    def intro(self) -> None:
        self.delay_print("Welcome to Codewords!\n---\nIn this game, you will guess programmer-related words within 6 tries!\n")
        self.delay_print("We are generating your first word\n...\n")
        time.sleep(.5)
        self.delay_print("...\n")
        time.sleep(.5)
        self.delay_print("...\n")
        self.delay_print("Your Code Word has been generated!\nIt is " + str(len(self.term)) + " characters long.\n")
        self.delay_print("Here is your first hint\n---\nThe definition is: " + self.definition, 0)


    def guess(self):
        guess_attempt = input("What is your guess? \n").lower()
        self.attempts += 1
        if (guess_attempt == self.term):
            print(f"You guessed the Code Word correctly in {self.attempts} attempt(s)!\n")
        else:
            print("You guessed incorrectly! Try again!")
            self.guess()


    def play(self):
        self.intro()
        self.guess()
        
    



game = Game()
game.play()