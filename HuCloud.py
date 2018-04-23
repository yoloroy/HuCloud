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
    back = back.copy()
    size = back.get_size()
    print(back.get_at((size[0]-1, size[1]-1)))
    for x in range(size[0]):
        for y in range(size[1]):
            back.set_at((x, y), back.get_at((x, y)) + to_color(tuple(reversed(new_color))))
    return back


# main menu
mm_main = Button((size[0] * .02, size[1] * .5,
                  size[0] * .25, size[1] * .075),
                 "Хранение", text_color=(255, 255, 255),
                 click_event=(lambda self:change_mode(1)))
mm_settings = Button((size[0] * .02, size[1] * .6,
                      size[0] * .25, size[1] * .075),
                     "Настройки", text_color=(255, 255, 255))
mm_exit = Button((size[0] * .02, size[1] * .7,
                  size[0] * .25, size[1] * .075),
                 "Выход", text_color=(255, 255, 255),
                 click_event=(lambda self: pygame.quit()))
mm_bg = pygame.transform.scale(pygame.image.load('data/mm_back.jpg'),
                               size)
mm_GUI = GUI(mm_main, mm_settings, mm_exit)

# main
m_exit = Button((size[0] * .02, size[1] * .7,
                 size[0] * .25, size[1] * .075),
                "Выход", text_color=(255, 255, 255),
                click_event=(lambda self: change_mode(0)))
m_bg = pygame.transform.scale(pygame.image.load('data/m_back.jpg'),
                              size)
m_GUI = GUI(m_exit)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.event.clear()

        if mode == 0:
            mm_exit.get_event(event)
            mm_settings.get_event(event)
            mm_main.get_event(event)
        elif mode == 1:
            m_exit.get_event(event)

    screen.blit(back_to_color(bg, (100, 0, 0)),
                (0, 0))
    GUI.render(screen)
    pygame.display.flip()


pygame.quit()
