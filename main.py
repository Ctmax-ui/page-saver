import os,re
import sys
from pathlib import Path


os.system('cls' if os.name == 'nt' else 'clear')

files = os.listdir(".")

if not files.__contains__('index.html'):
    print('index.html is not present\nCreating index file...')
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
</head>
<body>
    
</body>
</html>'''
    with open('./index.html', 'w') as f:
        f.write(html_template)
        pass

if not files.__contains__('root'):
    print('root folder is not present\nCreating root folder...')
    os.mkdir('root')
    

# p = Path('./index.html')
# print(p.read_text())
print(os.listdir('./root'))

userInp =input('>>')

if True: #userInp:
    userElemPasteInput=None
    userNewFileNameInput = None
    print("Paste your text and press Ctrl+D (or Ctrl+Z on Windows) to submit:")
    while True:
        userElemPasteInput = sys.stdin.read().strip()
        if userElemPasteInput:
            break
        print("Input element be empty. Try again.")
    while True:
        userNewFileNameInput = input("Please assign a name for the file: ").strip()
        if userNewFileNameInput:
            break
        print("Input name be empty. Try again.")   
        
    cleaned_html = re.sub(r'\s(class|style)="[^"]*"', '', userElemPasteInput)
    userInputToHtmlTemplate = f'''
          <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{userNewFileNameInput}</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
                <link href="../styles/style.css" rel="stylesheet">
                </head>
                <body class="text-break p-3">
                <a href="../index.html" style="font-size:3rem">⬅ Go Back</a>
                {cleaned_html}
                
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
                </body>
            </html>
          '''
    with open(f'./root/{userNewFileNameInput.replace(' ', '-')}.html', 'w',encoding='utf-8') as f:
        f.write(userInputToHtmlTemplate)
        pass
    print('Writing Complete.')
    