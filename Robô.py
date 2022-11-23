import pyautogui

#49
#currentMouseX, currentmouseY = pyautogui.position()#

#print(currentMouseX, currentmouseY )#
qtd= 48

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

pyautogui.keyDown('ctrl')
pyautogui.press(['c'])  
pyautogui.keyUp('ctrl')

pyautogui.keyDown('alt')
pyautogui.press(['tab','tab'])
pyautogui.keyUp('alt')

pyautogui.keyDown('ctrl')
pyautogui.press(['v'])  
pyautogui.keyUp('ctrl')

pyautogui.keyDown('alt')
pyautogui.press(['tab','tab'])
pyautogui.keyUp('alt')


for i in range (qtd):






    #Copia o "Serviço"
    pyautogui.press(['right','right','right'])
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])  
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    pyautogui.press(['-'])
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])  
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab','tab'])
    pyautogui.keyUp('alt')




    #Copia o "Grupo"
    pyautogui.press(['right','right','right','right'])
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])  
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    pyautogui.press(['tab','tab','tab'])
    pyautogui.press(['Del','Del','Del','Del','Del'])
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])  
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab','tab'])
    pyautogui.keyUp('alt')




    #Copia o "ValorSerivço"
    pyautogui.press(['right','right','right'])
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])  
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    pyautogui.press(['tab','tab','tab','tab','tab','tab'])
    
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])  
    pyautogui.keyUp('ctrl')

    pyautogui.click('Capturar.PNG')
    pyautogui.click('Novo.PNG')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab','tab'])
    pyautogui.keyUp('alt')





    #ReiniciarLoop
    pyautogui.press(['down','down','left','left','left','left','left','left','left','left','left','left',])
    
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])  
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])  
    pyautogui.keyUp('ctrl')

    pyautogui.keyDown('alt')
    pyautogui.press(['tab','tab'])
    pyautogui.keyUp('alt')



