"""
Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

OBS: Existem várias maneiras de reproduzir música. Aqui utiliza-se a biblioteca pugame
"""
# Bibliotecas
import pygame

# Iniciar pygame
pygame.mixer.init()

# Carregar música
pygame.mixer.music.load('C:/Users/e018266/Documents/PythonCursoEmVideo/modulo2/ex21.mp3')

# Executar música
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
