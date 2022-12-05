#IMPORTA A BIBLIOTECA "TIMER" PARA DESENHAR OU MOVER OBJETOS NA TELA COM UM TEMPO DETERMINADO
import time
#IMPORTA TUDO DA BIBLIOTECA TKINTER QUE JÁ VEM COM O PYTHON, QUE POSSIBILITA A CRIAÇÃO DE [GUI]
from tkinter import *

#CLASSE PARA GERENCIAR OS CANVAS E O LOOP PRINCIPAL POR ONDE IRA RODAR A APLICAÇÃO.
class main():
    def __init__(self,parent):
        super().__init__()
        self.StartingPage()
    
    #FUNÇÃO DO SEGUNDO CANVAS E/OU SCREEN(TELA), AINDA SEM CARACTERISTICAS.
    def CC(self):
            def swordbtn(event):
                print("Sword Button pressed")
                
            def wandbtn(event):
                print("Wand Button pressed")
            
            #ADQUIRE INFORMAÇÕES DA TELA DO USUÁRIO
            width = root.winfo_screenwidth()       
            height = root.winfo_screenheight()
            #CRIA UM NOVO CANVAS COM AS INFORMAÇÕES DA TELA DO USUÁRIO
            w = Canvas(width= width, height=height)
            #SINTÁXE PARA CRIAR UM RETÂNGULO NA TELA
            
            #FUNÇÃO PARA MANIPULAR A POSIÇÃO DO CANVAS
            w.grid(row=0,column=0) 
            
            
            new_y= width - 400
            
            self.sword=w.create_image(400,-190, image=swordcc )
            w.tag_bind(self.sword, "<Button-1>", swordbtn)
            self.wand = w.create_image(new_y, -190, image=wandtt )
            w.tag_bind(self.wand, "<Button-1>", wandbtn)
            
            self.target_y = 240
            while True:
            #PEGA AS COORDENADAS ATUAIS DOS BOTÕES          
                x, y = w.coords(self.play)
                #MOVE O BOTÃO PLAY, X UNIDADE E Y UNIDADES, X,Y SÃO COORDENADAS DO CANVAS.
                w.move(self.sword,0,20)
                #MOVE O BOTÃO QUIT, X UNIDADE E Y UNIDADES, X,Y SÃO COORDENADAS DO CANVAS.
                w.move(self.wand,0,20)
                #ATUALIZA O ESTADO DA GUI, MOSTRANDO O FUNCIONAMENTO DA ANIMAÇÃO
                root.update()
                #TIMER UTILIZADO PARA QUE O LOOP TENHA UMA TRANSFERENCIA SUAVE ENTRE FRAMES
                time.sleep(0.05)
                #QUANDO O LIMITE EM QUE OS BOTÕES SÃO ANIMADOS SÃO ALCANÇADOS O EVENTO TERMINA
                if y >= self.target_y:
                    break
            w.create_rectangle(287,460, 512, 600, width=4)
            w.create_rectangle(853,460, 1078, 600, width=4)
            w.create_text(400, 500, text="GUERREIROS SÃO RESISTENTES E CAPAZES DE LUTAR POR LONGOS PERIODOS DE TEMPO",width=210)    
                
            w.create_text(new_y, 500, text="MAGOS SÃO FORTES PORÉM POSSUEM POUCA RESISTÊNCIA, CAUSAM GRANDES DANOS EM MENOS TEMPO", width=210)
    #FUNÇÃO DA PÁGINA INICIAL, POR ENQUANTO CONTENDO UMA ANIMAÇÃO BÁSICA PARA OS BOTÕES
    def StartingPage(self):
        #FUNÇÃO DO BOTÃO PLAY, PRINT DO SEU USO, DELETA TODO O CONTEUDO DO CANVAS E CHAMA O PRÓXIMO CANVAS
        def playbtn(event):
            #PRINTA O EVENTO
            print("play Pressed")
            #DELETA O CONTEUDO
            w.delete("all")
            #CHAMA A PRÓXIMA FUNÇÃO
            self.CC()
        
        #FUNÇÃO DO BOTAO QUIT, PRINT DO SEU USO, DESTROY TODO O PROGRAMA PARA SAIR DA APLICAÇÃO
        def quitbtn(event):
            #PRINTA O EVENTO
            print("Quit Pressed")
            #DESTROI TODA A APLICAÇÃO, ASSIM, ENCERRANDO O PROGRAMA
            root.destroy()
        
        #ADQUIRE OS DADOS DA TELA DO JOGADOR PARA CRIAR UM CANVAS COM TAMANHO SEMPRE AJUSTADO
        w = root.winfo_screenwidth()    
        h = root.winfo_screenheight()
        #DESENHA UM CANVAS NA TELA BASEADO NAS INFORMAÇOES DA TELA DO USUÁRIO
        w = Canvas(width= w, height=h)
        #POSICIONA O CANVAS NA TELA
        w.grid(row=0,column=0)
        
        #GERA NOVAS VARIÁVEIS PARA POSICIONAR OS BOTÕES NA TELA BASEADOS NA TELA DO USUÁRIO
        new_x= h - 105
        new_y= h - 50
        
        #CRIA O BOTÃO PLAY E ATRIBUI UMA FUNÇÃO À ELE
        self.play = w.create_image(-60,new_x, image=playimg)
        #TAG_BIND ATRIBUI ALGUMA FUNÇÃO AO OBJETO ORIENTADO
        w.tag_bind(self.play, "<Button-1>",playbtn)
        
        #CRIA O BOTÃO QUIT E ATRIBUI UMA FUNÇÃO À ELE
        self.quit=w.create_image(-60,new_y, image=quitimg)
        #TAG_BIND ATRIBUI ALGUMA FUNÇÃO AO OBJETO ORIENTADO
        w.tag_bind(self.quit, "<Button-1>", quitbtn)
        
        #DEFINE O LIMITE PARA QUE OS BOTÕES SEJAM ANIMADOS
        self.target_x = 50

        #MOVE OS BOTÕES ATÉ A COORDENADA DESEJADA
        while True:
            #PEGA AS COORDENADAS ATUAIS DOS BOTÕES          
            x, y = w.coords(self.play)
            #MOVE O BOTÃO PLAY, X UNIDADE E Y UNIDADES, X,Y SÃO COORDENADAS DO CANVAS.
            w.move(self.play,15,0)
            #MOVE O BOTÃO QUIT, X UNIDADE E Y UNIDADES, X,Y SÃO COORDENADAS DO CANVAS.
            w.move(self.quit,14.7,0)
            #ATUALIZA O ESTADO DA GUI, MOSTRANDO O FUNCIONAMENTO DA ANIMAÇÃO
            root.update()
            #TIMER UTILIZADO PARA QUE O LOOP TENHA UMA TRANSFERENCIA SUAVE ENTRE FRAMES
            time.sleep(0.05)
            #QUANDO O LIMITE EM QUE OS BOTÕES SÃO ANIMADOS SÃO ALCANÇADOS O EVENTO TERMINA
            if x >= self.target_x:
                break
if __name__ == '__main__':
    root=Tk()
    #HABILITA A OPÇÃO DE PREENCHER A TELA COM O TAMANHO DA GUI CRIADA
    root.overrideredirect(True)
    #CRIA A GUI COM O TAMANHO BASEADO NA TELA DO JOGADOR, FAZENDO A JANELA FICAR EM [FULLSCREEN(TELA-CHEIA)]
    root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    #PRINTA AS INFORMAÇÕES DA TELA PARA CONSULTA NO CONSOLE
    print("WIDTH=",root.winfo_screenwidth(),", HEIGHT=",root.winfo_screenheight())
    #PEGA IMAGENS DA PASTA IMAGENS DENTRO DO DIRETÓRIO DA APLICAÇÃO PARA UTILIZAÇÃO
    playimg = PhotoImage(file="images/playmain.png")
    quitimg = PhotoImage(file="images/quitmain.png")
    swordcc = PhotoImage(file="images/swordcc.png")
    wandtt = PhotoImage(file="images/wandtt.png")
    #CHAMA A CLASSE "MAIN" PARA COMEÇAR A DESENHAR E MANIPULAR NA TELA
    main=main(root)
    #MANTÉM O LOOP DA APLICAÇÃO ATÉ QUE SEJA INTERROMPIDA(DESTROY, EXIT BUTTON, ETC..)
    root.mainloop()
