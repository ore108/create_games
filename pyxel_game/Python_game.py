import pyxel
import random

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

TITLE = 0
MAP = 1
BATTLE = 2
GAMEOVER = 3

class GAME:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="なんかげーむのてすと")
        self.state = TITLE

        pyxel.load("my_resource.pyxres")

        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT * 4 // 5

        self.stone_x = SCREEN_WIDTH // 2
        self.stone_y = SCREEN_HEIGHT // 2

        self.hit_flag = False
        self.walk_frame = 0

        pyxel.run(self.update, self.draw)

    def is_wall(self, x, y):
        tile_x = x // 8
        tile_y = y // 8

        if pyxel.tilemap(0).pget(tile_x, tile_y) == (6, 0):
            return True
        return False

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if self.state == TITLE and pyxel.btnp(pyxel.KEY_RETURN):
            self.state = MAP

        if self.state == MAP:
            next_x = self.player_x
            next_y = self.player_y

            if pyxel.btnp(pyxel.KEY_UP):
                next_y -= 8
                self.walk_frame = (self.walk_frame + 1) % 4
            if pyxel.btnp(pyxel.KEY_DOWN):
                next_y += 8
                self.walk_frame = (self.walk_frame + 1) % 4
            if pyxel.btnp(pyxel.KEY_LEFT):
                next_x -= 8
                self.walk_frame = (self.walk_frame + 1) % 4
            if pyxel.btnp(pyxel.KEY_RIGHT):
                next_x += 8
                self.walk_frame = (self.walk_frame + 1) % 4

            if not self.is_wall(next_x, next_y):
                self.player_x = next_x
                self.player_y = next_y

    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)

        if self.state == TITLE:
            pyxel.text(50, 60, "PRESS ENTER TO START", pyxel.COLOR_WHITE)

        if self.state == MAP:
            pyxel.bltm(0, 0, 0, 0, 0, 2400, 1600)
            pyxel.blt(self.stone_x, self.stone_y, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK)

            motion_x = [2, 3, 2, 3][self.walk_frame % 4]
            motion_y = [0, 0, 1, 1][self.walk_frame % 4]
            pyxel.blt(self.player_x, self.player_y, 0, motion_x * 8, motion_y * 8, 8, 8, pyxel.COLOR_BLACK)

GAME()
