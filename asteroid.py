import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH ,ASTEROID_MIN_RADIUS
from logger import log_event
import  random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def split (self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        random_angle = random.uniform(20 , 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x ,self.position.y , new_rad)
        asteroid2 = Asteroid(self.position.x ,self.position.y , new_rad)
        asteroid1.velocity = a * 1.2
        asteroid2.velocity = b * 1.2

    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen , "white" , self.position , self.radius , LINE_WIDTH )        


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt