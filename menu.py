import pygame , os
from pygame import mixer

#class untuk menampilkan menu
class Menu():
    def __init__ (self, gambar, x, y, W, H, animasi = 10):
        pygame.mixer.init()
        self.width_M , self.height_M = W , H
        self.image_original = pygame.transform.scale(gambar, (self.width_M, self.height_M))
        self.image_elevation = pygame.transform.scale(gambar, (120, 120))
        self.image = pygame.transform.scale(gambar, (self.width_M, self.height_M))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.dinamic_elevation = animasi
        self.original_y = y
        self.button_sound = mixer.Sound(os.path.join('Assets/Musik/button_sound.mp3'))
        self.button_sound.set_volume(0.2)
        self.cursor_sound = mixer.Sound(os.path.join('Assets/Musik/cursor_sound.mp3'))
        self.cursor_sound.set_volume(0.1)
        self.check = True

    def display_Menu(self, screen):
        play = False

        self.rect.y = self.original_y
        #posisi mouse
        pos_mouse = pygame.mouse.get_pos()

        #check jika posisi mouse berada pada gambar
        if self.rect.collidepoint(pos_mouse):
            if self.check:
                self.cursor_sound.play()
                self.check = False
            
            self.rect.y = self.original_y + self.dinamic_elevation
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.button_sound.play()
                self.image = self.image_elevation
                play = True
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked == False
                self.image = self.image_original
        else :
            self.check = True

        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return play
