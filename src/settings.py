import configparser

config = configparser.ConfigParser()

config.read('src/config.ini')

INITIAL_ROBOTS = config.getint('Simulation', 'initial_robots')
INITIAL_FOOD = config.getint('Simulation', 'initial_food')
FPS = config.getint('Simulation', 'fps')
ROBOTS_SIZE = config.getint('Simulation', 'robots_size')
FOOD_SIZE = config.getint('Simulation', 'food_size')

SCREEN_WIDTH = config.getint('Screen', 'width')
SCREEN_HEIGHT = config.getint('Screen', 'height')

FOOD_SPAWN_RATE = config.getfloat('FoodGenetics', 'food_spawn_rate')
FOOD_DEATH_TIME = config.getint('FoodGenetics', 'food_death_time')
FOOD_CHILD_TIME = config.getint('FoodGenetics', 'food_child_time')
FOOD_CHILD_RATE = config.getfloat('FoodGenetics', 'food_child_rate')

MIN_LIFE = config.getint('RobotGenetics', 'min_life')
MAX_LIFE = config.getint('RobotGenetics', 'max_life')
MIN_FIRST_VELOCITY = config.getint('RobotGenetics', 'min_first_velocity')
MAX_FIRST_VELOCITY = config.getint('RobotGenetics', 'max_first_velocity')
MIN_FIRST_ROT_VELOCITY = config.getint('RobotGenetics', 'min_first_rot_vel')
MAX_FIRST_ROT_VELOCITY = config.getint('RobotGenetics', 'max_first_rot_vel')
MIN_FIRST_VISION = config.getint('RobotGenetics', 'min_first_vision')
MAX_FIRST_VISION = config.getint('RobotGenetics', 'max_first_vision')
MIN_FIRST_FAIL_ROT = config.getint('RobotGenetics', 'min_first_fail_rot')
MAX_FIRST_FAIL_ROT = config.getint('RobotGenetics', 'max_first_fail_rot')
MUTATION_RATE = config.getfloat('RobotGenetics', 'mutation_rate')

GRID_CELL_SIZE = config.getint('World', 'grid_cell_size')
ROBOT_FIRST_SPECIES_COUNT = config.getint('World', 'robot_first_species_count')
ROBOT_MIN_SPECIES_POP = config.getint('World', 'robot_min_species_pop')
ROBOT_MAX_SPECIES_POP = config.getint('World', 'robot_max_species_pop')

SPECIAL_NAME = config.getboolean('Logs', 'special_name')
SPECIAL_MIN = config.getint('Logs','special_min')