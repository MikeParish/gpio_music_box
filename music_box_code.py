import pygame
from gpiozero import Button

pygame.init()

kick = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_bass_hard.wav")
snare = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav")
hihat = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_closed.wav")
bass = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/glitch_bass_g.wav")
glitch = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/glitch_perc5.wav")

#blue/1 is 14
blue_button = Button(14)
#yellow/2 is 15
yellow_button = Button(15)
#green/3 is 18
green_button = Button(18)
#orange/4 is 23
orange_button = Button(23)
#white/5 is 24
white_button = Button(24)

blue_button.when_pressed = kick.play
yellow_button.when_pressed = snare.play
green_button.when_pressed = hihat.play
orange_button.when_pressed = bass.play
white_button.when_pressed = glitch.play
