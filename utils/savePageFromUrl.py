from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re, json, requests, time
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime

with open(Path('./config.json')) as f:
    config = json.load(f)

def saveWithSelenium():
    brave_path = config["browser_path"]
    # brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    driver_path = Path("./driver/chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    # options.add_argument(r"user-data-dir=C:\Users\<your-userName>\AppData\Local\BraveSoftware\Brave-Browser\User Data")
    options.add_argument(f"user-data-dir={config["browser_userdata"]}")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--log-level=1")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    if(config["headless_webdriver"]):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    page_title=None
    exit_program = False
    url_pattern = re.compile(
        r'^(https?://)?'  # http:// or https:// (optional)
        r'([a-zA-Z0-9.-]+)?'  # Domain or subdomain
        r'(\.[a-zA-Z]{2,})'  # Dot-something (e.g., .com, .net)
        r'(:\d+)?'  # Optional port number
        r'(\/[^\s]*)?$',  # Path (optional)
        re.IGNORECASE
    )
    print('Type your url here, 0 for exit.')
    while True:
        url = input('>>').strip()
        if url == '0':
            print('Exiting the program.')
            exit_program = True
            break    
            
        if re.match(url_pattern, url):
            break
        print('invalid url, please check!')  
        
    if exit_program:
        return

    start_time = time.time()
    css_selector = input('Do you have any css selector in perticuler default selector is body "enter".\ncss-selector >>').replace(' ', '') or "body"
    service = Service(driver_path)
    print('Running the driver...')
    driver = webdriver.Chrome(service=service, options=options)
    try:
        print('Going to the destination page...')
        driver.get(url)
        print('Waiting for the element to appear...',css_selector)
        if(css_selector.count('.') == 1):
            elements = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        else: 
            elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)))
        # print(type(elements))
        
        page_title = driver.title
        body_html = ""
        for element in elements:
            print(element)
            body_html += element.get_attribute("outerHTML")

    except Exception as e:
        print("Error finding element:", e)
    finally:
        driver.quit()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")
    fileSaveParsed(body_html, page_title)
    return

def saveWithNormal():
    exit_program = False
    url_pattern = re.compile(
        r'^(https?://)?'  # http:// or https:// (optional)
        r'([a-zA-Z0-9.-]+)?'  # Domain or subdomain
        r'(\.[a-zA-Z]{2,})'  # Dot-something (e.g., .com, .net)
        r'(:\d+)?'  # Optional port number
        r'(\/[^\s]*)?$',  # Path (optional)
        re.IGNORECASE
    )
    print('Type your url here, 0 for exit.')
    while True:
        url = input('>>').strip()
        if url == '0':
            print('Exiting the program.')
            exit_program = True
            break    
            
        if re.match(url_pattern, url):
            break
        print('invalid url, please check!')
        
    if exit_program:
        return
    css_selector = input('Do you have any css selector in perticuler default selector is body "enter".\ncss-selector >>') or "body"   
    try:
        response = requests.get(url, {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    })
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        print('Page copied successfully.')
        page_title = soup.title.string if soup.title else None
        body_content = soup.body.decode_contents() if soup.select_one(css_selector) else None
        if body_content:
            fileSaveParsed(body_content,page_title)
        else:
            print('Unknown error, please try again.')
            
    except requests.exceptions.RequestException as e:
        status_code = e.response.status_code if e.response else "No Response"
        # print(f"An error occurred: {status_code}")
        print(f'Site fetcher failed with status Code: {e.response}')
    return 
    
def fileSaveParsed(body_html, page_title=None):
    removed_scripts_tag = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', str(body_html))
    removed_style_tag = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', removed_scripts_tag)
    body_cleaned_html = re.sub(r'\s(class|style)="[^"]*"', '', removed_style_tag)

    if(page_title):
        print('If your want to select default filename then "enter" or assign filename by typing.')
        print(f'your default filename is : {page_title}')
    
    file_name_input = input('Type the name of your file >>').strip()
    
    if len(file_name_input) == 0:
        file_name_input = page_title
    else:
        file_name_input = 'unknown'
        
    print([item.name for item in Path('./root').iterdir() if item.is_dir()])
    print('Type the name of your category. enter for default.')
    category_name = input('>>').strip()
    
    if len(category_name) == 0:
        category_name = 'default'
    
    file_save_path = Path(f'./root/{category_name}/{re.sub(r'[<>:"/\\|?*]', '', file_name_input).replace(' ', '-')}-{datetime.now().strftime("%Y-%m-%d_%H-%M")}.html')
    file_save_path.parent.mkdir(parents=True, exist_ok=True) 
    userInputToHtmlTemplate = f'''
          <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{file_name_input}</title>
                <link href="../../styles/bootstrap5.min.css" rel="stylesheet">
                <link href="../../styles/style.css" rel="stylesheet">
                </head>
                <body class="text-break p-3">
                <div class="clearfix mb-5"></div>
                {body_cleaned_html}
                
                <script src="../../scripts/bootstrap5.min.js"></script>
                <script src="../../scripts/script.js"></script>
                </body>
            </html>
          '''
    with open(file_save_path, 'w', encoding='utf-8') as f:
        f.write(userInputToHtmlTemplate)
        print('Page saved successfully.')
        return




def main():
        while True:
            print('''
              1: Quick Saver        #save the page quickly, !not recomanded for AUTH verifyied pages.
              2: Selenium Saver     #for complicated pages where you see content after login.
        0/enter: Exit
              ''')
            userInput = input('url-to-page>>').strip()
            match userInput:
                case '1':
                    saveWithNormal()
                case '2':
                    saveWithSelenium()
                case '0':
                    break
                case _:
                    break
           
# main()