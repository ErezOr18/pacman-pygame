import pygame
import extensions

done = False
from sprites.player import Player


def create_sprites():
    player = Player("res/sprite/pacman.gif", (100, 100))
    return player


def update_screen(sprites: list[pygame.sprite.Sprite]) -> list[pygame.Rect]:
    res = []
    for sprite in sprites:
        res.append(extensions.DISPLAY.blit(sprite.image, sprite.rect))
    pygame.display.flip()
    return res


def main():
    global done
    player = create_sprites()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        update_screen([player])


if __name__ == '__main__':
    main()
