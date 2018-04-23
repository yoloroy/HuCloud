from GUI import *
from json import loads, dump

_settings = loads(open("settings.json", "r").read())

pygame.init()
size = 800, 400
screen = pygame.display.set_mode(size)

""" 0 - main menu
    1 - main
    2 - settings
    3 - exit       """
mode = -1

def update_settings():
    global _settings
    _settings = loads(open("settings.json", "r").read())

def back_to_color(back, new_color):
    back = back.copy()
    size = back.get_size()
    print(back.get_at((size[0]-1, size[1]-1)), new_color)
    for x in range(size[0]):
        for y in range(size[1]):
            back.set_at((x, y), back.get_at((x, y)) +
                        to_color(tuple(reversed(new_color))))

    return back

def newcolor(*result):
    update_settings()
    if result[0]:
        mode = result[-1]
        print(result)
        _settings[str(mode)] = tuple(result[0][0][:-1])
        dump(_settings, open("settings.json", "w"), indent=4)


def change_mode(new_mode):
    global gui
    global mode
    global bg
    mode = new_mode

    if mode == 0:
        main = Button((size[0] * .02, size[1] * .5,
                          size[0] * .25, size[1] * .075),
                         "Хранение", text_color=(255, 255, 255),
                         click_event=(lambda self: change_mode(1)))
        settings = Button((size[0] * .02, size[1] * .6,
                              size[0] * .25, size[1] * .075),
                             "Настройки", text_color=(255, 255, 255),
                          click_event=(lambda self: change_mode(2)))
        exi = Button((size[0] * .02, size[1] * .7,
                          size[0] * .25, size[1] * .075),
                         "Выход", text_color=(255, 255, 255),
                         click_event=(lambda self: pygame.quit()))
        bg = pygame.transform.scale(pygame.image.load('data/mm_back.jpg'),
                                       size)
        gui = GUI(main, settings, exi)
    elif mode == 1:
        exi = Button((size[0] * .02, size[1] * .7,
                         size[0] * .25, size[1] * .075),
                        "Выход", text_color=(255, 255, 255),
                        click_event=(lambda self: change_mode(0)))
        bg = pygame.transform.scale(pygame.image.load('data/m_back.jpg'),
                                      size)
        gui = GUI(exi)
    elif mode == 2:
        mm_palette = Button((size[0] * .02, size[1] * .4,
                              size[0] * .25, size[1] * .075),
                            "Choice main menu color",
                            text_color=(255, 255, 255),
                            click_event=(lambda self: newcolor(palette(), 0)))
        m_palette = Button((size[0] * .02, size[1] * .5,
                              size[0] * .25, size[1] * .075),
                           "Choice main color",
                           text_color=(255, 255, 255),
                           click_event=(lambda self: newcolor(palette(), 1)))
        st_palette = Button((size[0] * .02, size[1] * .6,
                          size[0] * .25, size[1] * .075),
                            "Choice settings menu color",
                            text_color=(255, 255, 255),
                            click_event=(lambda self: newcolor(palette(), 2)))
        exi = Button((size[0] * .02, size[1] * .7,
                      size[0] * .25, size[1] * .075),
                     "Выход", text_color=(255, 255, 255),
                     click_event=(lambda self: change_mode(0)))
        bg = pygame.transform.scale(pygame.image.load('data/m_back.jpg'),
                                    size)
        gui = GUI(mm_palette, m_palette, st_palette, exi)



# main menu
change_mode(0)

# main
# change_mode(1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.event.clear()

        for i in gui.element:
            i.get_event(event)

    bag = back_to_color(bg, _settings[str(mode)])
    screen.blit(bag,
                (0, 0))
    gui.render(screen)
    pygame.display.flip()


pygame.quit()
