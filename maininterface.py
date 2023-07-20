from Calculator.Calculator import calculator
from misc.loadingscreen import loading_screen


def maininterface():
    loading_screen()
    print("Hello and welcome to the Common Use Machine")
    option = input("Select option here --> ")
    if option.lower() == "calc":
        loading_screen()
        calculator()
    if option.lower() == "files":
        pass


while True:
    maininterface()
