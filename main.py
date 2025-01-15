import os
import utils.renderFunc as renderFunc
from utils.systemcheck import systemCheck
files = os.listdir(".")
systemCheck()

def showHelpMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''    
        ╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌─┐  ╔═╗┌─┐┬  ┬┌─┐┬─┐
        ║║║├┤ │  │  │ ││││├┤    │ │ │  ╠═╝├─┤│ ┬├┤   ╚═╗├─┤└┐┌┘├┤ ├┬┘
        ╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ╩  ┴ ┴└─┘└─┘  ╚═╝┴ ┴ └┘ └─┘┴└─
        
        1 : save page            # save the element inside an html file.
        2 : save by URL          # save pages from the internet by URL.
        3 : delete pages         # delete the pages.
        4 : create/show category # create category to save the files in an organized way.
        5 :                      # upcoming features.
        6 : render data for HTML # render all of the files in the index page.
        7 : open in browser      # open in the browser.
        8 :                      # upcoming features.
        help/9 : show the help menu.
        enter/0 : exit           # exit the program.
    ''')
    
def main_menu():
    while True:
        userInputMainMenu = input('main >> ').strip()

        match userInputMainMenu:
            case '1':
                import utils.modulesFunc as modulesFunc
                modulesFunc.storeElements()
            case '2':
                import utils.savePageFromUrl as savePageFromUrl
                savePageFromUrl.main()
            case '3':
                print('upcoming features, delete pages.')
            case '4':
                import utils.categoryFunc as categoryFunc
                categoryFunc.main()
            case '5':
                print('upcoming features.')    
            case '6':
                renderFunc.main()
            case '7':
                renderFunc.main()
                import utils.runServer as runServer
                runServer.main()
            case '8':
                print('upcoming features.')        
            case 'help' | '9' | 'cls' | 'clear':
                showHelpMenu()
            case '0':
                break
showHelpMenu()
main_menu()