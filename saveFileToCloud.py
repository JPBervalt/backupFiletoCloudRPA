import pyautogui
import time

#código para realizar um backup de arquivo para um diretório cloud (neste caso google drive)
pyautogui.alert("O código será executado pelo Python e a automação será realizada! Não utilize o computador.")
pyautogui.PAUSE = 0.5
# abrir navegador
pyautogui.press('winleft')
pyautogui.write('opera')
pyautogui.press('enter')
# aguarda um momento
time.sleep(1)
#entra no google drive
pyautogui.write('drive.google.com')
pyautogui.PAUSE = 1
pyautogui.press('enter')
# minimizar
pyautogui.hotkey('winleft','d')
# clicar e arrastar arquivo
pyautogui.moveTo(423,796)
pyautogui.mouseDown()
# mudar para a tela do drive e soltar para realizar upload
pyautogui.moveTo(925,822)
pyautogui.hotkey('alt','tab')
pyautogui.mouseUp()
#aguardar upload do arquivo
time.sleep(60)
#fecha o navegador
pyautogui.hotkey('ctrl','w')
#avisa o usuário
pyautogui.alert('A automação foi finalizada com sucesso!')


