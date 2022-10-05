from enum import Flag
from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING
from pygame.sprite import Sprite
import pygame



class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS = 310
    JUMP_VELOCITY = 8.5
    
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_velocity = self.JUMP_VELOCITY
        self.dino_duck = True

       
    def update(self, user_input):
        if self.dino_run:
            self.run()    
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        if user_input [pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_jump =True
            self.dino_run = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif not self.dino_jump and not self.dino_duck:
            self.dino_duck = False
            self.dino_jump = False
            self.dino_run = True
        if self.step_index >= 9:
            self.step_index = 0


    def run(self):
        self.image = RUNNING[0] if self .step_index < 5 else RUNNING [1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index += 1

    def jump(self):
        pygame.key.get_pressed()
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        print ("Jump Velocity", self.jump_velocity)
        print("Y Position : ", self.dino_rect.y)
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY
    def duck(self):
        self.image = DUCKING[self.step_index // 5] 
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 40
        self.step_index += 1
    

    def draw(self, screen):
         screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    
        
  
   