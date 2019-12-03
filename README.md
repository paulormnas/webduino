# webduino
Um serviço simples em Python para conectar o arduino à internet

Neste exemplo é utilizado um serviço desenvolvido com o framework Flask e a biblioteca PySerial, que trata a comunicação serial com o Arduino.

A instalação das bibliotecas será realizada utilizando o gerenciador de pacotes pip. Mas antes deve ser inciado um ambiente virtual onde serão armazenadas todas as configurações deste projeto, evitando conflito com as depêndencias instaladas no computador de desenvolvimento. 

Após clonar o repositório, instale o virtualenv e inicialize o ambiente virtual. Os parâmetros passados no comando `virtualenv` são a versão do Python a ser utilizada e o nome do diretório onde são instaladas as configuções e depedências do ambiente virtual.
```shell
git clone https://github.com/paulormnas/webduino.git
cd webduino
pip3 install virtualenv
vitualenv -p python3 venv
```

Em seguida, ative o ambiente virtual e instale as depêndencias necessárias para o projeto. Neste caso vamos instalar as dependências a partir do arquivo "requirements.txt encontrado no repositório.
```shell
source venv/bin/activate
pip3 install -r requirements.txt
```

Uma vez que o ambiente se encontre configurado basta executar o comando a seguir para iniciar a aplicação do Web Service:
```shell
python3 service.py
```

Lembre-se de identificar a porta serial na qual o arduino se encontra conectado e configurar no arquivo "service.py". Caso contrário será apresentado erro durante o tratamento  das requisções HTTP.


