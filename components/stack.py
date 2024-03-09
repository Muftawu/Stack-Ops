from __init__ import * 

class Stack:
      WIDTH = 100
      HEIGHT = 100
      STACK_CELL_CENTER = [i for i in range(150, 800, 100)]

      def __init__(self, win, n_cells, x, y):
            self.win = win 
            self.x = x 
            self.y = y 
            self.n_cells = n_cells 
            assert 0 < n_cells < 8 , 'Cell number must not exceed 7'

      def show_cell_center(self):
            [pygame.draw.circle(self.win, 'green', (250, i), 10) for i in self.STACK_CELL_CENTER[:self.n_cells]]

      def draw_stack(self):
            pygame.draw.rect(self.win, 'orange', (self.x, self.y, self.WIDTH, self.HEIGHT*self.n_cells))
            for i in range(self.n_cells):
                  pygame.draw.line(self.win, 'white', (self.x, self.y+self.HEIGHT*i), (self.x+self.WIDTH, self.y+self.HEIGHT*i))

      def pop(self):
            pass 

      def push(self):
            pass 

