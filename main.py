#!/usr/bin/env python
import os, sys, regex
from analise import Analisador
from tokens import tokens

#Verifica argumentos de linha de comando
n = len(sys.argv)
if n > 1:
    file_check = os.path.isfile(str(sys.argv[1]))
    if file_check == True:
        print("Usando arquivo especificado: " + str(sys.argv[1]))
        caminho = str(sys.argv[1])
    else:
        print("Arquivo não encontrado, usando arquivo padrão (teste.c)")
        caminho = "teste.c"
else:
    print("Usando arquivo padrão (teste.c)\n")
    caminho = "teste.c"

arquivo = open(str(caminho), 'r')
analisador = Analisador(tokens)
linecount = 0
analise = []
#Realiza a analise linha por linha
for line in arquivo:
    linecount += 1

    analise += analisador.lex_line(line)
output = ""
output += output.join(analise)
#Remover a vírgula do final do texto resultante
print(output[:-2])

