# IrisVHA

IrisVHA é uma Assistente Virtual Residencial com interação por voz. Com ela é possível realizar acionamentos de eletrodomésticos, lâmpadas e outros tipos de objetos eletro-eletrônicos que são encontrados dentro de uma residência comum. Sua faixa de operação de tensão funciona entre 90-250V AC com uma faixa de frequência entre 50/60Hz e com corrente máxima de 10A. Iris ainda é capaz de reconhecer comandos de voz pré-configurados que adicionam funcionalidades à ela como é demonstrado na tabela á seguir:

COMANDOS DE AÇÕES                     | COMANDOS DE DIÁLOGO     
------------------------------------- | -------------------------------------
Iris ligar agora!                     | Olá Iris!                            
Iris desligar agora!                  | Gostaria de saber como você está?     
Iris que horas são?                   | Eu estou bem obrigado!                 
Iris que dia é hoje?                  | Obrigado Iris...                       
Iris previsão do tempo!               | Quem é você?                          
Iris pesquisar!                       | Você é muito inteligente...           
Iris futebol!                         | Até logo Iris...                       
Iris definir rota!                    |                                       
Iris programar tempo para ligar!      |                                        
Iris programar tempo para desligar!   |                                       
Iris reconhecimento escrito!          |                                       
Iris cotação de moedas!               |                                       
Dólar Americano                       |                                       
Dólar Canadense                       |                                        
Dólar Australiano                     |                                       
Euro                                  |                                       
Libra                                 |                                       
Iris bolsa de valores!                |                                       
Iris notícias!                        |                                       
Iris enviar email!                    |                                       
Iris criptografia!                    |                                       
Iris descriptografia!                 |                                      
Iris devocional diário!               |                                      
Iris bíblia online!                   |                                      
Iris ativar câmera!                   |                                       
Iris pedir comida!                    |   
                                                      

## Instalação e Configuração do Hardware (se houver)

* **SONOFF**: Para realizar os acionamentos, Iris se utiliza de um dispositivo chamado Sonoff. Nele contém um dispositivo eletrônico chamado ESP8266 que possibilita uma comunicação WiFi entre ele e o computador. Originalmente o Sonoff realiza os acionamentos via aplicativo de fábrica disponível na PlayStore chamado "eWeLink", dessa forma não seria possível estabelecer uma comunicação entre Iris e o Sonoff. Então, foi necessário realizar a alteração do firmware para que essa comunicação fosse possível. O firmware utiliza o protocolo de comunicação MQTT (M2M), cujo qual se utiliza de um Broker (servidor) que recebe as requisições chamadas de Publish (publicações) dos Subscribers (clientes) através de Topics (tópicos) que são endereços específicos publicados pelos clientes e direcionados para comunicação com o Broker.: 

  O firmware está disponível em: https://github.com/arendst/Sonoff-Tasmota 

  O Sonoff está disponível em: https://www.amazon.com/Sonoff-Wireless-Remote-Switch-Automation/dp/B01IF1H1TI

  Vídeo para instalação do firmware: https://www.youtube.com/watch?v=n4MDRm2yAJg

* **CONEXÃO DO HARDWARE**: Para conectar o Sonoff é bem simples, basta colocar a entrada (input) em qualquer tomada (que atenda a faixa de operação indicada) e a saída (output) no objeto eletro-eletrônico que se deseja acionar.                                             

* **CONEXÃO DO WIFI**: Para realizar a conexão do WiFi, basta baixar o aplicativo "ESP8266 SmartConfig" na PlayStore ou AppleStore e colocar a senha de sua rede interna na caixa de opção "password" que irá aparecer no smartphone e simultaneamente pressionar o botão acima do sonoff de forma breve 3 vezes.

   OBS: Para verificar se o Sonoff está conectado à rede, basta baixar aplicativo "Fing" na PlayStore ou na AppleStore, conectar com seu WiFi e realizar uma varredura da rede interna. Se o Sonoff estiver conectado na rede, além dos outros dispositivos conectados no WiFi, irá aparecer algo parecido com o nome "Light Espressif" juntamente com o endereço de IP que o Sonoff assumiu, algo como "192.168.25.10"
ou "10.0.0.115" dependendo do seu provedor de internet.
   Além disso, o firmware permite que uma página de controle Web seja criada assim que o Sonoff é conectado a rede, então para acessá-la, basta conectar seu Sonoff e verificar o endereço de IP que ele assumiu. Depois, abra um navegador qualquer e digite o IP do Sonoff. Logo irá aparecer uma página para controlar o Sonoff via Web.

## Instalação e Configuração do Software

* **BAIXAR O PROGRAMA**: Para baixar o código, aperte o botão de download ou clone via terminal ou cmd.:

 ```git
 git clone https://github.com/MrKruger/IRIS-VIRTUAL-HOME-ASSISTANT.git
 ```

* **BAIXAR O PYTHON**: Baixe e instale a última versão da linguagem python pelo site oficial. Não se esqueça de deixar a opção "Add Python 3.6 to PATH" marcada.: https://www.python.org/downloads/.


   OBS: Iris tem uma função para enviar emails com o módulo SMTP cujo qual funcionou apenas nas versões do Python 2.7 e 3.5 (de acordo com testes realizados por mim), dessa forma, se a opção de enviar emails for desejada, é indicado que o usuário impreterívelmente baixe a versão do Python 3.5.

* **BAIXAR OS MÓDULOS NECESSÁRIOS**: Para que Iris funcione corretamente é necessário instalar os móduclos adicionais que estão no arquivo Requirements.txt. Para fazer isso você precisa abrir o terminal ou cmd na pasta aonde se encontra o arquivo e digitar o seguinte comando.:

 ```py
 pip install -r Requirements.txt
 ```

* **CONFIGURAR O MICROFONE**: Iris precisa de um microfone para poder ouvir e entender os comandos de voz. Como existem várias entradas e saídas de áudio no computador, é necessário que o usuário selecione qual microfone (entrada de áudio) gostaria de usar. Assim, se torna necessário executar um programa para listar as entradas e saídas de áudio disponíveis no computador aonde Iris está sendo executada. Após a executação do código, será mostrado a lista de microfones disponíveis no computador, juntamente com as saídas de áudio, então o usuário precisa copiar qual microfone deseja utilizar e colar na linha de código do programa principal "Mic_Name = "NOME QUE APARECEU NA EXECUÇÃO DO ARQUIVO IrisMicList.py". É obrigatório copiar e colar o nome exatamente igual conforme apareceu no programa e entre aspas duplas. Para rodar o código, basta executar o seguinte comando.: 

 ```py
 python IrisMicList.py
 ```

* **EXECUTAR O CÓDIGO PRINCIPAL**: Após baixar e instalar o python juntamente com os módulos necessários, abra o terminal ou o cmd e vá até a pasta aonde se encontra o código fonte já descompactado e digite.:

 ```py 
 python Iris_VHA.py
 ```

O código será executado.

É isso, boa diversão!    
