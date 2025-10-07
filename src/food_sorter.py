from . import food
from .settings import *

class FoodSorter:
    def __init__(self, food_items: list[food.Food]):
        self.food_items = food_items

        self.grid_size = GRID_CELL_SIZE

        self.food_dic = {}
        for f in self.food_items:
            if (f.rect.x//self.grid_size,f.rect.y//self.grid_size) in self.food_dic:
                self.food_dic[(f.rect.x//self.grid_size,f.rect.y//self.grid_size)].append(f)
            else:
                self.food_dic[(f.rect.x//self.grid_size,f.rect.y//self.grid_size)] = [f]

    def add(self, food : food.Food):
        if (food.rect.x//self.grid_size,food.rect.y//self.grid_size) in self.food_dic:
            self.food_dic[(food.rect.x//self.grid_size,food.rect.y//self.grid_size)].append(food)
        else:
            self.food_dic[(food.rect.x//self.grid_size,food.rect.y//self.grid_size)] = [food]

    def remove(self, food :food.Food):
        if (food.rect.x//self.grid_size,food.rect.y//self.grid_size) not in self.food_dic:
            raise Exception("element not in list")
        
        self.food_dic[(food.rect.x//self.grid_size,food.rect.y//self.grid_size)].remove(food)
        if len(self.food_dic[(food.rect.x//self.grid_size,food.rect.y//self.grid_size)]) == 0:
            self.food_dic.pop((food.rect.x//self.grid_size,food.rect.y//self.grid_size))