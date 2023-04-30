import pyautogui

pyautogui.PAUSE = 2

pyautogui.press('win')

pyautogui.write("logar.ods")
pyautogui.press('backspace')
pyautogui.press('enter')
pyautogui.click(x=439, y=254)
pyautogui.write("Fabio")
pyautogui.click(x=466, y=320)
pyautogui.write("senha")
pyautogui.click(x=437, y=445)