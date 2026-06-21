import pygame
import random
import constants as const

pygame.init()

game_points = 0
snake_lives = "Yes"

screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
done = False

clock = pygame.time.Clock()
text_size = 65
font = pygame.font.Font(None, text_size)

screen.fill(const.background_color)
old_direction = ''

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

snake =[Point(12, 6)]
direction = ""
apples = []
apple_serf = pygame.image.load("Apple.png")
tick = 0

btn_easy_level = pygame.Rect(160, 169, 200, 49)
btn_medium_level = pygame.Rect(160, 248, 200, 51)
btn_hard_level =  pygame.Rect(160, 326, 200, 55)
btn_restart = pygame.Rect(95, 265, 310, 60)
btn_exit = pygame.Rect(505, 265, 298, 60)

def draw():
    # Рисуем поле по которому бегает змейка
    pygame.draw.rect(screen, const.field_color, pygame.Rect(const.x_field_start, const.y_field_start, const.WIDTH_field, const.HEIGHT_field))
    for i in range(12):
        pygame.draw.line(screen, const.line_color, (const.horizontal_start_pos_x, const.horizontal_start_pos_y + 30*i), (const.horizontal_end_pos_x, const.horizontal_end_pos_y + 30*i), width=3)
    for i in range(23):
        pygame.draw.line(screen, const.line_color, (const.vertical_start_pos_x + 30*i, const.vertical_start_pos_y), (const.vertical_end_pos_x + 30*i, const.vertical_end_pos_y-1), width=3)

    # Отображаем яблоки
    for i in range(len(apples)):
        screen.blit(apple_serf,(const.x_field_start + 30 * apples[i].x, const.y_field_start + 30 * apples[i].y))

    # Отображаем змейку
    for i in range(len(snake)):
        pygame.draw.rect(screen, (255,0,30), pygame.Rect(const.x_field_start + 30 * snake[i].x, const.y_field_start + 30 * snake[i].y, 30, 30))

    # Рисуем границу поля по которому бегает змейка
    pygame.draw.rect(screen, const.brown_color, pygame.Rect(const.x_field_start - 30, const.y_field_start - 30, const.WIDTH_field + 60, 30))
    pygame.draw.rect(screen, const.brown_color, pygame.Rect(const.x_field_start - 30, const.y_field_start - 30, 30, const.HEIGHT_field + 60))
    pygame.draw.rect(screen, const.brown_color, pygame.Rect( const.WIDTH_field+90, const.y_field_start - 30, 30, const.HEIGHT_field + 60))
    pygame.draw.rect(screen, const.brown_color, pygame.Rect(const.x_field_start - 30, const.HEIGHT_field + const.y_field_start, const.WIDTH_field + 60, 30))

    score_text = f"Ваш счет: {game_points}"
    title_font = pygame.font.Font(None, 58)

    if not exit_window:
        text = font.render(score_text, True, const.light_grey_color)
        screen.blit(text, ((const.WIDTH - len(score_text) * 26)//2, const.y_field_start // 2 - 15))

    if level_window:
        pygame.draw.rect(screen, const.green_color, pygame.Rect(60, 60, const.WIDTH - 120, const.HEIGHT -120))

        pygame.draw.rect(screen, const.grey_color, btn_easy_level, 5)
        pygame.draw.rect(screen, const.grey_color, btn_medium_level, 5)
        pygame.draw.rect(screen, const.grey_color, btn_hard_level, 5)


        btn_font = pygame.font.Font(None, 48)

        title_text = title_font.render("Выберите уровень сложности:", True, const.light_grey_color)
        screen.blit(title_text, (140, const.y_field_start // 2 + 10))

        btn_easy_level_text = btn_font.render(" Легкий", True, const.white_color)
        screen.blit(btn_easy_level_text, (170, const.y_field_start // 2 + 80))

        btn_medium_level_text = btn_font.render(" Средний", True, const.white_color)
        screen.blit(btn_medium_level_text, (170, const.y_field_start // 2 + 160))

        btn_hard_level_text = btn_font.render(" Сложный", True, const.white_color)
        screen.blit(btn_hard_level_text, (170, const.y_field_start // 2 + 240))

    if exit_window:
        global tick
        if tick < 85:
            loose_text = font.render(f"Вы проиграли!", True, const.light_grey_color)
            screen.blit(loose_text, (281, const.y_field_start // 2 - 15))
        # Плавная смена на окно выхода
        if tick >= 70:
            pygame.draw.rect(screen, const.green_color, pygame.Rect(180, 180, const.WIDTH - 360, const.HEIGHT -360))
        if tick >= 75:
            pygame.draw.rect(screen, const.green_color, pygame.Rect(120, 120, const.WIDTH - 240, const.HEIGHT -240))
        if tick >= 80 :
            pygame.draw.rect(screen, const.green_color, pygame.Rect(60, 60, const.WIDTH - 120, const.HEIGHT -120))

            score_text_title = font.render(score_text, True, const.light_grey_color)
            screen.blit(score_text_title, ((const.WIDTH - len(score_text) * 26) // 2, const.y_field_start // 2 + 25))

            pygame.draw.rect(screen, const.grey_color, btn_restart,5)

            btn_restart_text = title_font.render("Начать заново", True, const.white_color)
            screen.blit(btn_restart_text, (110, const.y_field_start // 2 + 180))

            pygame.draw.rect(screen, const.grey_color, btn_exit, 5)

            btn_exit_text = title_font.render("Выйти", True, const.white_color)
            screen.blit(btn_exit_text, (590, const.y_field_start // 2 + 180))
        tick += 1

def direction_of_movement():
    global direction
    global snake_lives
    global old_direction
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if old_direction == "down":
            direction = "down"
        else:
            direction = "up"
    if pressed[pygame.K_DOWN]:
        if old_direction == "up":
            direction = "up"
        else:
            direction = "down"
    if pressed[pygame.K_LEFT]:
        if old_direction == "right":
            direction = "right"
        else:
            direction = "left"
    if pressed[pygame.K_RIGHT]:
        if old_direction == "left":
            direction = "left"
        else:
            direction = "right"

    for i in range(len(snake)):
        if i > 0:
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                snake_lives = "No"
    if snake[0].x < 0 or snake[0].y < 0  or snake[0].x > 23 or snake[0].y > 12 :
        snake_lives = "No"

def move():
    global old_direction
    global game_points
    apple_is_eaten = False

    prev = Point()
    prev.x = snake[0].x
    prev.y = snake[0].y

    if direction == "right":
        prev.x += 1
    elif direction == "left":
        prev.x -= 1
    elif direction == "up":
        prev.y -= 1
    elif direction == "down":
        prev.y += 1

    for i in range(len(apples)):
        if snake[0].x == apples[i].x and snake[0].y == apples[i].y:
            apple_is_eaten = True
            apples.pop(i)
            game_points += 10
            add_aplle()

    if not apple_is_eaten:
        snake.pop()
    snake.insert(0, prev)

    old_direction = direction

def add_aplle():
    need_new_position = True
    is_apple_overlapping_snake = ''
    prev = Point()
    prev.x = random.randint(0,23)
    prev.y = random.randint(0,12)
    while need_new_position:
        for i in range(len(snake)):
            if prev.x == snake[i].x and prev.y == snake[i].y:
                is_apple_overlapping_snake = "Yes"
        if is_apple_overlapping_snake == "Yes":
            need_new_position = True
            prev.x = random.randint(0, 23)
            prev.y = random.randint(0, 12)
        else:
            need_new_position = False
        is_apple_overlapping_snake = ""

    apples.append(prev)

level_window = True
exit_window = False

MOVE_DELAY = 200
last_move_time = pygame.time.get_ticks()

add_aplle()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and level_window:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            if btn_easy_level.collidepoint(event.pos):
                MOVE_DELAY = 200
                level_window = False
            elif btn_medium_level.collidepoint(event.pos):
                MOVE_DELAY = 150
                level_window = False
            elif btn_hard_level.collidepoint(event.pos):
                MOVE_DELAY = 100
                level_window = False

        if event.type == pygame.MOUSEBUTTONDOWN and exit_window:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if btn_restart.collidepoint(event.pos):
                snake = [Point(12, 6)]
                screen.fill(const.background_color)
                snake_lives = 'Yes'
                game_points = 0
                direction = ''
                apples = []
                level_window = True
                exit_window = False
                tick = 0
                add_aplle()
            elif btn_exit.collidepoint(event.pos):
                done = True

    draw()
    current_time = pygame.time.get_ticks()

    if snake_lives != "No" and not level_window:
        if current_time - last_move_time > MOVE_DELAY:
            move()
            last_move_time = current_time
        direction_of_movement()
    elif snake_lives == "No":
        exit_window = True

    draw()
    pygame.display.flip()
    clock.tick(60)
    screen.fill(const.background_color)