import os,re,sys,json
from pathlib import Path
from datetime import datetime
from utils.systemcheck import systemCheck

def main():
    systemCheck()
    jsonPth = Path('./data/data.json')
    jsonData =[]
    count = 0
    given_path = './root'

    for root, dirs, files in os.walk(given_path):
        for file in files:
            count += 1
            category = re.sub(r".*\\", "", root)
            newjsonData = {
                "count": count,
                "category": category,
                "fileName": file,
                "filePath": f"{root.replace(os.sep, '/')}/{file}",
                "timestamp": re.sub(r".*?(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}).*", r"\1", file)
            }
            # print(newjsonData)
            jsonData.append(newjsonData)
            
    with open(jsonPth,'w') as file: 
        json.dump(jsonData, file, indent=4)
        print('json data updated successfully.')
        