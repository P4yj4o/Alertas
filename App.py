import tkinter as tk
import pyautogui
import datetime
import time
import os

root = tk.Tk()
root.title("Scalation automações")
root.geometry("1920x1080")

def button1_click():

    #########################################################################################################################################################################

    #Scalation VIVO apos 2 horas - 11-5115-6030 (opcao 1.6)
    pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")

    # ABRIR RELÓGIO NO MEU COMPUTADOR
    path_dir = 'C:\Program Files\WindowsApps\Microsoft.WindowsAlarms_11.2302.5.0_x64__8wekyb3d8bbwe\Time.exe'

    os.startfile(path_dir)

    #SELECIONAR TEMPORIZADOR PARA QUE NÃO HAJA PROBLEMAS
    time.sleep(1)
    pyautogui.press('alt')
    time.sleep(1)
    pyautogui.press('2')

    # CRIAR NOVO TIMER
    time.sleep(1)
    pyautogui.click(1849 , 942)
    time.sleep(1)
    pyautogui.click(1092 , 615)
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write('Scalation VIVO apos 2 horas - 11-5115-6030 (opcao 1.6)')
    time.sleep(1)

    # INSERIR O TEMPO (HORAS) :
    pyautogui.click(806 , 426) 
    time.sleep(1) 
    pyautogui.write('2')

    # SALVAR E STARTAR TIMER:
    #salvar o timer
    time.sleep(1)
    pyautogui.click(842 , 734)

    #click do start timer:
    time.sleep(1)
    pyautogui.click(802 , 497)

    #########################################################################################################################################################################

    # Scalation VIVO apos 2 horas - 11-5115-6030 (opcao 1.7).  Caso não obtiver sucesso ligar para Giacomo Martins de Oliveira (41-98875-5197 - Horario comercial das 09:00 as 19:00

    # CRIAR NOVO TIMER
    time.sleep(2)
    pyautogui.click(1849 , 942)
    time.sleep(1)
    pyautogui.click(1092 , 615)
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write('Scalation VIVO apos 2 horas - 11-5115-6030 (opcao 1.7).  Caso não obtiver sucesso ligar para Giacomo Martins de Oliveira (41-98875-5197 - Horario comercial das 09:00 as 19:00)')
    time.sleep(1)

    # INSERIR O TEMPO (HORAS) :

    pyautogui.click(806 , 426) 
    time.sleep(1) 
    pyautogui.write('2')

    # INSERIR O TEMPO (MINUTOS) :
    pyautogui.click(958 , 427)
    time.sleep(1)
    pyautogui.write('5')

    # SALVAR, STARTAR TIMER:
    #salvar o timer
    time.sleep(1)
    pyautogui.click(842 , 734)

    #click do start timer:
    time.sleep(1)
    pyautogui.click(1473 , 503)

    #########################################################################################################################################################################


    # Scalation VIVO apos 4 horas - DIEGO SANTOS BARBOSA (41-996283754)

    # CRIAR NOVO TIMER
    time.sleep(1)
    pyautogui.click(1849 , 942)
    time.sleep(1)
    pyautogui.click(1092 , 615)
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write('Scalation VIVO apos 4 horas - DIEGO SANTOS BARBOSA (41-996283754) OU CLEBER SOUZA SANCHES (11-996144343)')
    time.sleep(1)

    # INSERIR O TEMPO (HORAS) :

    pyautogui.click(806 , 426) 
    time.sleep(1) 
    pyautogui.write('4')

    # SALVAR, STARTAR E FECHAR TIMER/RELÓGIO :
    #salvar o timer
    time.sleep(1)
    pyautogui.click(842 , 734)
    time.sleep(1)

    #click do start timer:
    pyautogui.click(799 , 995)

    # FECHAR O RELÓGIO
    time.sleep(1)
    pyautogui.hotkey('alt','f4')

    pyautogui.alert("Seus alertas para seguir scalation list da VIVO em salas de crise foram criados. Por favor se atente as notificações!!")

def button2_click():
    pyautogui.alert("Encerrando os processos! Aguarde!")

    # ABRIR RELÓGIO NO MEU COMPUTADOR
    path_dir = 'C:\Program Files\WindowsApps\Microsoft.WindowsAlarms_11.2302.5.0_x64__8wekyb3d8bbwe\Time.exe'

    os.startfile(path_dir)

    #SELECIONAR TEMPORIZADOR PARA QUE NÃO HAJA PROBLEMAS
    time.sleep(1)
    pyautogui.press('alt')
    time.sleep(1)
    pyautogui.press('2')
    
    # BOTÃO EDITAR (RELÓGIO)
    time.sleep(2)
    pyautogui.click(1789 , 940)
    time.sleep(1)

    # BOTÃO EXCLUIR
    pyautogui.click(1520 , 755)
    time.sleep(1)
    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.press('delete')


    # FECHAR O RELÓGIO
    time.sleep(1)
    pyautogui.hotkey('alt','f4')

    pyautogui.alert("Pronto seus timers foram encerrados!! ;)")

def button3_click():
    #########################################################################################################################################################################

    #AVISO DE 30 MIN OLHAR E-MAIL
    pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")

    # ABRIR RELÓGIO NO MEU COMPUTADOR
    path_dir = 'C:\Program Files\WindowsApps\Microsoft.WindowsAlarms_11.2302.5.0_x64__8wekyb3d8bbwe\Time.exe'

    os.startfile(path_dir)

    #SELECIONAR ALARME PARA QUE NÃO HAJA PROBLEMAS
    time.sleep(1)
    pyautogui.press('alt')
    time.sleep(1)
    pyautogui.press('3')

    # CRIAR NOVO TIMER
    time.sleep(1)
    pyautogui.click(1849 , 942)
    time.sleep(1)
    pyautogui.click(989 , 442)
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write('AVISO DE 30 MIN CHECAR SE TEVE ATUALIZACOES NA TA')
    time.sleep(1)

def button4_click():
    
    #########################################################################################################################################################################
    pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")


# Criando os botões
Scalation_VIVO_Salas_de_crise = button1 = tk.Button(root, text="Scalation VIVO (Timers)" , command=button1_click)
Encerrar_Processos_Timers = button2 = tk.Button(root, text="Encerrar Processos (Timers)" , command=button2_click)
Aviso_de_30min_olhar_email = button3 = tk.Button(root, text="Criar aviso de 30min para olhar e-mail TA (VIVO)", command=button3_click)
Sala_de_crise_de_Rede_Interna = button4 = tk.Button(root, text="Scalation Sala de crise de Rede Interna", command=button4_click)
#button5 = tk.Button(root, text="Botão 5")
#button6 = tk.Button(root, text="Botão 6")

# Posicionando os botões na interface
button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=0, column=2, padx=10, pady=10)
button4.grid(row=1, column=0, padx=10, pady=10)
#button5.grid(row=1, column=1, padx=10, pady=10)
#button6.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
