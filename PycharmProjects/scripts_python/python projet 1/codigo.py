#passo a passo  d21m10a77


# 1.Entrar no sistema da empresa

#4.cadastrar um produdo
#repetir isso ate acabar base de dados      


import pyautogui

import pandas 

pyautogui.PAUSE = 3   
pyautogui.press("win")
import time
time.sleep(2)
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https:dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.click(x=400, y=411)
pyautogui.write("cristiano.brito.g@gmail.com")
pyautogui.press("tab")
time.sleep(0.5  )
pyautogui.write("d21m10a77")
pyautogui.press("tab")
pyautogui.press("enter")
import pandas
tabela=pandas.read_csv("produtos.csv")
pyautogui.click(x=413, y=296)
for linha in tabela.index:
    pyautogui.click(x=413, y=296)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.click(x=429,y=392)
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("enter")
    pyautogui.scroll(5000)












              
            
