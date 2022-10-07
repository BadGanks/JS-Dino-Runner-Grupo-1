from multiprocessing.pool import RUN
from unittest.mock import DEFAULT
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.player_hearts.player_hear_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.shield import Shield 
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS, RUNNING, FONT_STYLE
from dino_runner.components.obstacles.obstade_manager import ObstacleManager





class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.shields = [Shield()]
        self.player = Dinosaur()
        self._obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = PlayerHeartManager()
        
        self.death_count = 0
        self.score = Score()

    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self._obstacle_manager.update(self.game_speed, self.player, self.on_death,)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.player, self.score.score)
        self.power_up_manager.generate_power_up(self.score.score)
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

            
        pygame.quit()

    def run(self):

        
        self.playing = True
        self._obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self._obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_activate()
        self.heart_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def show_menu(self):
        self.screen.fill((255,255,255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH //2
        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text_component = font.render("PRESS ANY KEY TO START", True, (0,0,0))
            text_rect = text_component.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text_component, text_rect)
        else:
            self.death_count > 0
            font = pygame.font.Font(FONT_STYLE, 30)
            text_component = font.render("PRESS THE KEY TO CONTINUE PLAYING", True, (0,0,0))
            text_rect = text_component.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text_component, text_rect)

            font = pygame.font.Font(FONT_STYLE, 30)
            text_component = font.render(f"NUMBER OF DEATHS: {self.death_count}", True, (0,0,0))
            text_rect = text_component.get_rect()
            text_rect.center = (550, 400)
            self.screen.blit(text_component, text_rect)
            
            font = pygame.font.Font(FONT_STYLE, 30)
            text_component = font.render(f"Score: {self.score.score-1}", True, (0,0,0))
            text_rect = text_component.get_rect()
            text_rect.center = (550, 100)
            self.screen.blit(text_component, text_rect)

        
        
        self.screen.blit(RUNNING[0], (half_screen_width - 30, half_screen_height - 140))
        pygame.display.update()
        self.handle_key_events_on_menu()
        

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


            elif event.type == pygame.KEYDOWN:
                self.score.reset_score()
                self.game_speed = 20
                self.run()
                self.heart_manager.redeuce_heart()
                
           

    
    def on_death(self):
        has_shield = self.player.type == SHIELD_TYPE
        is_invencible = self.player.type == SHIELD_TYPE or self.heart_manager.heart_count > 0
        self.heart_manager.redeuce_heart()
        if has_shield:
            self.heart_manager.redeuce_heart()

        if not is_invencible:
                pygame.time.delay(500)
                self.playing = False
                self.death_count += 1
        
        return is_invencible
            
           
    
    def draw_power_up_activate(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 20)
                text_component = font.render(f"ENABNLE FOR SECONDS: {time_to_show}", True, (0,0,0))
                text_rect = text_component.get_rect()
                text_rect.center = (550, 100)
                self.screen.blit(text_component, text_rect)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    
    