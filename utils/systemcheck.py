import os
from pathlib import Path

os.system('cls' if os.name == 'nt' else 'clear')

files = os.listdir(".")

def systemCheck():
    
    index_path = Path('./index.html')
    root_dir = Path('./root')
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="./styles/bootstrap5.min.css" rel="stylesheet">
        <link href="./styles/style.css" rel="stylesheet">
        <title>index</title>
    </head>
    <body>

        <script src="./scripts/bootstrap5.min.js"></script>
        <script src="./scripts/script.js"></script>
    </body>
    </html>'''
    
    if not index_path.exists():
        print('index file is not present\nCreating index file...')
        index_path.write_text(html_template)

    if not root_dir.exists():
        print('root folder is not present\nCreating root folder...')
        root_dir.mkdir()
    print('System check successfull.')
    
    if not Path('./data').exists():
        print('Root folder is not present\nCreating root folder...')
        Path('./data').mkdir(parents=True, exist_ok=True)

    if not Path('./data/data.json').exists():
        print('data.json file is not present\nCreating data.json file...')
        Path('./data/data.json').touch()
        
systemCheck()