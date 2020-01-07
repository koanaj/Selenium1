from selenium import webdriver
import time, os, subprocess

print("\nPrzeglądanie z pomocą selenium\n")
print("\nOtwieram chrome...")


def wlacz():
    python_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]                   #wpisanie loginu w pole login (wpisać swój)
    python_button.send_keys('TwojLogin')                                                          #wysłanie klucza loginu
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]                      #wpisanie hasła w pole password (wpisać swój)
    python_button.send_keys('TwojeHaslo')                                                         #wysłanie klucza hasła
    python_button = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[8]")[0]    #wciśnięcie przycisku login
    python_button.click()
    time.sleep(1)                                                                                 #czekanie 1 sekundę

def reszta():
    browser.execute_script("window.open('https://stackoverflow.com/', 'tab2');")                  #przywołanie nowego okna ze stroną stackoverflow
    time.sleep(2)
    browser.switch_to.window("tab2")                                                              #zmiana okna na drugie


def program():
    subprocess.call('"C:\Windows\System32\Calc.exe"')                                             #włączenie kalkulatora


browser = webdriver.Chrome()                                                                      #przypisanie nazwy browser do silnika
browser.maximize_window()                                                                         #powiększenie okna przeglądarki
browser.get('http://github.com/login')                                                            #zainicjowanie strony github.


time.sleep(1)
wlacz()
time.sleep(1)
reszta()
program()








