WIDTH = 900
HEIGHT = 700
# Высота и ширина поля по которому бегает змея
WIDTH_field = 720
HEIGHT_field = 390

x_field_start = (WIDTH - WIDTH_field) /2 #90
y_field_start = 195#(HEIGHT - HEIGHT_field) /2

#  координаты  начала и конца  горизонтальных линий
horizontal_start_pos_x = x_field_start #90
horizontal_start_pos_y =  y_field_start + 30 #185
horizontal_end_pos_x = x_field_start + WIDTH_field - 1 #809
horizontal_end_pos_y = y_field_start + 30 #185
#  координаты  начала и конца  вертикальных линий
vertical_start_pos_x = x_field_start + 30  #120
vertical_start_pos_y = y_field_start #155
vertical_end_pos_x = x_field_start + 30 #120
vertical_end_pos_y = y_field_start + HEIGHT_field#545

#Цвета
background_color = (29, 79, 51)
field_color = (250, 209, 160)
line_color = (250, 250, 250)
green_color = (0, 61, 30)
light_grey_color = (215, 215, 215)
grey_color = (140, 140, 140)
brown_color = (77, 42, 0)
white_color = (225, 225, 225)

