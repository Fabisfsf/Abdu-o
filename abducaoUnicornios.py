import pygame, sys
from pygame.locals import *

largura = 900
altura = 400

class Unicornio(pygame.sprite.Sprite):
        def __init__(self, posx, posy):
           pygame.sprite.Sprite.__init__(self)
           self.imagem1 = pygame.image.load('sprites/unicornio.png')
           self.imagem2 = pygame.image.load('sprites/unicornio2.png')

           self.listaImagens = [self.imagem1, self.imagem2]
           self.posImagem = 0
           self.imagemUnicornio = self.listaImagens[self.posImagem]

           

           self.rect = self.imagemUnicornio.get_rect()

           self.listaDisparo = []
           self.velocidade= 5
           self.rect.top = posy
           self.rect.left = posx

           self.configTempo = 1

        def comportamento(self, tempo):
            if self.configTempo == tempo:
                self.posImagem += 1
                self.configTempo += 1
                if self.posImagem > len(self.listaImagens)-1:
                        self.posIMagem = 0
                        
        def colocar(self, superficie):
            self.imagemUnicornio = self.listaImagens[self.posImagem]                    
            superficie.blit(self.imagemUnicornio, self.rect)

class Raio(pygame.sprite.Sprite):
        def __init__(self, posx, posy):
           pygame.sprite.Sprite.__init__(self)
           self.ImagemRaio = pygame.image.load('sprites/raio.png')

           self.rect = self.ImagemRaio.get_rect()
           self.velocidadeRaio = 5
           self.rect.top = posy
           self.rect.left = posx

        def trajetoria(self):
            self.rect.top = self.rect.top - self.velocidadeRaio

        def colocar(self, superficie):
            superficie.blit(self.ImagemRaio, self.rect)

class naveEspacial (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load('sprites/nave.png')
          
        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura / 2
        self.rect.centery = altura - 350
        self.listaDisparo = []
        self.vida = True
        self.velocidade = 50

    def movimento(self):
             if self.vida == True:
                 if self.rect.left <= 0:
                    self.rect.left = 0

                 elif self.rect.right > 900:
                      self.rect.right = 900

    def disparar(self, x, y):
        meuRaio = Raio(x,y)
        self.listaDisparo.append(meuRaio)

    def colocar(self, superficie):
        superficie.blit(self.ImagemNave, self.rect)
          
            
def invasaoEspaco():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Invasao do Espaco")
    
    jogador = naveEspacial()
    ImagemFundo = pygame.image.load('sprites/fundo_ok.png')
    jogando = True
    inimigo = Unicornio(100,350)

    raioNave = Raio(largura / 2 , altura + 350)

    while True:

        
        tempo =  pygame.time.get_ticks()/1000
        jogador.movimento()
        raioNave.trajetoria
        for evento in pygame.event.get():
            if evento.type == QUIT:
               pygame.quit()
               sys.exit()

            if evento.type == pygame.KEYDOWN:
               if evento.key == K_LEFT:
                  jogador.rect.left -= jogador.velocidade

               elif evento.key == K_RIGHT:
                    jogador.rect.right += jogador.velocidade

               elif evento.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.disparar(x,y)
                                    
        tela.blit(ImagemFundo, (0,0))
        raioNave.colocar(tela)
        jogador.colocar(tela)
        inimigo.colocar(tela)
        inimigo.comportamento(tempo)
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
        pygame.display.update()
                      
invasaoEspaco()

                             
   
        

               


            
            
               




                   

                              
