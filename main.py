import os,re
import sys
from pathlib import Path

from utils.systemcheck import systemCheck
files = os.listdir(".")

systemCheck()

# p = Path('./index.html')
# print(p.read_text())
print(os.listdir('./root'))

def showHelpMenu():
        os.system('cls' if os.name == 'nt' else 'clear')
        # print("\n" * 100)
        print('''
            ╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌─┐  ╔═╗┌─┐┬  ┬┌─┐┬─┐
            ║║║├┤ │  │  │ ││││├┤    │ │ │  ╠═╝├─┤│ ┬├┤   ╚═╗├─┤└┐┌┘├┤ ├┬┘
            ╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ╩  ┴ ┴└─┘└─┘  ╚═╝┴ ┴ └┘ └─┘┴└─
            
            1 : save page            # save the element inside an html file.
            2 : save by URL          # save pages from the internet by url.
            3 : delete pages         # delete the pages.
            4 : create/show category # create category to save the files in organize way.
            5 : 
            6 : render data for html # render all of the files in index page.
            7 : open in browser      # open in the brwser.
            8 :
       help/9 : show the help menu.
      enter/0 : exit                 # exit the program.
            ''')
showHelpMenu()
while True:
    import utils.modulesFunc as modulesFunc
    import utils.categoryFunc as categoryFunc
    import utils.renderFunc as renderFunc
    import utils.savePageFromUrl as savePageFromUrl

    userInputMainMenu=input('main >> ').strip()
    match userInputMainMenu:
        case '1':
            modulesFunc.storeElements()
        case '2':
            savePageFromUrl.main()
        case '3':
            print('upcoming features, delete pages.')
        case '4':
            categoryFunc.main()
        case '5':
            print('upcoming features.')    
        case '6':
            renderFunc.main()
        case '7':
            print('upcoming features.')
        case '8':
            print('upcoming features.')        
        case 'help' | '9':
            showHelpMenu()
        case '' | '0':
            break   

    