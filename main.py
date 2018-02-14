from display import *
from draw import *

screen = new_screen()

color = [ 255, 255, 255 ]
# vertical line
draw_line(250, 0, 250, 500, screen, color)

# horizontal line
draw_line(0, 250, 500, 250, screen, color)

color = [ 0, 255, 0 ]
# y = x & y = -x
draw_line(0, 0, 500, 500, screen, color)
draw_line(0, 500, 500, 0, screen, color)


color = [ 51, 153, 255 ]
# quadrant 1 & quadrant 5
draw_line(250, 250, 500, 400, screen, color)
draw_line(0, 100, 250, 250, screen, color)

color = [ 255, 0, 127 ]
# quadrant 2 & quadrant 6
draw_line(250, 250, 300, 500, screen, color)
draw_line(200, 0, 250, 250, screen, color)

color = [ 178, 102, 255 ]
# quadrant 3 & quadrant 7
draw_line(250, 250, 375, 0, screen, color)
draw_line(125, 500, 250, 250, screen, color)

color = [ 255, 255, 51 ]
# quadrant 4 & quadrant 8
draw_line(250, 250, 500, 200, screen, color)
draw_line(0, 300, 250, 250, screen, color)

display(screen)
save_extension(screen, 'img.png')
