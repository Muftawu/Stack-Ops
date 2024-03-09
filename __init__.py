import pygame
from config import * 
pygame.init()
import sys

TITLE_FONT = pygame.font.SysFont('tlwgtypist', TITLE_FONT_SIZE)
TEXT_FONT = pygame.font.SysFont('tlwgtypist', CELL_FONT_SIZE)
STACK_LABEL_FONT = pygame.font.SysFont('tlwgtypist', STACK_LABEL_FONT_SIZE)

def render_text(win, font, text, text_color, x, y):
      data = font.render(text, False, text_color)
      win.blit(data, (x, y))

def pad(data: str):
      data_len = [d for d in str(data)]
      print('data len', len(data))
      try:
            if data_len == 1:
                  data = '00'+str(data)
            elif data_len == 2:
                  data = '0'+str(data)
      except:
            print("Max value length should be 3")
      return data
     
def polish_notation(default_cell_size):
      user_specified_cell_num = default_cell_size
      try:
            user_specified_cell_num = int(sys.argv[1])
      except:
            print('input must be an integer') 
      return user_specified_cell_num

if __name__ == '__main__':
      # polish_notation()
      print(pad('4'))