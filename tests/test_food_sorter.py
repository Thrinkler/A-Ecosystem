import unittest
import pygame 

from src.food import Food
from src.food_sorter import FoodSorter
# Assuming your FoodSorter class is in a file named food_sorter.py
# from food_sorter import FoodSorter 

# --- Mock Objects for Testing ---
# We create simple mock classes to simulate the behavior of Pygame's Rect and your Food class.
class MockRect:
    def __init__(self, x, y):
        self.x = x
        self.y = y


color = pygame.Color(0,0,0)

# --- The Actual Unit Tests ---

class TestFoodSorter(unittest.TestCase):

    def test_initialization_with_items(self):
        """Tests if the dictionary is populated correctly upon creation."""
        food1 = Food(10, 20, color)
        food2 = Food(30, 40, color)
        food3 = Food(10, 20, color) # Same coordinates as food1
        
        sorter = FoodSorter([food1, food2, food3])
        
        self.assertEqual(len(sorter.food_dic), 2)
        self.assertIn((10, 20), sorter.food_dic)
        self.assertIn((30, 40), sorter.food_dic)
        self.assertEqual(len(sorter.food_dic[(10, 20)]), 2)
        self.assertEqual(sorter.food_dic[(30, 40)], [food2])

    def test_initialization_empty(self):
        """Tests initialization with an empty list."""
        sorter = FoodSorter([])
        self.assertEqual(len(sorter.food_dic), 0)

    def test_add_new_location(self):
        """Tests adding food to a previously empty location."""
        sorter = FoodSorter([])
        food1 = Food(50, 50, color)
        sorter.add(food1)
        
        self.assertIn((50, 50), sorter.food_dic)
        self.assertEqual(sorter.food_dic[(50, 50)], [food1])

    def test_add_to_existing_location(self):
        """Tests adding food to a location that already contains food."""
        food1 = Food(10, 10, color)
        sorter = FoodSorter([food1])
        food2 = Food(10, 10, color)
        sorter.add(food2)
        
        self.assertEqual(len(sorter.food_dic[(10, 10)]), 2)
        self.assertIn(food1, sorter.food_dic[(10, 10)])
        self.assertIn(food2, sorter.food_dic[(10, 10)])

    def test_remove_last_item_at_location(self):
        """Tests removing the only food item, which should also remove the key."""
        food1 = Food(100, 100,color)
        sorter = FoodSorter([food1])
        sorter.remove(food1)
        
        self.assertNotIn((100, 100), sorter.food_dic)

    def test_remove_one_of_many_items(self):
        """Tests removing one item from a location with multiple items."""
        food1 = Food(25, 25,color)
        food2 = Food(25, 25,color)
        sorter = FoodSorter([food1, food2])
        sorter.remove(food1)
        
        self.assertIn((25, 25), sorter.food_dic)
        self.assertEqual(len(sorter.food_dic[(25, 25)]), 1)
        self.assertEqual(sorter.food_dic[(25, 25)], [food2])

    def test_remove_nonexistent_item_raises_exception(self):
        """Tests that removing an item not in the list raises an exception."""
        food1 = Food(1, 1,color)
        food2 = Food(1, 1,color) # A different object at the same coordinates
        sorter = FoodSorter([food1])
        
        # self.assertRaises is a context manager that checks for exceptions.
        with self.assertRaises(Exception):
            sorter.remove(food2)

    def test_remove_from_nonexistent_key_raises_exception(self):
        """Tests that removing from a non-existent key raises an exception."""
        sorter = FoodSorter([])
        food1 = Food(99, 99,color)

        with self.assertRaises(Exception):
            sorter.remove(food1)

# This allows the tests to be run from the command line
if __name__ == '__main__':
    unittest.main()