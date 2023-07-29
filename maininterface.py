from Calculator.Calculator import calculator
from misc.loadingscreen import loading_screen
from games.guessinggame import guessinggame

Break = False

def maininterface():
    option = input("Select option here --> ")
    if option.lower() == "calc":
        loading_screen()
        calculator()
    if option.lower() == "files":
        pass
    if option.lower() == "guessinggame":
        guessinggame()
    if option.lower() == "help":
        print(""" 
              Applications:
              Calculator: 'calc'
              Guessing Game: 'guessinggame'
               """)
        
        

print("Welcome, please type 'help' to see a list of functions and applications")
while Break == False:
    maininterface()
