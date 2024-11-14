import os,re
import sys
from pathlib import Path
from datetime import datetime


def storeElements():
    import utils.categoryFunc as categoryFunc
    userElemPasteInput=None
    userNewFileNameInput = None   
    root_dir = Path('./root')
    root_dir.mkdir(parents=True, exist_ok=True)

    print("Paste your text and press Ctrl+D (or Ctrl+Z on Windows) to submit.")
    while True:
        userElemPasteInput = sys.stdin.read().strip()
        if userElemPasteInput:
            break
        print("Input element be empty. write somthing.")
        
    while True:
        userNewFileNameInput = input("Please assign a name for the file: ").strip()
        if userNewFileNameInput:
            break
        print("File name cannot be empty.")   
        
    cleaned_html = re.sub(r'\s(class|style)="[^"]*"', '', userElemPasteInput)
    userInputToHtmlTemplate = f'''
          <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{userNewFileNameInput}</title>
                <link href="../../styles/bootstrap5.min.css" rel="stylesheet">
                <link href="../../styles/style.css" rel="stylesheet">
                </head>
                <body class="text-break p-3">
                <a href="../../index.html" class="h1">⇦ Go Back</a>
                <div class="clearfix mb-5"></div>
                {cleaned_html}
                
                <script src="../../scripts/bootstrap5.min.js"></script>
                <script src="../../scripts/script.js"></script>
                </body>
            </html>
          '''

    
    while True:
        categoryName = categoryFunc.main()
        root_dir = Path(f'./root/{categoryName}')
        break
 
 
    newFile = root_dir/(userNewFileNameInput.replace(' ', '-')+f'-{datetime.now().strftime("%Y-%m-%d_%H-%M")}.html')
    with open(newFile, 'w',encoding='utf-8') as f:
        f.write(userInputToHtmlTemplate)
    
    print(f'file {userNewFileNameInput.replace(' ', '-')}-{datetime.now().strftime("%Y-%m-%d_%H-%M")}.html created successfully.')

 