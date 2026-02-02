#importa as bibliotecas os e shutil
#os -> Responsável pela comunicação com o sistema e pela leitura dos arquivos e diretórios.
#shutil -> Responsável por interagir com o sistema, movendo, copiando e apagando arquivos.
import os
import shutil

#Variável responsável por definir o caminho para a pasta que será organizada.
#O prefixo "r" indica uma raw string -> Faz com que o python interprete a string de maneira literal, evitando o erro da "\".
pasta_alvo = r"C:\Users\Desktop\Downloads"

#Trecho responsável por listar tudo que há dentro da pasta alvo.
#os.listdir() lista tudo que existe na pasta indicada.
#os.path.join() Indica o caminho correto, unindo o caminho do diretório e do arquivo.
for arquivo in os.listdir(pasta_alvo):
    caminho_arquivo = os.path.join(pasta_alvo, arquivo)

    #Identifica se o objeto na pasta é um arquivo e ignora pastas.
    if os.path.isfile(caminho_arquivo):

        #Coleta a extensão do arquivo
        nome,extensao = os.path.splitext(arquivo)

        #ignora arquivos sem extensão
        if extensao == "":
            continue
        
        #Remove o ponto e deixa tudo em maiúsculo.
        pasta_extensao = extensao[1:].upper()

        caminho_pasta = os.path.join(pasta_alvo, pasta_extensao)

        #Cria a pasta caso ela não exista.
        if not os.path.exists(caminho_pasta):
            os.mkdir(caminho_pasta)
        
        #Move o arquivo para a pasta extensão.
        shutil.move(caminho_arquivo, caminho_pasta)

print("Arquivos organizados com sucesso!!".strip())