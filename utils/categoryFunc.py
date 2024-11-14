import os,re
import sys
from pathlib import Path

def main():
    root_dir = Path('./root')
    root_dir.mkdir(parents=True, exist_ok=True)
    categoryName = None
    categories = [item.name for item in Path('./root').iterdir() if item.is_dir()]
    print(categories)
    item = input('Write the category name, "enter" to exit.\n: ').strip()
    if len(item) > 0:
        if item in categories:
            categoryName = item
            print(f"{item} category is in the list.")
        else:
            print(f"'{item}' category is not found in list.")
            categoryAccept = input('create category by typeing the name and "enter" for exit.\n: ').strip()
            
            match len(categoryAccept):
                case length if length > 1:
                    sanitized_category = re.sub(r"/", "", categoryAccept)
                    new_category_path = root_dir / sanitized_category
                    new_category_path.mkdir(parents=True, exist_ok=True)
                    print(f"Category '{sanitized_category}' successfully created.")
                    categoryName = sanitized_category
                case _:
                    print('no category created.')
                    categoryName= 'default'
    else:
        (default_category_path := root_dir / 'default').mkdir(parents=True, exist_ok=True)
        
        categoryName= 'default'
    return categoryName
