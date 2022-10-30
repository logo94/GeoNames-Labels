from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

fire_driver = GeckoDriverManager().install()
driver = Firefox(service=FirefoxService(fire_driver))
driver.maximize_window()

wb = openpyxl.load_workbook(file)
sh = wb.active
m_row = sh.max_row

def get_url(cell):
    url = sh.cell(row=i, column=1).value.replace("<", "").replace(">", "")
    return url

def get_label(i):
    url = get_url(i)
    driver.get(url)
    sleep(1)
    
    name = driver.find_element(By.XPATH,
    '/html/body/div[2]/h4').get_attribute("innerHTML").split(" - ")
    
    name_label = name[0]
    place_label = driver.find_elements(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[4]/small/a')[-1].get_attribute("innerHTML")   
  
    if place_label==name_label:
        label = name_label
    else:
        label = name_label + " " + "<" + place_label + ">"    

    labelCell = sh.cell(row=i, column=3)
    labelCell.value = label
    wb.save(file)

for i in range(1, m_row + 1):
    try:
        get_label(i)
    except:
        pass
    









