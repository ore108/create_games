import pyxel

SCREEN_WIDTH = 120
SCREEN_HEIGHT = 140

GRAVITY = 0.4
JUMP_POWER = -3.5
MOVE_SPEED = 2

TITLE = 0
MAP = 1
GAMECLEAR = 2

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=30, title="ジャンプゲーム")
        self.state = TITLE

        pyxel.load("my_resource.pyxres")
        
        self.player_x = 64
        self.player_y = 112
        self.velocity_y = 0
        self.on_ground = False
        
        
        
        pyxel.run(self.update, self.draw)




    def is_wall(self, x, y):
        tile_x = x // 8
        tile_y = y // 8
        return pyxel.tilemap(0).pget(tile_x, tile_y) == (0, 1)
    
    def is_flag(self, x, y):
        tile_x = x // 8
        tile_y = y // 8
        return pyxel.tilemap(0).pget(tile_x, tile_y) == (2, 0)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if self.state == TITLE and pyxel.btnp(pyxel.KEY_RETURN):
            self.state = MAP
        
        if self.state == MAP:
            next_x = self.player_x
            self.velocity_y += GRAVITY
            next_y = self.player_y + self.velocity_y
            
            if pyxel.btn(pyxel.KEY_LEFT):
                next_x -= MOVE_SPEED
            if pyxel.btn(pyxel.KEY_RIGHT):
                next_x += MOVE_SPEED
            
            if self.on_ground and pyxel.btn(pyxel.KEY_SPACE):
                self.velocity_y = JUMP_POWER
                self.on_ground = False
            
            if not self.is_wall(next_x, self.player_y):
                self.player_x = next_x
            
            if self.velocity_y > 0:  # Falling
                if not self.is_wall(self.player_x, next_y + 7):
                    self.player_y = next_y
                    self.on_ground = False
                else:
                    self.player_y = (self.player_y // 8) * 8
                    self.velocity_y = 0
                    self.on_ground = True
            else:  # Jumping
                if not self.is_wall(self.player_x, next_y):
                    self.player_y = next_y
                else:
                    self.velocity_y = 0
            
            if self.is_flag(self.player_x, self.player_y):
                self.state = GAMECLEAR
        if self.state == GAMECLEAR:
            pyxel.sound()


    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        
        if self.state == TITLE:
            pyxel.text(30, 60, "PRESS ENTER TO START", pyxel.COLOR_WHITE)
        
        if self.state == MAP:
            pyxel.bltm(0, 0, 0, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            pyxel.blt(self.player_x, self.player_y, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK)
        
        if self.state == GAMECLEAR:
            pyxel.text(30, 60, "GAME CLEAR!", pyxel.COLOR_ORANGE)
            pyxel.text(30, 80, "PRESS ESC KEY EXIT", pyxel.COLOR_ORANGE)
            

App()
