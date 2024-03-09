from __init__ import * 
from components.stack import Stack
from components.pointer import Pointer
from config import *

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(TITLE)

# frame rate
clock = pygame.time.Clock()

def main(expression):
      data_dict = {i:ch for i, ch in enumerate([d for d in expression].__reversed__())}
      print(data_dict)

      num_cells = polish_notation(len(data_dict))
      run = True
      win.fill('black')
      clock.tick(FPS)

      # stack instance
      try:
            stacks = []
            stack_container_offset = [j for j in range(0, 200*num_cells, STACK_SPACING)]
            for i in range(num_cells):
                  stacks += [Stack(win, num_cells, STACK_X+stack_container_offset[i], STACK_Y)]
      except:
            pass 

      # master pointer  
      master_pointer = Pointer(win, 'yellow', num_cells)

      # get text display centers
      text_display_centers = [stacks[0].STACK_CELL_CENTER[i] for i in data_dict]

      # stack pointer container
      pointers = [master_pointer]

      # arrow pointer heads for selected cells 
      master_pointer.POINTER_TIP_Y = master_pointer.POINTER_TIP_Y[:num_cells]

      # slave pointers 
      for i in range(1, master_pointer.ID).__reversed__():
            pointers.append(Pointer(win, 'blue', i))

      while run:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT: 
                        run = False

                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE: 
                              pygame.quit()

            # simulation title bar / details 
            render_text(win, TITLE_FONT, f'Expression => {expression}', 'white', WIN_WIDTH//2-0.3*WIN_WIDTH, EXPRESSION_TITLE_Y) 
                        
            # draw stack 
            for j, stack in enumerate(stacks):
                  stack.draw_stack()  
                  render_text(win, STACK_LABEL_FONT, f'Stack {j+1}', 'white', stack.x-15, stack.y+WIN_HEIGHT-200)
    

            # draw pointers
            for pointer in pointers:
                  pointer.point()

            # show cell centers of stack 
            stack.show_cell_center()

            # arrange data in stack cells
            x = master_pointer.X_OFFSET+master_pointer.WIDTH+110
            [render_text(win, TEXT_FONT, data_dict[idx], 'white', x, y-CELL_TEXT_OFFSET_Y) for idx, y in enumerate(text_display_centers)]


            pygame.display.update()


if __name__ == "__main__":
      expression = '12+48/6'
      main(expression)