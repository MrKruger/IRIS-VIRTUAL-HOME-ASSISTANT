"""
    TITLE: IRIS RESIDENTIAL VIRTUAL ASSISTANT
    AUTHORS: BRUNO DE OLIVEIRA FERNANDES, GABRIEL KRÜGER, PEDRO SARRO ORTOLANI
    DATE: 13/11/17
    v1.0
"""

import speech_recognition as Sr
import paho.mqtt.publish as publish
from gtts import gTTS
from playsound import playsound
import Weather
import cv2
from Email_SMTP import Send_Email_Settings

from datetime import datetime
import webbrowser
import random
import time
import os

"""
Banner_1 = 
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
     ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌          
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ 
     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌
     ▐░▌     ▐░█▀▀▀▀█░█▀▀      ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌     ▐░▌       ▐░▌               ▐░▌
 ▄▄▄▄█░█▄▄▄▄ ▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
	                                                    
                 Your Virtual Home Assistant!


Banner_2 =                                                                                     
IIIIIIIIIIRRRRRRRRRRRRRRRRR   IIIIIIIIII   SSSSSSSSSSSSSSS 
I::::::::IR::::::::::::::::R  I::::::::I SS:::::::::::::::S
I::::::::IR::::::RRRRRR:::::R I::::::::IS:::::SSSSSS::::::S
II::::::IIRR:::::R     R:::::RII::::::IIS:::::S     SSSSSSS
  I::::I    R::::R     R:::::R  I::::I  S:::::S            
  I::::I    R::::R     R:::::R  I::::I  S:::::S            
  I::::I    R::::RRRRRR:::::R   I::::I   S::::SSSS         
  I::::I    R:::::::::::::RR    I::::I    SS::::::SSSSS    
  I::::I    R::::RRRRRR:::::R   I::::I      SSS::::::::SS  
  I::::I    R::::R     R:::::R  I::::I         SSSSSS::::S 
  I::::I    R::::R     R:::::R  I::::I              S:::::S
  I::::I    R::::R     R:::::R  I::::I              S:::::S
II::::::IIRR:::::R     R:::::RII::::::IISSSSSSS     S:::::S
I::::::::IR::::::R     R:::::RI::::::::IS::::::SSSSSS:::::S
I::::::::IR::::::R     R:::::RI::::::::IS:::::::::::::::SS 
IIIIIIIIIIRRRRRRRR     RRRRRRRIIIIIIIIII SSSSSSSSSSSSSSS   

                        Your Virtual Home Assistant! 


Banner_3 = 
██╗██████╗ ██╗███████╗
██║██╔══██╗██║██╔════╝
██║██████╔╝██║███████╗
██║██╔══██╗██║╚════██║
██║██║  ██║██║███████║
╚═╝╚═╝  ╚═╝╚═╝╚══════╝

Your Virtual Home Assistant!


Banner_4 = 
 ██▓ ██▀███   ██▓  ██████ 
▓██▒▓██ ▒ ██▒▓██▒▒██    ▒ 
▒██▒▓██ ░▄█ ▒▒██▒░ ▓██▄   
░██░▒██▀▀█▄  ░██░  ▒   ██▒
░██░░██▓ ▒██▒░██░▒██████▒▒
░▓  ░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░
 ▒ ░  ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░
 ▒ ░  ░░   ░  ▒ ░░  ░  ░  
 ░     ░      ░        ░  
                          
Your Virtual Home Assistant!


Banner_5 = 
 ▄█     ▄████████  ▄█     ▄████████ 
███    ███    ███ ███    ███    ███ 
███▌   ███    ███ ███▌   ███    █▀  
███▌  ▄███▄▄▄▄██▀ ███▌   ███        
███▌ ▀▀███▀▀▀▀▀   ███▌ ▀███████████ 
███  ▀███████████ ███           ███ 
███    ███    ███ ███     ▄█    ███ 
█▀     ███    ███ █▀    ▄████████▀  
       ███    ███                   

Your Virtual Home Assistant!



Banner_6 =                                             
 8 8888 8 888888888o.    8 8888    d888888o.   
 8 8888 8 8888    `88.   8 8888  .`8888:' `88. 
 8 8888 8 8888     `88   8 8888  8.`8888.   Y8 
 8 8888 8 8888     ,88   8 8888  `8.`8888.     
 8 8888 8 8888.   ,88'   8 8888   `8.`8888.    
 8 8888 8 888888888P'    8 8888    `8.`8888.   
 8 8888 8 8888`8b        8 8888     `8.`8888.  
 8 8888 8 8888 `8b.      8 8888 8b   `8.`8888. 
 8 8888 8 8888   `8b.    8 8888 `8b.  ;8.`8888 
 8 8888 8 8888     `88.  8 8888  `Y8888P ,88P' 

            Your Virtual Home Assistant!


"""
Banner_1 = """
s.  .s5SSSs.  s.  .s5SSSs.  
SS.       SS. SS.       SS. 
S%S sS    S%S S%S sS    `:; 
S%S SS    S%S S%S SS        
S%S SS .sS;:' S%S `:;;;;.   
S%S SS    ;,  S%S       ;;. 
`:; SS    `:; `:;       `:; 
;,. SS    ;,. ;,. .,;   ;,. 
;:' `:    ;:' ;:' `:;;;;;:'                             	                                                   

Your Virtual Home Assistant!

"""

Banner_2 = """                                                                                      
IIIIIIIIIIRRRRRRRRRRRRRRRRR   IIIIIIIIII   SSSSSSSSSSSSSSS 
I::::::::IR::::::::::::::::R  I::::::::I SS:::::::::::::::S
I::::::::IR::::::RRRRRR:::::R I::::::::IS:::::SSSSSS::::::S
II::::::IIRR:::::R     R:::::RII::::::IIS:::::S     SSSSSSS
  I::::I    R::::R     R:::::R  I::::I  S:::::S            
  I::::I    R::::R     R:::::R  I::::I  S:::::S            
  I::::I    R::::RRRRRR:::::R   I::::I   S::::SSSS         
  I::::I    R:::::::::::::RR    I::::I    SS::::::SSSSS    
  I::::I    R::::RRRRRR:::::R   I::::I      SSS::::::::SS  
  I::::I    R::::R     R:::::R  I::::I         SSSSSS::::S 
  I::::I    R::::R     R:::::R  I::::I              S:::::S
  I::::I    R::::R     R:::::R  I::::I              S:::::S
II::::::IIRR:::::R     R:::::RII::::::IISSSSSSS     S:::::S
I::::::::IR::::::R     R:::::RI::::::::IS::::::SSSSSS:::::S
I::::::::IR::::::R     R:::::RI::::::::IS:::::::::::::::SS 
IIIIIIIIIIRRRRRRRR     RRRRRRRIIIIIIIIII SSSSSSSSSSSSSSS   

                                Your Virtual Home Assistant! 

"""

Banner_3 = """                                              
 /$$$$$$ /$$$$$$$  /$$$$$$  /$$$$$$ 
|_  $$_/| $$__  $$|_  $$_/ /$$__  $$
  | $$  | $$  \ $$  | $$  | $$  \__/
  | $$  | $$$$$$$/  | $$  |  $$$$$$ 
  | $$  | $$__  $$  | $$   \____  $$
  | $$  | $$  \ $$  | $$   /$$  \ $$
 /$$$$$$| $$  | $$ /$$$$$$|  $$$$$$/
|______/|__/  |__/|______/ \______/ 
                                                                 
        Your Virtual Home Assistant!
"""

Banner_4 = """
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || |  _______     | || |     _____    | || |    _______   | |
| |    |_   _|   | || | |_   __ \    | || |    |_   _|   | || |   /  ___  |  | |
| |      | |     | || |   | |__) |   | || |      | |     | || |  |  (__ \_|  | |
| |      | |     | || |   |  __ /    | || |      | |     | || |   '.___`-.   | |
| |     _| |_    | || |  _| |  \ \_  | || |     _| |_    | || |  |`\____) |  | |
| |    |_____|   | || | |____| |___| | || |    |_____|   | || |  |_______.'  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'               
                                                    
                                                    Your Virtual Home Assistant!
"""

Banner_5 = """
 .S   .S_sSSs     .S    sSSs  
.SS  .SS~YS%%b   .SS   d%%SP  
S%S  S%S   `S%b  S%S  d%S'    
S%S  S%S    S%S  S%S  S%|     
S&S  S%S    d*S  S&S  S&S     
S&S  S&S   .S*S  S&S  Y&Ss    
S&S  S&S_sdSSS   S&S  `S&&S   
S&S  S&S~YSY%b   S&S    `S*S  
S*S  S*S   `S%b  S*S     l*S  
S*S  S*S    S%S  S*S    .S*P  
S*S  S*S    S&S  S*S  sSS*S   
S*S  S*S    SSS  S*S  YSS'    
SP   SP          SP           
Y    Y           Y                                        

Your Virtual Home Assistant!

"""

Banner_6 = """                                               
 8 8888 8 888888888o.    8 8888    d888888o.   
 8 8888 8 8888    `88.   8 8888  .`8888:' `88. 
 8 8888 8 8888     `88   8 8888  8.`8888.   Y8 
 8 8888 8 8888     ,88   8 8888  `8.`8888.     
 8 8888 8 8888.   ,88'   8 8888   `8.`8888.    
 8 8888 8 888888888P'    8 8888    `8.`8888.   
 8 8888 8 8888`8b        8 8888     `8.`8888.  
 8 8888 8 8888 `8b.      8 8888 8b   `8.`8888. 
 8 8888 8 8888   `8b.    8 8888 `8b.  ;8.`8888 
 8 8888 8 8888     `88.  8 8888  `Y8888P ,88P' 

                   Your Virtual Home Assistant!

"""

Banner_7 = """
      ::::::::::: :::::::::  ::::::::::: :::::::: 
         :+:     :+:    :+:     :+:    :+:    :+: 
        +:+     +:+    +:+     +:+    +:+         
       +#+     +#++:++#:      +#+    +#++:++#++   
      +#+     +#+    +#+     +#+           +#+    
     #+#     #+#    #+#     #+#    #+#    #+#     
########### ###    ### ########### ########       
                     
                     Your Virtual Home Assistant!

"""

Banner_8 = """
::::::::::: :::::::::  ::::::::::: ::::::::  
    :+:     :+:    :+:     :+:    :+:    :+: 
    +:+     +:+    +:+     +:+    +:+        
    +#+     +#++:++#:      +#+    +#++:++#++ 
    +#+     +#+    +#+     +#+           +#+ 
    #+#     #+#    #+#     #+#    #+#    #+# 
########### ###    ### ########### ########  
       
                Your Virtual Home Assistant!

"""

Banner_9 = """
'####:'########::'####::'######::
. ##:: ##.... ##:. ##::'##... ##:
: ##:: ##:::: ##:: ##:: ##:::..::
: ##:: ########::: ##::. ######::
: ##:: ##.. ##:::: ##:::..... ##:
: ##:: ##::. ##::: ##::'##::: ##:
'####: ##:::. ##:'####:. ######::
....::..:::::..::....:::......:::

     Your Virtual Home Assistant!
"""

Banner_10 = """
d888888b d8888b. d888888b .d8888. 
  `88'   88  `8D   `88'   88'  YP 
   88    88oobY'    88    `8bo.   
   88    88`8b      88      `Y8b. 
  .88.   88 `88.   .88.   db   8D 
Y888888P 88   YD Y888888P `8888Y' 
                                                                  
     Your Virtual Home Assistant!
"""

Banner_11 = """                                                                  
        *****  *      ***** ***          *****  *       *******    
     ******  *     ******  * **       ******  *       *       ***  
    **   *  *     **   *  *  **      **   *  *       *         **  
   *    *  *     *    *  *   **     *    *  *        **        *   
       *  *          *  *    *          *  *          ***          
      ** **         ** **   *          ** **         ** ***        
      ** **         ** **  *           ** **          *** ***      
    **** **         ** ****          **** **            *** ***    
   * *** **         ** **  ***      * *** **              *** ***  
      ** **         ** **    **        ** **                ** *** 
 **   ** **         *  **    **   **   ** **                 ** ** 
***   *  *             *     **  ***   *  *                   * *  
 ***    *          ****      ***  ***    *          ***        *   
  ******          *  ****    **    ******          *  *********    
    ***          *    **     *       ***          *     *****      
                 *                                *                
                  **                               **                                                                                                                                                                                                                                      

                                     Your Virtual Home Assistant!
"""

Banner_12 = """                                          
        #####  #  ##### /##         #####  # #######    
     ######  / ######  / ##      ######  / /       ###  
    /#   /  / /#   /  /  ##     /#   /  / /         ##  
   /    /  / /    /  /   ##    /    /  /  ##        #   
       /  /      /  /    /         /  /    ###          
      ## ##     ## ##   /         ## ##   ## ###        
      ## ##     ## ##  /          ## ##    ### ###      
    /### ##     ## ###/         /### ##      ### ###    
   / ### ##     ## ##  ###     / ### ##        ### /##  
      ## ##     ## ##    ##       ## ##          #/ /## 
 ##   ## ##     #  ##    ##  ##   ## ##           #/ ## 
###   #  /         /     ## ###   #  /             # /  
 ###    /      /##/      ### ###    /    /##        /   
  #####/      /  ####    ##   #####/    /  ########/    
    ###      /    ##     #      ###    /     #####      
             #                         |                
              ##                        \)              
                                                        
                           Your Virtual Home Assistant!

"""

Banner_13 = """                                          
::::::::::..   ::: .::::::. 
;;;;;;;``;;;;  ;;;;;;`    ` 
[[[ [[[,/[[['  [[['[==/[[[[,
$$$ $$$$$$c    $$$  '''    $
888 888b "88bo,888 88b    dP
MMM MMMM   "W" MMM  "YMmMY" 
 
Your Virtual Home Assistant!

"""

Banner_14 = """                                          
    .....     .       ..      ...         .....     .         ...         
  .d88888Neu. 'L   :~"8888x :"%888x     .d88888Neu. 'L    .x888888hx    : 
  F""""*8888888F  8    8888Xf  8888>    F""""*8888888F   d88888888888hxx  
 *      `"*88*"  X88x. ?8888k  8888X   *      `"*88*"   8" ... `"*8888%`  
  -....    ue=:. '8888L'8888X  '%88X    -....    ue=:. !  "   ` .xnxx.    
         :88N  `  "888X 8888X:xnHH(``          :88N  ` X X   .H8888888%:  
         9888L      ?8~ 8888X X8888            9888L   X 'hn8888888*"   > 
  uzu.   `8888L   -~`   8888> X8888     uzu.   `8888L  X: `*88888%`     ! 
,""888i   ?8888   :H8x  8888  X8888   ,""888i   ?8888  '8h.. ``     ..x8> 
4  9888L   %888>  8888> 888~  X8888   4  9888L   %888>  `88888888888888f  
'  '8888   '88%   48"` '8*~   `8888!` '  '8888   '88%    '%8888888888*"   
     "*8Nu.z*"     ^-==""      `""         "*8Nu.z*"        ^"****""`     
                                                                                                                                                                                                                        
                                             Your Virtual Home Assistant!

"""

Banner_List = [Banner_1, Banner_2, Banner_3, Banner_4, Banner_5, Banner_6, Banner_7, Banner_8, Banner_9, Banner_10, Banner_11, Banner_12, Banner_13, Banner_14]
print(random.choice(Banner_List))

print("""
+--------------------------------------+
|         Selecione uma Opção          |
+--------------------------------------+

+--------------------------------------+
| [1] Conversar com a Iris             |
+--------------------------------------+
| [2] Obter ajuda                      |
+--------------------------------------+
| [3] Créditos                         |
+--------------------------------------+
            """)

try:
	Option = int(input("Opt -->  "))
	
	while Option == 1 or Option == 2 or Option == 3:
		if Option == 1:
			Inst_Recog = Sr.Recognizer()

			Mic_Name = "Microfone (WO Mic Device)"  		#"Microfone (Realtek High Definit" <= Nome do Microfone Padrão do Windows...
			Mic_List = Sr.Microphone.list_microphone_names()

			Initial_Speech = ["Olá, tudo Bem?", "O que posso fazer por você?", "Olá, sou Iris!", "Precisa de ajuda?", "Vamos começar?", "Saudações terráqueo!",
	 		"Vamos lá jovem Padawan!", "Pronto para novas aventuras?", "É novo por aqui? Selecione o menu de ajuda!", "Bem-vindo!", "Você por aqui?", 
	 		"Olá... De novo!", "Gostaria de me conhecer?"]


			Unknown_Speaking = ["Não entendi, você poderia digitar novamente?", "Eu não falo essa língua! =P", "Sério, não entendo você!", "Affff...",
			"Você não acha melhor pedir ajuda?", "Você precisa olhar a tabela de comandos!", "Tente digitar novamente, quem sabe eu te entendo!", 
			"Eu sou um robô, não compreendo sentimentos!", "Posso ligar para seu psicólogo? Você não escreve nada com nada!"]
	 		
			print("Iris -> ",random.choice(Initial_Speech))
			print("Iris ->  Pode falar, eu estou te ouvindo!\n")

			for m, microphone_name in enumerate(Mic_List):
				if microphone_name == Mic_Name:
					device_id = m

			with Sr.Microphone(device_index = device_id, chunk_size = 1024) as source:
				Inst_Recog.adjust_for_ambient_noise(source)

				while True:
					Hearing = Inst_Recog.listen(source)

					Recog_Google_Voice = Inst_Recog.recognize_google(Hearing, language='pt')

					print("Você -> ",Recog_Google_Voice)

					if Recog_Google_Voice == "Olá Íris":
						Voice_Iris = gTTS("Olá, em que posso ajudar?", lang='pt')
						Voice_Iris.save("voz_iris_1.mp3")
						playsound('voz_iris_1.mp3')
						print("Iris ->  Olá, em que posso ajudar?")
		
					elif Recog_Google_Voice == "gostaria de saber como você está":
						Voice_Iris = gTTS("Eu estou bem, e você?", lang='pt')
						Voice_Iris.save("voz_iris_2.mp3")
						playsound('voz_iris_2.mp3')
						print("Iris ->  Eu estou bem, e você?")
					
					elif Recog_Google_Voice == "Eu estou bem obrigado":
						Voice_Iris = gTTS("Por nada", lang='pt')
						Voice_Iris.save("voz_iris_3.mp3")
						playsound('voz_iris_3.mp3')
						print("Iris ->  Por nada!")
					
					elif Recog_Google_Voice == "Iris ligar agora":
						Voice_Iris = gTTS("Ligar pronto!", lang='pt')
						Voice_Iris.save("voz_iris_4.mp3")
						playsound('voz_iris_4.mp3')
						publish.single("cmnd/sonoff/POWER", "ON", hostname="iot.eclipse.org")
						print("Iris ->  Ligar pronto!")
					
					elif Recog_Google_Voice == "Iris desligar agora":
						Voice_Iris = gTTS("Desligar entendido!", lang='pt')
						Voice_Iris.save("voz_iris_5.mp3")
						playsound('voz_iris_5.mp3')
						publish.single("cmnd/sonoff/POWER", "OFF", hostname="iot.eclipse.org")
						print("Iris ->  Desligar entendido!")
					
					elif Recog_Google_Voice == "Obrigado íris":
						Voice_Iris = gTTS("Por nada", lang='pt')
						Voice_Iris.save("voz_iris_6.mp3")
						playsound('voz_iris_6.mp3')
						print("Iris ->  Por nada!")
					
					elif Recog_Google_Voice == "Iris Que horas são":
						Time = datetime.now()
						Voice_Iris = gTTS("Agora são", lang='pt')
						Voice_Iris.save("voz_iris_7.mp3")
						playsound('voz_iris_7.mp3')
						print("Iris ->  Agora são, ", Time.hour,":", Time.minute,":", Time.second)
					
					elif Recog_Google_Voice == "Iris Que dia é hoje":
						Time = datetime.now()
						Voice_Iris = gTTS("Hoje é dia", lang='pt')
						Voice_Iris.save("voz_iris_8.mp3")
						playsound('voz_iris_8.mp3')
						print("Iris ->  Hoje é dia, ", Time.day,"/", Time.month,"/", Time.year)
					
					elif Recog_Google_Voice == "Iris previsão do tempo":
						Voice_Iris = gTTS("Para qual cidade você deseja?", lang='pt')
						Voice_Iris.save("voz_iris_9.mp3")
						playsound('voz_iris_9.mp3')
						Prediction_City = str(input("Iris ->  Para qual cidade você deseja? \nVocê ->  "))
						os.system("python Weather.py " + Prediction_City)
					
					elif Recog_Google_Voice == "Iris pesquisar":
						Voice_Iris = gTTS("O que você gostaria de saber?", lang='pt')
						Voice_Iris.save("voz_iris_10.mp3")
						playsound('voz_iris_10.mp3')
						Key_Words_General = str(input("Iris ->  O que gostaria de saber? \nVocê ->  "))
						webbrowser.open("www.google.com.br/search?q=" + Key_Words_General, autoraise=True)
					
					elif Recog_Google_Voice == "Iris futebol":
						Voice_Iris = gTTS("Qual time você busca?", lang='pt')
						Voice_Iris.save("voz_iris_11.mp3")
						playsound('voz_iris_11.mp3')
						Key_Words_Soccer = str(input("Iris ->  Qual time você busca? \nVocê ->  "))
						webbrowser.open("http://globoesporte.globo.com/futebol/times/" + Key_Words_Soccer, autoraise=True)	
					
					elif Recog_Google_Voice == "Iris definir rota":
						Voice_Iris = gTTS("Onde você está?", lang='pt')
						Voice_Iris.save("voz_iris_12.mp3")
						playsound('voz_iris_12.mp3')
						Key_Words_Starting_Point = str(input("Iris ->  Onde você está? \nVocê ->  "))
						Voice_Iris = gTTS("Para onde você quer ir?", lang='pt')
						Voice_Iris.save("voz_iris_13.mp3")
						playsound('voz_iris_13.mp3')
						Key_Words_Point_Of_Arrival = str(input("Iris ->  Para onde você quer ir? \nVocê ->  "))
						webbrowser.open("www.google.com.br/maps/dir/%s/%s" % (Key_Words_Starting_Point, Key_Words_Point_Of_Arrival))

					elif Recog_Google_Voice == "Iris programar tempo para ligar":
						Voice_Iris = gTTS("Em quanto tempo (em minutos) você deseja ligar?", lang='pt')
						Voice_Iris.save("voz_iris_14.mp3")
						playsound('voz_iris_14.mp3') 
						Count_Time_On = float(input("Iris ->  Em quanto tempo (em minutos) você deseja ligar? \nVocê ->  "))	
						time.sleep(Count_Time_On*60)
						publish.single("cmnd/sonoff/POWER", "ON", hostname="iot.eclipse.org")
						print("Iris ->  Ligado!")  
					
					elif Recog_Google_Voice == "Iris programar tempo para desligar":
						Voice_Iris = gTTS("Em quanto tempo (em minutos) você deseja desligar?", lang='pt')
						Voice_Iris.save("voz_iris_15.mp3")
						playsound('voz_iris_15.mp3') 
						Count_Time_Off = float(input("Iris ->  Em quanto tempo (em minutos) você deseja desligar? \nVocê ->  "))
						time.sleep(Count_Time_Off*60)
						publish.single("cmnd/sonoff/POWER", "OFF", hostname="iot.eclipse.org")
						print("Iris ->  Desligado!")
					
					elif Recog_Google_Voice == "Iris reconhecimento escrito":
						Voice_Iris = gTTS("Pode falar, eu estou te ouvindo!E irei escrever para você!", lang='pt')
						Voice_Iris.save("voz_iris_16.mp3")
						playsound('voz_iris_16.mp3')

						Hearing_To_Read = Inst_Recog.listen(source)
						Recog_Google_To_Read = Inst_Recog.recognize_google(Hearing_To_Read, language='pt')
						print("Iris ->  Pode falar, eu estou te ouvindo!E irei escrever para você!")
						print("Você -> ", Recog_Google_To_Read)
						Recog_Google_Reading = open('Reconhecimento_Escrito.txt', 'w')
						Recog_Google_Reading.write(Recog_Google_To_Read)
						Recog_Google_Reading.close()

					elif Recog_Google_Voice == "Quem é você":
						Voice_Iris = gTTS("Eu sou Iris, sua assistente virtual residencial!", lang='pt')
						Voice_Iris.save("voz_iris_17.mp3")
						playsound('voz_iris_17.mp3')
						print("Iris ->  Eu sou Iris, sua assistente virtual residencial!")

					elif Recog_Google_Voice == "Você é muito inteligente":
						Voice_Iris = gTTS("Obrigada, eu tento ser!", lang='pt')
						Voice_Iris.save("voz_iris_18.mp3")
						playsound('voz_iris_18.mp3')
						print("Iris ->  Obrigada, eu tento ser!")

					elif Recog_Google_Voice == "Iris cotação de moedas":
						Voice_Iris = gTTS("Qual moeda você deseja cotar?", lang='pt')
						Voice_Iris.save("voz_iris_19.mp3")
						playsound('voz_iris_19.mp3')
						Key_Words_Coin = str(input("Iris ->  Qual moeda você deseja cotar? \nVocê ->  "))
						if Key_Words_Coin == "Dólar Americano":
							Voice_Iris = gTTS("O valor do Dólar Americano é,", lang='pt')
							Voice_Iris.save("voz_iris_20.mp3")
							playsound('voz_iris_20.mp3')
							print("Iris ->  O valor do Dólar Americano é,")

							webbrowser.open("https://www.melhorcambio.com/dolar-hoje", autoraise=True)
 
						elif Key_Words_Coin == "Dólar Canadense":
							Voice_Iris = gTTS("O valor do Dólar Canadense é,", lang='pt')
							Voice_Iris.save("voz_iris_21.mp3")
							playsound('voz_iris_21.mp3')
							print("Iris ->  O valor do Dólar Canadense é,")

							webbrowser.open("https://www.melhorcambio.com/dolar-canadense-hoje", autoraise=True)

						elif Key_Words_Coin == "Dólar Australiano":
							Voice_Iris = gTTS("O valor do Dólar Australiano é,", lang='pt')
							Voice_Iris.save("voz_iris_22.mp3")
							playsound('voz_iris_22.mp3')
							print("Iris ->  O valor do Dólar Australiano é,")

							webbrowser.open("https://www.melhorcambio.com/dolar-australiano-hoje", autoraise=True)

						elif Key_Words_Coin == "Euro":
							Voice_Iris = gTTS("O valor do Euro é,", lang='pt')
							Voice_Iris.save("voz_iris_23.mp3")
							playsound('voz_iris_23.mp3')
							print("Iris ->  O valor do Euro é,")

							webbrowser.open("https://www.melhorcambio.com/euro-hoje", autoraise=True)

						elif Key_Words_Coin == "Libra":
							Voice_Iris = gTTS("O valor da Libra é,", lang='pt')
							Voice_Iris.save("voz_iris_24.mp3")
							playsound('voz_iris_24.mp3')
							print("Iris ->  O valor da Libra é,")

							webbrowser.open("https://www.melhorcambio.com/libra-hoje", autoraise=True)
							
						else:
							webbrowser.open("https://economia.uol.com.br/cotacoes/cambio/", autoraise=True)

					elif Recog_Google_Voice == "Iris bolsa de valores":
						Voice_Iris = gTTS("Abrindo mercado de ações atual!", lang='pt')
						Voice_Iris.save("voz_iris_25.mp3")
						playsound('voz_iris_25.mp3')
						print("Iris ->  Abrindo mercado de ações atual!")
						
						webbrowser.open("http://www.infomoney.com.br/mercados/acoes-e-indices", autoraise=True)

					elif Recog_Google_Voice == "Iris notícias":
						Voice_Iris = gTTS("Abrindo as útlimas notícias de hoje!", lang='pt')
						Voice_Iris.save("voz_iris_26.mp3")
						playsound('voz_iris_26.mp3')
						print("Iris ->  Abrindo as útlimas notícias de hoje!")

						webbrowser.open("http://g1.globo.com/ultimas-noticias.html", autoraise=True)

					elif Recog_Google_Voice == "Até logo íris":
						Voice_Iris = gTTS("Nos vemos em breve!", lang='pt')
						Voice_Iris.save("voz_iris_27.mp3")
						playsound('voz_iris_27.mp3')
						print("Iris ->  Nos vemos em breve!")
						break
 
					elif Recog_Google_Voice == "Iris enviar e-mail":
						Send_From = 'iris.assistant2017@gmail.com'
						Password  = 'Iris2017@#%&*'

						Voice_Iris = gTTS("Para quem você deseja enviar?", lang='pt')
						Voice_Iris.save("voz_iris_28.mp3")
						playsound('voz_iris_28.mp3')
						Send_To = str(input("Iris -> Para quem você deseja enviar? (Digite o email destinatário) \nVocê -> "))

						#Send_To_Refact = [Send_To]
						
						Voice_Iris = gTTS("Qual o assunto?", lang='pt')
						Voice_Iris.save("voz_iris_29.mp3")
						playsound('voz_iris_29.mp3')
						Subject = str(input("Iris -> Qual o assunto? \nVocê -> "))

						Voice_Iris = gTTS("Qual o escopo do email?", lang='pt')
						Voice_Iris.save("voz_iris_30.mp3")
						playsound('voz_iris_30.mp3')
						Compose_Email = str(input("Iris -> Qual o escopo do email? \nVocê -> "))

#						Voice_Iris = gTTS("Deseja anexar algum arquivo?", lang='pt')
#						Voice_Iris.save("voz_iris_31.mp3")
#						playsound('voz_iris_31.mp3')
#						Attachment_Option = str(input("Iris -> Deseja anexar algum arquivo? [S/N] \nVocê -> "))
#
#						if Attachment_Option == "S":
#							Voice_Iris = gTTS("Selecione o arquivo para ser anexado!", lang='pt')
#							Voice_Iris.save("voz_iris_32.mp3")
#							playsound('voz_iris_32.mp3')
#
#							Attachment = str(input("Iris -> Selecione o arquivo para ser anexado! \nVocê -> "))
#
#						elif Attachment_Option == "N":
#
#							Attachment = None
#
#						else:
#							print("Iris -> Escolha entre as opções S(SIM) ou N(NÃO)!")
#							Attachment_Option = str(input("Iris -> Deseja anexar algum arquivo? [S/N] \nVocê -> "))

						Send_Email_Settings(Send_From, Password, Send_To, Subject, Compose_Email) #ENVIAR COM PYTHON 2.7 ou 3.5

					elif Recog_Google_Voice == "Iris criptografia":
						Voice_Iris = gTTS("Você deseja Criptografar um texto ou um arquivo?", lang='pt')
						Voice_Iris.save('voz_iris_33.mp3')
						playsound('voz_iris_33.mp3')
						
						Cript_Option = str(input("Iris ->  Você deseja Criptografar um texto ou um arquivo? [T/A] \nVocê ->  "))

						if Cript_Option == "T" or Cript_Option == "t" or Cript_Option == "Texto" or Cript_Option == "texto":
							Voice_Iris = gTTS("Digite o texto para ser Criptografado!", lang='pt')
							Voice_Iris.save('voz_iris_34.mp3')
							playsound('voz_iris_34.mp3')

							Cript_Text_Plain = str(input("Iris ->  Digite o texto para ser Criptografado! \nVocê ->  "))
							
							Cript_Text_Write = open('Cript_Text_Plain_Write.txt', 'w')
							Cript_Text_Write.write(Cript_Text_Plain)
							Cript_Text_Write.close()

							Voice_Iris = gTTS("Digite uma senha como chave criptográfica!", lang='pt')
							Voice_Iris.save('voz_iris_35.mp3')
							playsound('voz_iris_35.mp3')

							os.system("gpg --cipher-algo AES256 --symmetric Cript_Text_Plain_Write.txt")

							print("Iris ->  Seu texto foi Criptografado com Sucesso! (AES256)\n")
							os.system("type Cript_Text_Plain_Write.txt.gpg" or "cat Cript_Text_Plain_Write.txt.gpg")

						elif Cript_Option == "A" or Cript_Option == "a" or Cript_Option == "Arquivo" or Cript_Option == "arquivo":
							Voice_Iris = gTTS("Selecione o arquivo para ser Criptografado!", lang='pt')
							Voice_Iris.save('voz_iris_36.mp3')
							playsound('voz_iris_36.mp3')

							Cript_File_Plain = input("Iris ->  Selecione o arquivo para ser Criptografado! \nVocê ->  ")

							Voice_Iris = gTTS("Digite uma senha como chave criptográfica!", lang='pt')
							Voice_Iris.save('voz_iris_37.mp3')
							playsound('voz_iris_37.mp3')

							os.system("gpg --cipher-algo AES256 --symmetric " + Cript_File_Plain)

							print("Iris ->  Seu arquivo foi Criptografado com Sucesso! (AES256)\n")
							os.system("type %s.gpg" % Cript_File_Plain or "cat %s.gpg" % Cript_File_Plain)
							print("\n")

						else:
							print("Iris -> Escolha entre as opções T(TEXTO) ou A(ARQUIVO)!")
							Cript_Option = str(input("Iris ->  Você deseja Criptografar um texto ou um arquivo? [T/A] \nVocê ->  "))

					elif Recog_Google_Voice == "Iris descriptografia":
						Voice_Iris = gTTS("Você deseja Descriptografar um texto ou um arquivo?", lang='pt')
						Voice_Iris.save('voz_iris_38.mp3')
						playsound('voz_iris_38.mp3')
						Cript_Option = str(input("Iris ->  Você deseja Descriptografar um texto ou um arquivo? [T/A] \nVocê ->  "))

						if Cript_Option == "T" or Cript_Option == "t" or Cript_Option == "Texto" or Cript_Option == "texto":
							Voice_Iris = gTTS("Seu texto digitado anteriormente será Descriptografado!", lang='pt')
							Voice_Iris.save('voz_iris_39.mp3')
							playsound('voz_iris_39.mp3')

							os.system("gpg -d Cript_Text_Plain_Write.txt.gpg ")

							print("\n\nIris ->  Seu texto foi Descriptografado com Sucesso! (AES256)\n")

						elif Cript_Option == "A" or Cript_Option == "a" or Cript_Option == "Arquivo" or Cript_Option == "arquivo":
							Voice_Iris = gTTS("Selecione o arquivo para ser Descriptografado!", lang='pt')
							Voice_Iris.save('voz_iris_40.mp3')
							playsound('voz_iris_40.mp3')

							Cript_File_Cipher = str(input("Iris ->  Selecione o arquivo para ser Descriptografado! \nVocê ->  "))

							os.system("gpg -d " + Cript_File_Cipher)

							print("\nIris ->  Seu arquivo foi Descriptografado com Sucesso! (AES256)\n")

						else:
							print("Iris ->  Escolha entre as opções T(TEXTO) ou A(ARQUIVO)!")
							Cript_Option = str(input("Iris ->  Você deseja Descriptografar um texto ou um arquivo? [T/A] \nVocê ->  "))

					elif Recog_Google_Voice == "Iris devocional diário":
						Devotional_List = ["http://www.devocionaldiario.com.br", "http://www.maxlucado.com.br/devocional-diario/",
						"http://ultimato.com.br/sites/devocional-diaria/", "http://www.devocionaisdiarios.com"]

						Voice_Iris = gTTS("Abrindo o devocional de hoje!", lang='pt')
						Voice_Iris.save("voz_iris_41.mp3")
						playsound('voz_iris_41.mp3')
						print("Iris ->  Abrindo o devocional de hoje!")

						webbrowser.open(random.choice(Devotional_List), autoraise=True)

					elif Recog_Google_Voice == "Iris Bíblia online":
						Bible_List = ["https://www.bibliaonline.com.br", "https://www.bibliaon.com"]

						Voice_Iris = gTTS("Abrindo bíblia online!", lang='pt')
						Voice_Iris.save("voz_iris_42.mp3")
						playsound('voz_iris_42.mp3')
						print("Iris ->  Abrindo bíblia online!")

						webbrowser.open(random.choice(Bible_List), autoraise=True)

					elif Recog_Google_Voice == "Iris ativar câmera":
						Voice_Iris = gTTS("Iniciando captura de vídeo!", lang='pt')
						Voice_Iris.save("voz_iris_43.mp3")
						playsound('voz_iris_43.mp3')
						print("Iris ->  Iniciando captura de vídeo!")

						Capture = cv2.VideoCapture(0)

						while(True):
							Ret, Frame = Capture.read()

							cv2.imshow('Iris Video Stream', Frame)
							if cv2.waitKey(1) & 0xFF == ord('q'):
								break

						Capture.release()
						cv2.destroyAllWindows()

					elif Recog_Google_Voice == "Iris pedir comida":
						Voice_Iris = gTTS("Digite sua cidade e estado!", lang='pt')
						Voice_Iris.save("voz_iris_44.mp3")
						playsound('voz_iris_44.mp3')
						print("Iris ->  Digite sua cidade e estado!")

						City_State_Food = input("Iris ->  Digite sua cidade e estado! (Exemplo: maringa-pr ou sao-jose-dos-pinhais-pr) \nVocê ->  ")

						webbrowser.open("https://www.ifood.com.br/delivery/" + City_State_Food, autoraise=True)

					else:
						print("Iris -> ",random.choice(Unknown_Speaking))
						Recog_Google_Voice = input("Você ->  ")

						Hearing = Inst_Recog.listen(source)
						Recog_Google_Voice = Inst_Recog.recognize_google(Hearing, language='pt')
						
		elif Option == 2:

			print("""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                        SEJA BEM-VINDO AO MENU DE AJUDA!                                        |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                                                                |
|IRIS É UMA ASSISTENTE VIRTUAL RESIDENCIAL, COM ELA VOCÊ PODE FAZER ACIONAMENTOS DE ELETRODOMÉSTICOS, LÂMPADAS   |
|ENTRE OUTROS OBJETOS ELÉTRICOS QUE SE ENCONTRAM DENTRO DE CASA APENAS POR COMANDOS DE VOZ. SUA FAIXA DE OPERAÇÃO|
|DE TENSÃO FUNCIONA ENTRE 90-250V AC ENTRE 50/60Hz E COM CORRENTE MÁXIMA DE 10A. IRIS AINDA É CAPAZ DE RECONHECER|
|OUTROS COMANDOS PRÉ-CONFIGURADOS QUE ADICIONAM FUNCIONALIDADES À ELA COMO VOCÊ PODE VER Á SEGUIR:               |
|                                                                                                                |
|=> COMANDOS CONFIGURADOS:                                                                                       |
|   => "OLÁ IRIS"                                   |	=> "IRIS BOLSA DE VALORES"                               |
|   => "GOSTARIA DE SABER COMO VOCÊ ESTÁ"           |	=> "IRIS PESQUISAR"                                      |
|   => "EU ESTOU BEM OBRIGADO"                      |	=> "IRIS FUTEBOL"                                        |
|   => "QUEM É VOCÊ"                                |   => "IRIS LIGAR AGORA"                                    |
|   => "VOCÊ É MUITO INTELIGENTE"                   |   => "IRIS DESLIGAR AGORA"                                 |
|   => "OBRIGADO IRIS"                              |	=> "IRIS PROGRAMAR TEMPO PARA LIGAR"                     |
|   => "ATÉ LOGO IRIS"                              |	=> "IRIS PROGRAMAR TEMPO PARA DESLIGAR"                  |
|   => "IRIS PREVISÃO DO TEMPO"                     |	=> "IRIS RECONHECIMENTO ESCRITO"                         |
|   => "IRIS QUE HORAS SÃO"                         |   => "IRIS NOTÍCIAS"                                       |
|   => "IRIS QUE DIA É HOJE"                        |   => "IRIS ENVIAR EMAIL"                                   |
|   => "IRIS DEFINIR ROTA"                          |   => "IRIS CRIPTOGRAFIA"                                   |
|   => "IRIS COTAÇÃO DE MOEDAS"                     |   => "IRIS DESCRIPTOGRAFIA"                                |
|      => "DOLAR AMERICANO"                         |   => "IRIS DEVOCIONAL DIÁRIO"                              |
|      => "DOLAR CANADENSE"                         |   => "IRIS BÍBLIA ONLINE"                                  |
|      => "DOLAR AUSTRALIANO"                       |   => "IRIS ATIVAR CÂMERA"                                  |
|      => "EURO"                                    |   => "IRIS PEDIR COMIDA"                                   |
|      => "LIBRA"                                   |   => "FUTURA AGENDA E LEMBRETES" (BREVE)                   |
|      => "VAZIO"                                   |   => "FUTURA CALCULADORA PARA ENGENHARIA" (BREVE)          |
|                                                                                                                |
|=> CONEXÃO DO HARDWARE:                                                                                         |
|   => A CONEXÃO DO HARDWARE SONOFF É MUITO SIMPLES, BASTA COLOCAR A ENTRADA (input) EM QUALQUER TOMADA          |
|      (QUE FUNCIONE ENTRE A FAIXA DE OPERAÇÃO DETERMINADA) E A SAÍDA (output) NO OBJETO ELÉTRICO QUE VOCÊ       |
|      DESEJA LIGAR.                                                                                             |
|                                                                                                                |
|=> CONEXÃO DO WIFI:                                                                                             |
|   => PARA REALIZAR A CONEXÃO DO SONOFF COM SUA REDE WIFI, BASTA BAIXAR O APLICATIVO "ESP8266 SmartConfig"      |
|      NA PLAYSTORE OU APPLE STORE, COLOCAR A SENHA DE SUA REDE INTERNA NA CAIXA DE OPÇÃO "password" QUE IRÁ     |
|      APARECER EM SEU SMARTPHONE E SIMULTANEAMENTE PRESSIONAR O BOTÃO ACIMA DO SONOFF DE FORMA BREVE 3 VEZES.   |
|                                                                                                                |
|      OBS:                                                                                                      |
|      => PARA VERIFICAR SE SEU SONOFF ESTÁ CONECTADO À SUA REDE, VOCÊ PODE BAIXAR O APLICATIVO "FING" NA        |
|         PLAYSOTRE OU APPLE STORE, CONECTAR COM SEU WIFI E REALIZAR UMA VARREDURA DE SUA REDE INTERNA. SE O     |
|         SONOFF ESTIVER CONECTADO COM SUA REDE, ALÉM DOS OUTROS DISPOSITIVOS CONECTADOS AO SEU WIFI, IRÁ        |
|         APARECER ALGO PARECIDO COM O NOME "Light  Espressif" E O ENDEREÇO IP QUE O SONOFF ASSUMIU, ALGO COMO   |
|         "192.168.25.4" OU "10.0.0.115" DEPENDENDO DO SEU PROVEDOR DE INTERNET.                                 |
|                                                                                                                |
|=> CONEXÃO DO MICROFONE:                                                                                        |
|   => PARA UTILIZAR O MICROFONE PADRÃO OU EXTERNO É NECESSÁRIO EXECUTAR O PROGRAMA "Iris_Mic_List.py". QUANDO   |
|      EXECUTADO, O PROGRAMA IRÁ MOSTRAR UMA LISTA DE ENTRADAS E SAÍDAS DE SOM DISPONÍVEIS EM SEU COMPUTADOR.    |
|      PARA UTILIZAR O MICROFONE DESEJADO, BASTA COPIAR O NOME DO MICROFONE MOSTRADO NA LISTA E COLOCAR NA       |
|      VARIÁVEL DO PROGRAMA PRINCIPAL "Mic_Name". O PROJETO PADRÃO UTILIZA O SMARTPHONE COMO MICROFONE PARA O    |
|      RECONHECIMENTO DE VOZ. PARA ISSO, É UTILIZADO O PROGRAMA "WO Mic". PARA UTILIZAR DESSA FORMA, BASTA BAIXAR|
|      O "WO Mic" NA PLAYSTORE OU APPLESTORE E INSTALAR. TAMBÉM DEVE SER BAIXADO O "WO Mic" EM SEU COMPUTADOR,   |
|      PESQUISE NO GOOGLE E BAIXE O "WO Mic" E O "WO Mic Client". PARA FAZER A CONEXÃO, ABRA O APLICATIVO EM SEU |
|      SMARTPHONE, VÁ EM CONFIGURAÇÕES, SELECIONE O TIPO DE TRANSPORTE DE DADOS (NESSE CASO, WIFI), DEIXE AS     |
|      PORTAS PADRÕES E PRESSIONE "START". LOGO EM SEGUIDA IRÁ APARECER UM NÚMERO DE IP. ABRA O "WO Mic Client"  |
|      DO SEU COMPUTADOR, VÁ EM OPÇÕES, PORTS, E CONFIGURE AS PORTAS EM CONFORMIDADE COM AS PORTAS DO APLICATIVO |
|      DO SMARTPHONE. DEPOIS VÁ EM CONEXÃO, CONECTAR, SELECIONE O MODO DE RECEPÇÃO WIFI E COLOQUE O ENDEREÇO DE  |
|      IP QUE APARECEU EM SEU SMARTPHONE. CASO TUDO ESTEJA CORRETO, SEU COMPUTADOR JÁ ESTARÁ RECEBENDO AUDIOS EM |
|      TEMPO REAL E RECONHECENDO SEU SMARTPHONE COMO MICROFONE.                                                  |
|                                                                                                                |
|=> PARA CONVERSAR COM IRIS, SELECIONE A OPÇÃO 1.                                                                |
|                                                                                                                |
|=> PARA OBTER AJUDA, SELECIONE A OPÇÃO 2.                                                                       |
|                                                                                                                |
|=> PARA VER OS CRÉDITOS, SELECIONE A OPÇÃO 3.                                                                   |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                        SEJA BEM-VINDO AO MENU DE AJUDA!                                        |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")
			break

		elif Option == 3:
			Credit_1 = """
 .S_SsS_S.    .S_sSSs           .S    S.    .S_sSSs     .S       S.     sSSSSs    sSSs   .S_sSSs
.SS~S*S~SS.  .SS~YS%%b         .SS    SS.  .SS~YS%%b   .SS       SS.   d%%%%SP   d%%SP  .SS~YS%%b
S%S `Y' S%S  S%S   `S%b        S%S    S&S  S%S   `S%b  S%S       S%S  d%S'      d%S'    S%S   `S%b
S%S     S%S  S%S    S%S        S%S    d*S  S%S    S%S  S%S       S%S  S%S       S%S     S%S    S%S
S%S     S%S  S%S    d*S        S&S   .S*S  S%S    d*S  S&S       S&S  S&S       S&S     S%S    d*S
S&S     S&S  S&S   .S*S        S&S_sdSSS   S&S   .S*S  S&S       S&S  S&S       S&S_Ss  S&S   .S*S
S&S     S&S  S&S_sdSSS         S&S~YSSY%b  S&S_sdSSS   S&S       S&S  S&S       S&S~SP  S&S_sdSSS
S&S     S&S  S&S~YSY%b         S&S    `S%  S&S~YSY%b   S&S       S&S  S&S sSSs  S&S     S&S~YSY%b
S*S     S*S  S*S   `S%b        S*S     S%  S*S   `S%b  S*b       d*S  S*b `S%%  S*b     S*S   `S%b
S*S     S*S  S*S    S%S        S*S     S&  S*S    S%S  S*S.     .S*S  S*S   S%  S*S.    S*S    S%S
S*S     S*S  S*S    S&S        S*S     S&  S*S    S&S   SSSbs_sdSSS    SS_sSSS   SSSbs  S*S    S&S
SSS     S*S  S*S    SSS   SS   S*S     SS  S*S    SSS    YSSP~YSSY      Y~YSSY    YSSP  S*S    SSS
        SP   SP          S%%S  SP          SP                                           SP
        Y    Y            SS   Y           Y                                            Y

                                                                                    by: @Mr.Kr¥g€₹
                                                                                    by: @Mr.Bruno
                                                                                    by: @Mr.Pedro
"""

			Credit_2 = """

 .S_SsS_S.    .S_sSSs           .S_SSSs     .S_sSSs     .S       S.    .S_sSSs      sSSs_sSSs    
.SS~S*S~SS.  .SS~YS%%b         .SS~SSSSS   .SS~YS%%b   .SS       SS.  .SS~YS%%b    d%%SP~YS%%b   
S%S `Y' S%S  S%S   `S%b        S%S   SSSS  S%S   `S%b  S%S       S%S  S%S   `S%b  d%S'     `S%b  
S%S     S%S  S%S    S%S        S%S    S%S  S%S    S%S  S%S       S%S  S%S    S%S  S%S       S%S  
S%S     S%S  S%S    d*S        S%S SSSS%P  S%S    d*S  S&S       S&S  S%S    S&S  S&S       S&S  
S&S     S&S  S&S   .S*S        S&S  SSSY   S&S   .S*S  S&S       S&S  S&S    S&S  S&S       S&S  
S&S     S&S  S&S_sdSSS         S&S    S&S  S&S_sdSSS   S&S       S&S  S&S    S&S  S&S       S&S  
S&S     S&S  S&S~YSY%b         S&S    S&S  S&S~YSY%b   S&S       S&S  S&S    S&S  S&S       S&S  
S*S     S*S  S*S   `S%b        S*S    S&S  S*S   `S%b  S*b       d*S  S*S    S*S  S*b       d*S  
S*S     S*S  S*S    S%S        S*S    S*S  S*S    S%S  S*S.     .S*S  S*S    S*S  S*S.     .S*S  
S*S     S*S  S*S    S&S        S*S SSSSP   S*S    S&S   SSSbs_sdSSS   S*S    S*S   SSSbs_sdSSS   
SSS     S*S  S*S    SSS   SS   S*S  SSY    S*S    SSS    YSSP~YSSY    S*S    SSS    YSSP~YSSY    
        SP   SP          S%%S  SP          SP                         SP                         
        Y    Y            SS   Y           Y                          Y                          
                                                                                                 
                                                                                  by: @Mr.Bruno
                                                                                  by: @Mr.Pedro
                                                                                  by: @Mr.Kr¥g€₹
                                                                                    
"""

			Credit_3 = """

 .S_SsS_S.    .S_sSSs           .S_sSSs      sSSs   .S_sSSs     .S_sSSs      sSSs_sSSs    
.SS~S*S~SS.  .SS~YS%%b         .SS~YS%%b    d%%SP  .SS~YS%%b   .SS~YS%%b    d%%SP~YS%%b   
S%S `Y' S%S  S%S   `S%b        S%S   `S%b  d%S'    S%S   `S%b  S%S   `S%b  d%S'     `S%b  
S%S     S%S  S%S    S%S        S%S    S%S  S%S     S%S    S%S  S%S    S%S  S%S       S%S  
S%S     S%S  S%S    d*S        S%S    d*S  S&S     S%S    S&S  S%S    d*S  S&S       S&S  
S&S     S&S  S&S   .S*S        S&S   .S*S  S&S_Ss  S&S    S&S  S&S   .S*S  S&S       S&S  
S&S     S&S  S&S_sdSSS         S&S_sdSSS   S&S~SP  S&S    S&S  S&S_sdSSS   S&S       S&S  
S&S     S&S  S&S~YSY%b         S&S~YSSY    S&S     S&S    S&S  S&S~YSY%b   S&S       S&S  
S*S     S*S  S*S   `S%b        S*S         S*b     S*S    d*S  S*S   `S%b  S*b       d*S  
S*S     S*S  S*S    S%S        S*S         S*S.    S*S   .S*S  S*S    S%S  S*S.     .S*S  
S*S     S*S  S*S    S&S        S*S          SSSbs  S*S_sdSSS   S*S    S&S   SSSbs_sdSSS   
SSS     S*S  S*S    SSS   SS   S*S           YSSP  SSS~YSSY    S*S    SSS    YSSP~YSSY    
        SP   SP          S%%S  SP                              SP                         
        Y    Y            SS   Y                               Y                          
                                                                                          
                                                                           by: @Mr.Pedro
                                                                           by: @Mr.Kr¥g€₹
                                                                           by: @Mr.Bruno

"""
			Credit_List = [Credit_1, Credit_2, Credit_3]
			print(random.choice(Credit_List))
			break

	while Option not in range(1,4):
		print("\n[!] Insira um valor contido na opção do menu.")
		break
		#Option = int(input("\nOpt -->  "))
		#if Option in range(1,4):
		#	break

except KeyboardInterrupt:
    print('\n[!] Saindo...')
except ValueError:
    print('\n[!] Insira um valor correto.')
#except Range_Option_Menu_Error():
#	print('\n[!] Insira um valor de opção correta.')
#	Option = int(input("Opt -->  "))
#except TimeoutError:
#	print('\n[!] Continue falando!')
#	Hearing = Inst_Recog.listen(source)