from __init__ import * 

class Pointer:
      HEIGHT = 50
      WIDTH = 100
      X_OFFSET = HEIGHT 
      POINTER_TIP_X = 250
      POINTER_TIP_Y = [150, 250, 350, 450, 550, 650, 750]
            
      def __init__(self, win, color, ID):
            self.win = win 
            self.color = color 
            self.ID = ID 

      def point(self):
            arrow_points = [
                  (self.X_OFFSET, self.POINTER_TIP_Y[self.ID-1]-self.HEIGHT//2),
                  (self.X_OFFSET+self.WIDTH, self.POINTER_TIP_Y[self.ID-1]-self.HEIGHT//2),
                  (self.X_OFFSET+self.WIDTH, self.POINTER_TIP_Y[self.ID-1]-self.HEIGHT),
                  (self.POINTER_TIP_X, self.POINTER_TIP_Y[self.ID-1]),
                  (self.X_OFFSET+self.WIDTH, self.POINTER_TIP_Y[self.ID-1]+self.HEIGHT),
                  (self.X_OFFSET+self.WIDTH, self.POINTER_TIP_Y[self.ID-1]+self.HEIGHT//2),
                  (self.X_OFFSET, self.POINTER_TIP_Y[self.ID-1]+self.HEIGHT//2),
            ]
            pygame.draw.polygon(self.win, self.color, arrow_points)



                  