import random
import pygame

from . import robot
from . import food
from . import create_files
from . import food_sorter

class Creator:
    def __init__(self, numRobots, numFoods):
        self.file = create_files.new_file()

        self.F = [food.Food(random.randint(0,1000),random.randint(0,800),pygame.Color(0,255,0)) for i in range(numFoods)]
        self.dic_F = food_sorter.FoodSorter(self.F)

        self.P = [robot.Robot(i,random.randint(0,800),random.randint(0,600), self.F, self.dic_F, \
                    velocity=random.uniform(1,10), rot_vel=random.uniform(1,10), \
                    vision = random.randint(50,100), prob_fail_rot= random.randint(50,100),
                    life=random.randint(100,1000))\
                    for i in range(numRobots)]
        
        
        self.mutation_rate = 0.1

        self.avg_velocity = 0
        self.avg_rot_vel = 0
        self.avg_vision = 0
        self.avg_fail_rot = 0
    
    def update(self):

        self.avg_velocity = self.avg_velocity/len(self.P) if len(self.P) > 0 else 0
        self.avg_rot_vel = self.avg_rot_vel/len(self.P) if len(self.P) > 0 else 0
        self.avg_vision = self.avg_vision/len(self.P) if len(self.P) > 0 else 0
        self.avg_fail_rot = self.avg_fail_rot/len(self.P) if len(self.P) > 0 else 0

        if(self.avg_velocity > 0 or self.avg_rot_vel > 0 or self.avg_vision > 0 or self.avg_fail_rot > 0):
            self.file.write(str(len(self.F))+","+ str(len(self.P))+ "," + str(self.avg_velocity) + "," + str(self.avg_rot_vel) + "," + str(self.avg_vision) + "," + str(self.avg_fail_rot) + "\n")
        self.avg_velocity = 0
        self.avg_rot_vel = 0
        self.avg_vision = 0
        self.avg_fail_rot = 0

        if random.randint(0,100) > 98:
            self.F.append(food.Food(random.randint(0,1000),random.randint(0,800),pygame.Color(0,255,0)))
            self.dic_F.add(self.F[-1])

        for f in self.F:
            if f.time > f.death_time:
                self.dic_F.remove(f)
                self.F.pop(self.F.index(f))
            if f.time > f.child_time: #and len(self.F) < 3000:
                self.F.append(f.gen_new())
                self.dic_F.add(self.F[-1])
                f.time = 0

        for p in self.P:

            self.avg_velocity += p.velocity
            self.avg_rot_vel += p.rot_vel
            self.avg_vision += p.vision
            self.avg_fail_rot += p.prob_fail_rot
            p.closest_food()
            p.move_to_food(p.closest)

            if self.F != []:
                if p.rect.colliderect(self.F[p.closest].rect):
                    p.food_eaten += 1
                    p.life += 50
                    self.dic_F.remove(self.F[p.closest])
                    self.F.pop(p.closest)
            
            
            
            if p.food_eaten >= p.food_to_reproduce:
                self.P.append(robot.Robot(p.id,p.rect.x,p.rect.y, self.F,self.dic_F,\
                        velocity=p.velocity+(random.uniform(-1,1) if random.randint(0,10)< self.mutation_rate*10 else 0),\
                        rot_vel=p.rot_vel+(random.uniform(-1,1) if random.randint(0,10)< self.mutation_rate*10 else 0),\
                        vision=p.vision+(random.randint(-10,10) if random.randint(0,10)< self.mutation_rate*10 else 0), \
                        prob_fail_rot=p.prob_fail_rot+(random.randint(-10,10) if random.randint(0,10)< self.mutation_rate*10 else 0),\
                            life=random.randint(100,1000)))

                p.food_eaten = 0
                p.food_to_reproduce += random.randint(2,5)

            if p.timeout:
                self.P.pop(self.P.index(p))
        

    def draw(self,surface):
        self.update()
        for p in self.P:
            p.draw(surface)
        for f in self.F:
            f.draw(surface)