import pygame


class Cell:
    def __init__(self, x=0, y=0, width: int = 20, length: int = 20, display = None,border = 2):

        # identities of a cell
        self.coordinates = [x, y]
        self.type = 'Head'
        self.size = (width, length)
        self.change_type(self.type)
        self.border = border
        
        # links with different cells
        self.top = None
        self.bottom = None
        self.right = None
        self.left = None

        # position of cell
        self.x = x
        self.y = y
        
        
        self.snake_length = 0
        self.off_set = 0
        
        #link to display
        self.screen = display
        
    def change_type(self, cell_type):
        if cell_type not in ['Head','Body','Food','Floor']:
            raise ValueError('Bad cell type')   
            
        cell_types = {
        'Head':  "pink",
        'Body':  "red",
        'Food':  "yellow",
        'Floor': "black"
        }
        
        self.color = cell_types[cell_type]
        
    def draw_cell(self):
        pygame.draw.rect(
            self.screen, 
            self.color, 
            [self.x, self.y, self.size[0], self.size[0]])
        
    def change_state(self):
        if self.type == 'Head':
            self.change_type('Body')
        elif self.type == 'Body':
            self.change_type('Floor')
    
    def __str__(self):
        cell_types = {
        'Head':  1,
        'Body':  2,
        'Food':  3,
        'Floor': 0
        }
        
        return str(cell_types[self.type])
    
    def body_dead(self):
        self.snake_length = self.snake_length - 1
        if self.snake_length == 0:
            self.change_state()
            
    def set_position(self,off_set = 0):
        self.x = (self.coordinates[0] * self.size[0]) + off_set * self.border
        self.y = (self.coordinates[1] * self.size[0]) + off_set * self.border
            
    def display(self):
        self.set_position()
        pygame.draw.rect(
            self.screen, 
            'black', 
            [self.x, self.y, self.size[0], self.size[0]])
        pygame.draw.rect(
            self.screen, 
            self.color, 
            [self.x+1, self.y+1, self.size[0]-2, self.size[0]-2])

class Board:

    def __init__(self, columns: int = 10, rows: int = 10, tile_size=(20, 20)):
        self.columns = columns
        self.rows = rows
        self.width = columns * (tile_size[0])
        self.length = rows * (tile_size[1])
        self.head = None
        self.head_row = None
        self.tail = None
        self.visualization = []
        self.line = []
        self.screen = pygame.display.set_mode((self.width,self.length))
        self.number_tiles = 0

    def add_tile(self, tile):
        if self.head == None:  # """If there is no tile in board"""
            tile.coordinates = [0, 0]
            self.head = tile
            self.head_row = tile
            self.tail = tile
            self.visualization.append(tile.type)
        else:
            if self.number_tiles % self.columns == 0:  # """If the new tile will go into new line"""
                tile.coordinates = [self.head_row.coordinates[0], self.head_row.coordinates[1]+1]
                self.head_row.bottom = tile
                tile.top = self.head_row
                self.head_row = tile
                self.head = tile
                self.visualization.append(self.line.copy())
                self.visualization.append(tile.type)
            else:  # """if new tile go to the same row as previous tile"""
                tile.coordinates = [self.head.coordinates[0] + 1, self.head.coordinates[1]]
                if self.number_tiles / self.columns >= 1 and self.columns > 1:
                    self.head.top.right.bottom = tile
                    tile.top = self.head.top.right
                    
                self.visualization.append(tile.type)
                self.head.right = tile
                tile.left = self.head
                self.head = tile
        self.number_tiles += 1
        if self.rows * self.columns == self.number_tiles:
            self.visualization.append(self.line.copy())
            
    def create(self):
        tile_number = self.rows * self.columns
        for tiles in range(int(tile_number)):
            node = Cell(display = self.screen)
            self.add_tile(node)

    def output(self):
        tile = self.tail
        small_tail = self.tail
        for y in range(self.rows):
            for x in range(self.columns):
                tile.display()
                tile = tile.right
            small_tail = small_tail.bottom
            tile = small_tail
            
    def __str__(self):
        return self.visualization
    

        
    
pygame.init()

x = Board()
x.create()
x.output()
print(x.width)
print(x.visualization)
pygame.display.flip()