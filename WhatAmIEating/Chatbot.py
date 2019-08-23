import json
import sys
import os
import subprocess as s

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json','r')
        except FileNotFoundError:
            memoria = open(nome+'.json','w')
            memoria.write('[["Jess", "Jaime"],  {"Hi": "Hi! What is your name?","Tchau":"tchau", "no":"No problem!"}]')
            memoria.close()
            memoria = open(nome+'.json','r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None,]
    

    def escuta(self, frase=None):
        if frase == None:
            frase = input('>: ')
        frase=str(frase)
        if self.historico[-1] != 'Enter answer: ':
            frase=frase.lower()
            return frase
        return frase


        

    def pensa(self,frase):
        ultimaFrase=self.historico[-1]

        if frase == '/start':
            return """
Welcome! :) 

I am a Chatbot made by Jéssica Alves.
I am here to tell you about human nutrition.
You tell me the name of some food, and I'll tell you the nutritional information of that food.

ex: Apple, Banana, Soy. 

If you want to teach me something, just write "learn" in the text box.

Tell me about you: What is your name?
            """

        if "What is your name?" in ultimaFrase:
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase

        if ultimaFrase == 'I have not learned about this food yet. Do you want to teach me? ':
            if frase.lower() == 'no':
                return 'Alright! Maybe u can teach me someday.'
            if frase.lower() == 'yes' or frase.lower == 'learn':
                return 'What food do you want to teach me? '    
        

        if ultimaFrase == 'What food do you want to teach me? ':
            self.chave = frase 
            return 'Enter answer: '

        if ultimaFrase == 'Enter answer: ':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Learned! :)'

        if frase in self.frases:
            return self.frases[frase]

        if frase == 'learn':
            return 'What food do you want to teach me? '

        if frase not in self.frases:
            return 'I have not learned about this food yet. Do you want to teach me? '


        try:
            resp = str(eval(frase))
            return resp
        except:
            pass

        
        
            
    def pegaNome(self,nome):
        if 'my name is' in nome:
            nome = nome[12:]

        nome = nome.title()
        return nome

    def respondeNome(self,nome):
        if nome in self.conhecidos:
            frase = 'Hey, '
        else:
            frase = 'Nice to meet u, '
            self.conhecidos.append(nome)
            self.gravaMemoria()
            
        return frase+nome

    def fala(self,frase):
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ','')
            if 'win' in plataforma:
                os.startfile(comando)
            if 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError:
                    s.Popen(['xdg-open',comando])
        else:
            print(frase)
        self.historico.append(frase)


    def gravaMemoria(self):
        memoria = open(self.nome+'.json','w')
        json.dump([self.conhecidos, self.frases],memoria)
        memoria.close()