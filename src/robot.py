import pygame
import math
import random

from .settings import *

from . import food
from . import food_sorter

class Robot(pygame.sprite.Sprite):
    def __init__(self, id: int,x:int,y:int, food:list[food.Food],dict_food: food_sorter.FoodSorter, velocity=2.0, rot_vel=2.0, vision = 80, life = 500, prob_fail_rot =70) -> None:
        super().__init__() 
        self.id = id
        self.rect = pygame.Rect(x,y,ROBOTS_SIZE,ROBOTS_SIZE)
        self.color = pygame.Color(((50+int(velocity)*20) if velocity*20 < 200 else 255,\
                                   (vision) if vision < 250 else 255,\
                                   (50+int(rot_vel)*20 if rot_vel*20 < 200 else 255)))
        
        self.food = food
        self.dict_food = dict_food

        self.angle = random.uniform(0,2*math.pi)
        
        self.velocity = velocity
        self.rot_vel = rot_vel
        self.life = life
        self.vision = vision
        self.prob_fail_rot = prob_fail_rot

        self.timeout = False
        self.closest = 0

        self.food_eaten = 0
        self.food_to_reproduce = random.randint(2,5)



        self.food_to_reproduce = random.randint(2,5)
    
    def vector_to_ind(self, ind):
        if(ind >= len(self.food)):
            ind = 0
        
        if len(self.food) == 0:
            return [random.randint(-1,1),random.randint(-1,1)]
        return [self.food[ind].rect.x - self.rect.x, self.food[ind].rect.y - self.rect.y]
    
    def vector_to_food(self, food: food.Food):
        if food is None:
            return [random.randint(-1,1),random.randint(-1,1)]
        return [food.rect.x - self.rect.x, food.rect.y - self.rect.y]

    def find_closest_food(self,food_list: list[food.Food]):
        
        x,y = self.vector_to_ind(self.closest)
        closest_distance = math.inf

        self.closest = -1
        if len(food_list)==0:
            return
        
        closest = None

        for food in food_list:
            x,y = self.vector_to_food(food)
            if x**2 + y**2 < closest_distance:
                closest_distance = x**2 + y**2
                closest = food
        
        if closest is not None:
            self.closest = self.food.index(closest)


    def closest_food(self):
        close_food = []
        if (self.rect.x//self.dict_food.grid_size,self.rect.y//self.dict_food.grid_size) in self.dict_food.food_dic:
            close_food = close_food + self.dict_food.food_dic[(self.rect.x//self.dict_food.grid_size,self.rect.y//self.dict_food.grid_size)]

        for i in range(1,self.vision//(2*self.dict_food.grid_size)):
            if len(close_food) > 1:
                break
            for j in range(-i,i+1):
                y = i+(self.rect.y//self.dict_food.grid_size)
                x = j+(self.rect.x//self.dict_food.grid_size)
                if (x,y) in self.dict_food.food_dic:
                    close_food = close_food + self.dict_food.food_dic[(x,y)]

                y = -i+(self.rect.y//self.dict_food.grid_size)
                x = -j+(self.rect.x//self.dict_food.grid_size)
                if (x,y) in self.dict_food.food_dic:
                    close_food = close_food + self.dict_food.food_dic[(x,y)]

            for j in range(-i+1,i):
                y = j+(self.rect.y//self.dict_food.grid_size)
                x = i+(self.rect.x//self.dict_food.grid_size)
                if (x,y) in self.dict_food.food_dic:
                    close_food = close_food + self.dict_food.food_dic[(x,y)]

                y = -j+(self.rect.y//self.dict_food.grid_size)
                x = -i+(self.rect.x//self.dict_food.grid_size)
                if (x,y) in self.dict_food.food_dic:
                    close_food = close_food + self.dict_food.food_dic[(x,y)]

        self.find_closest_food(close_food)
    

    def square(self):
        for i in range(0,self.vision):
            for j in range(0,i):
                pass


    def angle_to_food(self, ind):
        x,y = self.vector_to_ind(ind)

        if x**2 + y**2 > self.vision**2:
            return self.angle + math.pi/2 * random.randint(-10,10)*0.1
        return math.atan2(y,x)* (1 if random.randint(0,100) < self.prob_fail_rot else 0)
        
    def draw(self, surface):

        #x1,y1 = self.rect.x+self.rect.width//2 ,self.rect.y+self.rect.width//2 
        #x2, y2 = self.rect.x+self.rect.width//2+(math.cos(self.angle)*10*10),self.rect.y+self.rect.width//2+(math.sin(self.angle)*10*10)

        pygame.draw.rect(surface, self.color, self.rect, width=0)

        #pygame.draw.line(surface,pygame.color.Color(0,0,0),(x1,y1),(x2,y2))

    def wander(self):
        turn_strength = self.rot_vel*0.1
        self.change_angle(random.uniform(-turn_strength, turn_strength))

    def change_angle(self, angle):
        self.angle += angle

    def update(self):
        self.closest_food()
        if self.closest == -1:
            self.wander()
        else:
            self.move_to_food(self.closest)

        move_angle = (math.cos(self.angle)*2*self.velocity*0.5,math.sin(self.angle)*2*self.velocity*0.5)
        self.rect.move_ip(move_angle if random.randint(0,100) < self.prob_fail_rot else (move_angle[0]*1.5, move_angle[1] *1.5))
        self.life -= random.randint(0,1)
        self.life -= 0.05*self.velocity * random.randint(0,1)
        self.life -= 0.05*self.rot_vel * random.randint(0,1)

        if self.life <= 0:
            self.timeout = True

    def move_to_food(self, ind):
        ang = self.angle_to_food(ind)
        move_angle = ang - self.angle
        if move_angle > math.pi:
            move_angle -= 2 * math.pi
        elif move_angle < -math.pi:
            move_angle += 2 * math.pi
        
        self.change_angle(move_angle*0.05 * self.rot_vel*0.1)

        return move_angle

        


        