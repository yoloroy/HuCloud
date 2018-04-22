from GUI import *


pygame.init()
size = 800, 400
screen = pygame.display.set_mode(size)

""" 0 - main menu
    1 - main
    2 - settings
    3 - exit       """
mode = 0

def change_mode(new_mode):
    global mode
    mode = new_mode

def back_to_color(back, new_color):
    size = back.get_size()
    for x in range(size[0]):
        for y in range(size[1]):
            back.set_at((x, y), back.get_at((x, y)) + to_color(new_color))
    return back


# main menu
bt_main = Button((size[0] * .02, size[1] * .5,
                             size[0] * .25, size[1] * .075),
                             "Хранение", text_color=(255, 255, 255))
bt_settings = Button((size[0] * .02, size[1] * .6,
                                 size[0] * .25, size[1] * .075),
                                 "Настройки", text_color=(255, 255, 255))
bt_exit = Button((size[0] * .02, size[1] * .7,
                             size[0] * .25, size[1] * .075),
                             "Выход", text_color=(255, 255, 255))
mm_bg = pygame.transform.scale(pygame.image.load('data/mm_back.jpg'),
                               size)
mm_GUI = GUI(bt_main, bt_settings, bt_exit)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.event.clear()

    if mode == 0:
        screen.blit(back_to_color(mm_bg, (255, 0, 0)),
                    (0, 0))
        mm_GUI.render(screen)
    pygame.display.flip()


pygame.quit()
