import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def getData(year):
    url = 'https://www.nba.com/stats/teams/traditional?dir=A&sort=TEAM_NAME&Season=' + year
   
    try:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--user-agent=Mozilla/5.0")

        driver = webdriver.Chrome(options)
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        ok_button = wait.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
        ok_button.click()

        table = driver.find_element(By.CLASS_NAME, "Crom_table__p1iZz") 

        thead = table.find_elements(By.XPATH, '*')[0]
        tbody = table.find_elements(By.XPATH, '*')[1]

        cols = thead.find_element(By.XPATH, '*')
        rows = tbody.find_elements(By.XPATH, '*')

        colList = cols.text.split()
        data = pd.DataFrame(columns = colList)

        for row in rows:
            lines = row.text.splitlines()
            row0 = lines[0] # teamname
            row1 = lines[1].split() # data
            row1.insert(0,row0)        
            data.loc[len(data.index)] = row1

        data.to_csv(f"data/nba_{year}.csv", index=False)
        return data
    except:
        return None
    finally:
        driver.close()
      
   