import pygame,random,math
from pygame.locals import *
TreeImg = pygame.image.load("overworld/trees.png")
TreeImg2 = pygame.image.load("overworld/single_trees.png")
TreeImg3 = pygame.image.load("overworld/single_tree.png")
RockImg = pygame.image.load("overworld/rocks.png")
DestRock = pygame.image.load("overworld/explodable_rocks.png")
Oldie = pygame.image.load("misc/old_man.png")
dungeon_rock = pygame.image.load("overworld/dungeon_rocks.png")
Water1 = pygame.image.load("overworld/water.png")
Water2 = pygame.image.load("overworld/water_right.png")
Water3 = pygame.image.load("overworld/water_right_inverse.png")
water1 = pygame.image.load("overworld/water/0.png")
water2 = pygame.image.load("overworld/water/1.png")
water3 = pygame.image.load("overworld/water/2.png")
water4 = pygame.image.load("overworld/water/3.png")
water5 = pygame.image.load("overworld/water/4.png")
water6 = pygame.image.load("overworld/water/5.png")
water7 = pygame.image.load("overworld/water/6.png")
water8 = pygame.image.load("overworld/water/7.png")
water9 = pygame.image.load("overworld/water/8.png")
Zelda = pygame.image.load("misc/zelda.png")
Win = pygame.image.load("misc/final.jpg")
class Zeb(pygame.sprite.Sprite):
    
    def __init__(self, x, y,DIRECTION,upKeyPressed,downKeyPressed,leftKeyPressed,rightKeyPressed, spacePressed,has_sword,has_bombs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Zeb/Zeb_up1.png")
        self.right1 = pygame.image.load("Zeb/walk_right1.png")
        self.right2 = pygame.image.load("Zeb/Zeb_right2.png")
        self.left1 = pygame.image.load("Zeb/Zeb_left1.png")
        self.left2 = pygame.image.load("Zeb/Zeb_left2.png")
        self.up1 = pygame.image.load("Zeb/Zeb_up1.png")
        self.up2 = pygame.image.load("Zeb/Zeb_up2.png")
        self.down1 = pygame.image.load("Zeb/Zeb_down1.png")
        self.down2 = pygame.image.load("Zeb/Zeb_down2.png")
        self.attack_right = pygame.image.load("Zeb/attack_right.png")
        self.attack_left = pygame.image.load("Zeb/attack_left.png")
        self.attack_up = pygame.image.load("Zeb/attack_up.png")
        self.attack_down = pygame.image.load("Zeb/attack_down.png")
        self.right_walk = [self.right1,self.right2]
        self.left_walk = [self.left1, self.left2]
        self.up_walk = [self.up1, self.up2]
        self.down_walk = [self.down1,self.down2]
        self.ticker = 0
        self.current_frame = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x_left = 0
        self.change_x_right = 0
        self.change_y_up = 0
        self.change_y_down = 0
        self.walls = None
        self.mobs = None
        self.items = None
        self.bomb_items = None
        self.keys = None
        self.locks = None
        self.DIRECTION = DIRECTION
        self.upKeyPressed = upKeyPressed
        self.downKeyPressed = downKeyPressed
        self.leftKeyPressed = leftKeyPressed
        self.rightKeyPressed = rightKeyPressed
        self.spacePressed = spacePressed
        self.WALKRATE = 5
        self.RIGHT, self.LEFT, self.UP, self.DOWN = "right left up down".split()
        self.action = 'walking'
        self.has_sword = has_sword
        self.effect = pygame.mixer.Sound("SFX/LOZ_Sword.wav")
        self.item_find = pygame.mixer.Sound("SFX/LOZ_Get_Item.wav")
        self.item_find.set_volume(.3)
        self.secret = pygame.mixer.Sound("SFX/LOZ_Secret.wav")
        self.secret.set_volume(.6)
        self.enter_door = False
        self.enter_door2 = False
        self.enter_door3 = False
        self.in_dungeon = False
        self.can_move = True
        self.has_key = False
        self.has_bombs = False
        self.bombs = pygame.sprite.Group()
    def walk(self):
        pass
    
    def update(self):
        
        if self.downKeyPressed:
            self.rect.y += 5
            self.image = self.down_walk[self.current_frame]
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            mob_hit_list = pygame.sprite.spritecollide(self, self.mobs, False)
            item_hit_list = pygame.sprite.spritecollide(self, self.items, False)
            bomb_items_hit_list = pygame.sprite.spritecollide(self, self.bomb_items,False)
            key_hit_list = pygame.sprite.spritecollide(self,self.keys,False)
            lock_hit_list = pygame.sprite.spritecollide(self, self.locks, False)
            door_list3 = pygame.sprite.spritecollide(self, self.doors3, False)
            for wall in wall_hit_list:
                self.rect.bottom = wall.rect.top
            for mob in mob_hit_list:
                if mob.hitpoint > 0:
                    self.rect.bottom = mob.rect.top
            for item in item_hit_list:
                self.rect.bottom = item.rect.top
                self.has_sword = True
                self.item_find.play()
                item.kill()
            for key in key_hit_list:
                if self.rect.bottom == key.rect.top:
                    self.has_key = True
                    
            for bombitem in bomb_items_hit_list:
                bombitem.kill()
                self.has_bombs = True
                self.item_find.play()
                    
            for lock in lock_hit_list:
                self.rect.bottom == lock.rect.top
                if self.has_key:
                    lock.kill()
                    self.secret.play()
            if door_list3:
                self.enter_door3 = True
                self.rect.x = 400
                self.rect.y = 200
                    
                    
        elif self.upKeyPressed:
            self.rect.y -= 5
            self.image = self.up_walk[self.current_frame]
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            mob_hit_list = pygame.sprite.spritecollide(self, self.mobs, False)
            item_hit_list = pygame.sprite.spritecollide(self, self.items, False)
            bomb_items_hit_list = pygame.sprite.spritecollide(self,self.bomb_items,False)
            door_list = pygame.sprite.spritecollide(self, self.doors, False)
            door_list2 = pygame.sprite.spritecollide(self, self.doors2, False)

            key_hit_list = pygame.sprite.spritecollide(self,self.keys,False)
            lock_hit_list = pygame.sprite.spritecollide(self, self.locks, False)

            for wall in wall_hit_list:
               self.rect.top = wall.rect.bottom
            for mob in mob_hit_list:
                if mob.hitpoint > 0:
                    self.rect.top = mob.rect.bottom
            for item in item_hit_list:
                self.rect.top = item.rect.bottom
                self.has_sword = True
                self.item_find.play()
                item.kill()
            for key in key_hit_list:
                if self.rect.top == key.rect.bottom:
                    self.has_key = True
            for lock in lock_hit_list:
                self.rect.top = lock.rect.bottom
                if self.has_key:
                    lock.kill()
                    self.secret.play()
            for bombitem in bomb_items_hit_list:
                bombitem.kill()
                self.has_bombs = True
                self.item_find.play()
                
            if door_list:
                self.enter_door = True
                self.rect.x = 300
                self.rect.y = 500
            if door_list2 and self.has_key:
                self.enter_door2 = True
                self.rect.x = 400
                self.rect.y = 500
                
        elif self.leftKeyPressed:
            self.rect.x -= 5
            self.image = self.left_walk[self.current_frame]
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            mob_hit_list = pygame.sprite.spritecollide(self, self.mobs, False)
            item_hit_list = pygame.sprite.spritecollide(self, self.items, False)
            bomb_items_hit_list = pygame.sprite.spritecollide(self,self.bomb_items,False)
            key_hit_list = pygame.sprite.spritecollide(self,self.keys,False)
            for wall in wall_hit_list:
                self.rect.left = wall.rect.right
            for mob in mob_hit_list:
                if mob.hitpoint > 0:
                    self.rect.left = mob.rect.right
            for item in item_hit_list:
                self.rect.left = item.rect.right
                self.has_sword = True
                self.item_find.play()
                item.kill()
            for key in key_hit_list:
                if self.rect.left == key.rect.right:
                    self.has_key = True
                    
            for bombitem in bomb_items_hit_list:
                bombitem.kill()
                self.has_bombs = True
                self.item_find.play()

        elif self.rightKeyPressed:
            self.rect.x += 5
            self.image = self.right_walk[self.current_frame]
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            mob_hit_list = pygame.sprite.spritecollide(self, self.mobs, False)
            item_hit_list = pygame.sprite.spritecollide(self, self.items, False)
            bomb_items_hit_list = pygame.sprite.spritecollide(self,self.bomb_items,False)
            key_hit_list = pygame.sprite.spritecollide(self, self.keys,False)
            for wall in wall_hit_list:
                self.rect.right = wall.rect.left
            for mob in mob_hit_list:
                if mob.hitpoint > 0:
                    self.rect.right = mob.rect.left
            for item in item_hit_list:
                self.rect.right= item.rect.left
                self.has_sword = True
                self.item_find.play()
                item.kill()
            for key in key_hit_list:
                if self.rect.right == key.rect.left:
                    self.has_key = True
            for bombitem in bomb_items_hit_list:
                bombitem.kill()
                self.has_bombs = True
                self.item_find.play()
        elif self.spacePressed:
            if self.action == "attacking":
                mob_hit_list = pygame.sprite.spritecollide(self, self.mobs, False)
                wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
                for mob in mob_hit_list:
                    if self.rect.colliderect(mob):
                        if self.DIRECTION == self.UP:
                            #mob.rect.y = mob.rect.y - 15
                            mob.hitpoint -= 1
                        if self.DIRECTION == self.LEFT:
                            #mob.rect.x -= 15
                            mob.hitpoint -= 1
                        if self.DIRECTION == self.RIGHT:
                            #mob.rect.x += 15
                            mob.hitpoint -= 1
                        if self.DIRECTION == self.DOWN:
                            #mob.rect.y += 15
                            mob.hitpoint -= 1

            
        self.ticker += 1
        if self.ticker % 8 == 0:
            self.current_frame = (self.current_frame + 1) % 2
class Mob(pygame.sprite.Sprite):
    def __init__(self,x,y,hitpoint,game):
        self.left1 = pygame.image.load("Enemy/0.png")
        self.left2 = pygame.image.load("Enemy/1.png")
        self.down1 = pygame.image.load("Enemy/2.png")
        self.down2 = pygame.image.load("Enemy/3.png")
        self.right1 = pygame.image.load("Enemy/4.png")
        self.right2 = pygame.image.load("Enemy/5.png")
        self.up1 = pygame.image.load("Enemy/6.png")
        self.up2 = pygame.image.load("Enemy/7.png")
        self.left_walk = [self.left1,self.left2]
        self.right_walk = [self.right1, self.right2]
        self.up_walk = [self.up1, self.up2]
        self.down_walk = [self.down1, self.down2]
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(0,0,48,48)
        self.image = pygame.image.load("Enemy/0.png")
        self.rect.x = x
        self.rect.y = y
        self.one = pygame.image.load("misc/0.png")
        self.two = pygame.image.load("misc/1.png")
        self.three= pygame.image.load("misc/2.png")
        self.die = [self.one,self.two,self.three]
        self.ticker = 0
        self.current_frame = 0
        self.walk_anim_frame = 0
        self.hitpoint = hitpoint
        self.x_change = 1
        self.t = 0
        self.timer = random.randint(60,180)
        self.arrow_timer = random.randint(0,120)
        self.arrow_t = 0
        self.randomDirections = ["up", "down","left","right"]
        self.randomnumber = random.randint(0,3)
        self.direction = self.randomDirections[self.randomnumber]
        self.walls = None
        self.doors = None
        self.x_change = 1
        self.y_change = 1
        self.anim_ticker = 0
        self.game = game
        self.effect = pygame.mixer.Sound("SFX/LOZ_Kill.wav")
        self.effect.set_volume(.4)
        self.has_bomb = True
        
    def update(self):
        if self.direction == "right":
            self.image = self.right_walk[self.walk_anim_frame]
            self.rect.x += self.x_change
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for wall in wall_hit_list:
                self.rect.right = wall.rect.left
                self.direction = self.randomDirections[2]
            self.t += 1
            if self.arrow_t >= self.arrow_timer:
                self.game.arrows.add(Mob_Arrow(self.rect.x, self.rect.y, self.direction))
                self.arrow_t = 0
                self.arrow_timer = random.randint(60,240)
            self.arrow_t += 1
            if self.t == self.timer: 
              self.direction = self.randomDirections[random.randint(0,3)]
              self.t = 0
            
        elif self.direction == "left":
            self.image = self.left_walk[self.walk_anim_frame]
            self.rect.x -= self.x_change
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for wall in wall_hit_list:
                self.rect.left = wall.rect.right
                self.direction = self.randomDirections[3]
            self.t += 1
            self.arrow_t += 1
            if self.arrow_t >= self.arrow_timer:
                self.game.arrows.add(Mob_Arrow(self.rect.x, self.rect.y, self.direction))
                self.arrow_t = 0
                self.arrow_timer = random.randint(60,240)
            if self.t == self.timer:
                self.direction = self.randomDirections[random.randint(0,3)]
                self.t = 0
        elif self.direction == "up":
            self.image = self.up_walk[self.walk_anim_frame]
            self.rect.y -= self.y_change
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for wall in wall_hit_list:
                self.rect.top = wall.rect.bottom
                self.direction = self.randomDirections[1]

            self.t += 1
            self.arrow_t += 1
            if self.arrow_t >= self.arrow_timer:
                self.game.arrows.add(Mob_Arrow(self.rect.x, self.rect.y, self.direction))
                self.arrow_t = 0
                self.arrow_timer = random.randint(60,240)
            if self.t == self.timer:
                self.direction = self.randomDirections[random.randint(0,3)]
                self.t = 0

        elif self.direction == "down":
            self.image = self.down_walk[self.walk_anim_frame]
            self.rect.y += self.y_change
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for wall in wall_hit_list:

                self.rect.bottom = wall.rect.top
                self.direction = self.randomDirections[0]
            self.t += 1
            self.arrow_t += 1
            if self.arrow_t >= self.arrow_timer:
                self.game.arrows.add(Mob_Arrow(self.rect.x, self.rect.y, self.direction))
                self.arrow_t = 0
                self.arrow_timer = random.randint(60,240)
            if self.t == self.timer:
                self.direction = self.randomDirections[random.randint(0,3)]
                self.t = 0
            
                
        if self.hitpoint <= 0:
            self.arrow_t = -1
            self.x_change = 0
            self.y_change = 0
            self.rect.y = self.rect.y
            self.image = self.die[self.current_frame]
            self.ticker += 1
            if self.ticker % 15 == 0:
                self.current_frame = (self.current_frame + 1) % 3
            if self.image == self.die[2]:
                self.kill()
                self.effect.play()
                
        self.anim_ticker += 1
        if self.anim_ticker % 10 == 0:
            self.walk_anim_frame = (self.walk_anim_frame + 1) % 2

        
            
class Mob_Arrow(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        if self.direction == "right":
            self.image = pygame.image.load("Enemy/Slimes/Slime3.png")
        elif self.direction == "left":
            self.image = pygame.image.load("Enemy/Slimes/Slime1.png")
        elif self.direction == "up":
            self.image = pygame.image.load("Enemy/Slimes/Slime4.png")
        elif self.direction == "down":
            self.image = pygame.image.load("Enemy/Slimes/Slime2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        if self.direction == "right":
            self.rect.x += 6
        elif self.direction == "left":
            self.rect.x -= 6
        elif self.direction == "up":
            self.rect.y -= 6
        elif self.direction == "down":
            self.rect.y += 6
class Bomb(pygame.sprite.Sprite):
    def __init__(self, x,y, Zeb):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load("bombs/bombs.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.hit_rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 100
        self.one = pygame.image.load("misc/00.png")
        self.two = pygame.image.load("misc/1.png")
        self.three= pygame.image.load("misc/2.png")
        self.explode = [self.one,self.two,self.three]
        self.current_frame = 0
        self.ticker = 0
        self.Zeb = Zeb
        self.effect = pygame.mixer.Sound("SFX/LOZ_Bomb_Blow.wav")

    def update(self):
        self.hit_rect = self.image.get_rect()
        self.hit_rect.x = self.x
        self.hit_rect.y = self.y
        block_hit_list = [block for block in self.Zeb.walls if self.hit_rect.colliderect(block.rect)]
        for block in block_hit_list:
            if type(block) == Rock:
                block.kill()
            if block.destructible:
                block.kill()
        self.timer -= 1
        if self.timer == 0:
            self.rect.x -= 25
            self.rect.y -= 15
        if self.timer <= 0:
            self.ticker = self.ticker + 1
            self.image = self.explode[self.current_frame]
            if self.ticker % 15 == 0:
                self.effect.play()
                self.kill()

        
        
        
        
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = False
class Rock(pygame.sprite.Sprite):
    def __init__(self,x,y,destructible,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = RockImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = destructible
        self.image = image

    def __str__(self):
        return "I am a rock", self.destructible
class DungeonRock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = dungeon_rock
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = False
        
class Water(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = False
        
class Door(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Zeb/walk_right1.png")
        self.rect = self.image.get_rect()
        self.image.fill(Color("Black"))
        self.rect.x = x
        self.rect.y = y
        self.destructible = False
class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("0.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class BombCollectable(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Bombs/bombs.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Text(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("32-2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Key(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("misc/key.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Lock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("misc/lock.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Room(object):
    wall_list = None
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.mob_list = pygame.sprite.Group()
        self.arrows = pygame.sprite.Group()
        self.item_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.door_list2 = pygame.sprite.Group()
        self.door_list3 = pygame.sprite.Group()
        self.key_list = pygame.sprite.Group()
        self.lock_list = pygame.sprite.Group()
        self.bombs_items_list = pygame.sprite.Group()
        self.dungeon = False
        
class Room1(Room):
    def __init__(self):
        Room.__init__(self)
        walls = [Wall(0,0,TreeImg), Wall(256,0,TreeImg),Wall(500,0,TreeImg), Wall((900-256),0,TreeImg), Wall(-160,113,TreeImg),
                 Wall(-160,226,TreeImg),Wall(-160,440,TreeImg), Wall(-160, 553,TreeImg),
                 Wall((900-150),113,TreeImg),Wall((900-150),226,TreeImg),
                 Water((800-216),443, water1),Water((800-168),443, water2),
                 Water((800-120),443, water2),Water((800-82),443, water2),Water((800-34),443, water2),
                 Water((800-34),491, water9),Water((800-34),539, water9),Water((800-34),580, water9),
                 Water((800-82),580, water9),Water((800-120),580, water9),Water((800-168),580, water9),
                 Water((800-168),580, water9),Water((800-216),580, water8),Water((800-216),539, water8),
                 Water((800-216),491, water8),Water((800-168),580, water9),Water((800-120),580, water9),
                 Water((800-82),539, water9),Water((800-34),539, water9),Water((800-82),491, water9),
                 Water((800-120),491, water9),Water((800-168),491, water9),Water((800-82),491, water9),
                 Water((800-168),539, water9),Water((800-120),539, water9),
                 Wall(700,0,TreeImg),
                 Wall(75,553,TreeImg),Wall(200,553,TreeImg),Wall(330,553,TreeImg)]
        doors = [Door(300,66)]
        for wall in walls:
            self.wall_list.add(wall)
        for door in doors:
            self.door_list.add(door)
class Room2(Room):
    def __init__(self):
        Room.__init__(self)
        walls = [Water(0,443, Water2),Wall(213,500,TreeImg), Wall(326,500,TreeImg),
                 Rock(0,0,False,RockImg),Rock(-500,120,False,RockImg),Rock(-500,200,False,RockImg), Wall(439,500,TreeImg),Wall(551,500,TreeImg),
                 Wall(750,0,TreeImg),Wall(750, 339,TreeImg),Wall(750,451,TreeImg),Wall(750,113,TreeImg),
                  Wall(750,226,TreeImg)]
        mobs = [Mob(400,200,5,self),Mob(500,300,5,self),Mob(500,400,5,self)]
        self.keys = [Key(300,300)]
        for wall in walls:
            self.wall_list.add(wall)
        for mob in mobs:
            mob.walls = self.wall_list
            self.mob_list.add(mob)
        for key in self.keys:
            self.key_list.add(key)
        

            
class Room3(Room):
    def __init__(self):
        Room.__init__(self)
        walls = [Wall(0,0,TreeImg2), Wall(-400,140,TreeImg2),Wall(-400,280,TreeImg2),Wall(-400,400,TreeImg2), Wall(700,440,TreeImg),Wall(700,553,TreeImg),
                 Wall(500,553,TreeImg),Wall(700,226,TreeImg),Wall(700,113,TreeImg),Wall(700,0,TreeImg),Rock(355,553,True,DestRock),Wall(100,553,TreeImg),Wall(0,553,TreeImg)]
        mobs = [Mob(200,200,1,self),Mob(300,300,1,self),Mob(400,400,1,self)]
        
        #locks = [Lock(400,400)]
        for wall in walls:
            self.wall_list.add(wall)
        for mob in mobs:
            mob.walls = self.wall_list
            self.mob_list.add(mob)
        
        
                     
class Room4(Room):
    def __init__(self):
        Room.__init__(self)
        walls = [Wall(0,0,Water3),Wall(200,0,RockImg),Wall(-100,520,RockImg),Wall(500,520,RockImg)]
        mobs = [Mob(400,400,7,self),Mob(400,400,1,self),Mob(400,400,1,self)]
        locks = [Lock(400,98)]
        doors = [Door(400,97)]
        for wall in walls:
            self.wall_list.add(wall)
        for mob in mobs:
            mob.walls = self.wall_list
            self.mob_list.add(mob)
        for lock in locks:
            self.lock_list.add(lock)
        for door in doors:
            self.door_list2.add(door)
            
class Room5(Room):
    def __init__(self):
        Room.__init__(self)
        walls = [Wall(0,520,TreeImg2),Wall(90,520,TreeImg2),Wall(750,113,TreeImg),Wall(750,0,TreeImg),Wall(750,226,TreeImg),
                 Wall(750,339,TreeImg),Wall(750,440,TreeImg),Wall(750,553,TreeImg),Rock(0,0,False,RockImg),Rock(220,0,False,RockImg), Wall(400,400,TreeImg3),
                 Wall(500,300,TreeImg3),Wall(200,200,TreeImg3),Wall(200,400,TreeImg3)]
        for wall in walls:
            self.wall_list.add(wall)
        
class Room6(Room):
    def __init__(self):
        Room.__init__(self)
        walls = [Wall(0,48,TreeImg),Wall(256,48,TreeImg),Wall(500,48,TreeImg),Wall(700,48,TreeImg),
                 Wall(0,0,TreeImg),Wall(256,0,TreeImg),Wall(500,0,TreeImg),Wall(700,0,TreeImg),
                 Wall(0,123,TreeImg),Wall(0,230,TreeImg),Wall(0,340,TreeImg),Wall(0,440,TreeImg),Wall(0,550,TreeImg),
                 Wall(0,553,TreeImg),Wall(250,553,TreeImg),Wall(275,553,TreeImg),Wall(700,553,TreeImg)]
        for wall in walls:
            self.wall_list.add(wall)
class Room7(Room):
    def __init__(self):
        Room.__init__(self)
        walls = [Wall(-256,-30,RockImg), Wall(-500,100,RockImg),Wall(-500,200,RockImg),
                 Wall(-500,300,RockImg),Wall(-500,400,RockImg),Wall(-500,500,RockImg),Wall(0,500,RockImg),Wall(400,500,RockImg),
                 Wall(700,100,RockImg),Wall(700,200,RockImg),Wall(700,300,RockImg),Wall(700,400,RockImg),Wall(700,500,RockImg),
                 Wall(544,-30,RockImg)]
        doors = [Door(400,500)]
        for wall in walls:
            self.wall_list.add(wall)
        for door in doors:
            self.door_list3.add(door)
##        for mob in mobs:
##            mob.walls = self.wall_list
##            self.mob_list.add(mob)
class Dungeon(Room):
    def __init__(self):
        Room.__init__(self)
        self.dungeon = True
        items = [Sword(390,250), Text(1,0)]
        walls = [DungeonRock(0,-50), DungeonRock(400,-50), DungeonRock(-550,90),
                 DungeonRock(-550,220),DungeonRock(-550,300),DungeonRock(-550,400),DungeonRock(738,90),
                 DungeonRock(738,220),DungeonRock(738,300),DungeonRock(738,400),DungeonRock(-375,500),
                 DungeonRock(570,500), Wall(382,175,Oldie)]
        doors = []
        for wall in walls:
            self.wall_list.add(wall)
        for item in items:
            self.item_list.add(item)
class Dungeon2(Room):
    def __init__(self):
        Room.__init__(self)
        self.dungeon = True
        walls = [DungeonRock(0,-50), DungeonRock(400,-50), DungeonRock(-550,90),
                 DungeonRock(-550,220),DungeonRock(-550,300),DungeonRock(-550,400),DungeonRock(738,90),
                 DungeonRock(738,220),DungeonRock(738,300),DungeonRock(738,400),DungeonRock(-375,500),
                 DungeonRock(570,500)]
        bomb_items = [BombCollectable(400,200)]
        doors = []
        mobs = []
        for wall in walls:
            self.wall_list.add(wall)
        for item in bomb_items:
            self.bombs_items_list.add(item)
        for mob in mobs:
            self.mob_list.add(mob)
class FINAL_DUNGEON(Room):
    def __init__(self):
        Room.__init__(self)
        self.dungeon = True
        walls = [DungeonRock(0,500), DungeonRock(400,500), DungeonRock(-550,90),
                 DungeonRock(-550,220),DungeonRock(-550,300),DungeonRock(-550,400),DungeonRock(738,90),
                 DungeonRock(738,220),DungeonRock(738,300),DungeonRock(738,400),DungeonRock(-200,-50),DungeonRock(600,-50),
                 Wall(380,300,Zelda),Wall(300,400,Win)]
        mobs = []
        doors = []
        for wall in walls:
            self.wall_list.add(wall)
        for mob in mobs:
            self.mob_list.add(mob)
        for door in doors:
            self.door_list.add(door)
        
class GameMain():
    done = False
   
    def __init__(self,width = 800, height = 600):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        
        
        self.color_x = 109
        self.color_y = 247
        self.color_z = 177
        self.width, self.height = width, height
        pygame.display.set_caption("AshmoleanProjectPygame")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.Zeb = Zeb(200,500,"UP",False,False,False,False,False,False,False)        
        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.Zeb)
        self.rooms = [[Room3(),Room1(),Room2()],
                      [Room6(),Room4(), Room5()],
                      [Room7(),Dungeon(),Dungeon2(),FINAL_DUNGEON()]]
        self.current_x = 1
        self.current_y = 0
        self.current_room = self.rooms[self.current_y][self.current_x]
        self.Zeb.walls = self.rooms[self.current_y][self.current_x].wall_list
        self.Zeb.mobs = self.rooms[self.current_y][self.current_x].mob_list
        self.Zeb.bomb_items = self.rooms[2][2].bombs_items_list
        self.Zeb.items = self.current_room.item_list
        self.Zeb.doors = self.current_room.door_list
        self.Zeb.doors2 = self.current_room.door_list2
        self.Zeb.doors3 = self.rooms[self.current_y][self.current_x].door_list3
        self.Zeb.keys = self.rooms[0][2].keys
        self.Zeb.locks = self.current_room.lock_list

        

        self.current_screen = "title"
        
    def main_loop(self):
        pygame.mixer.music.load("music/Zelda - Breath of the Wild - Main Theme【8-BIT】♪.ogg")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.5)
        while not self.done:
            if self.current_screen == "game":
                self.handle_events()
                self.draw()
                self.all_sprite_list.update()
                self.Zeb.mobs.update()
                self.Zeb.bombs.update()
                self.current_room.arrows.update()
                self.change_room()
                arrow_hit_list = self.current_room.arrows
                for arrow in arrow_hit_list:
                    if pygame.sprite.collide_rect(self.Zeb, arrow) and self.Zeb.action == "attacking":
                        arrow.kill()
                    elif pygame.sprite.collide_rect(self.Zeb, arrow) and self.Zeb.action == "walking":
                        #print "oww"
                        self.Zeb.kill()
            elif self.current_screen == "title":
                self.handle_events_title()
                self.draw_title()
            self.clock.tick(60)
        
        pygame.quit()
        
    def draw_title(self):
        self.screen.fill(Color("Grey"))
        logo = pygame.image.load("logo.png")
        credit = pygame.image.load("credits.png")
        self.screen.blit(logo,(220,200))
        self.screen.blit(credit,(240,443))
        pygame.display.flip()
    def handle_events_title(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.current_screen = "game"
        
    def draw(self):
        if self.current_room.dungeon:
            self.screen.fill(Color("black"))
        else:
            self.screen.fill((self.color_x, self.color_y, self.color_z))
        self.all_sprite_list.draw(self.screen)
        self.current_room.wall_list.draw(self.screen)
        self.current_room.mob_list.draw(self.screen)
        self.current_room.arrows.draw(self.screen)
        self.current_room.item_list.draw(self.screen)
        
        self.current_room.door_list.draw(self.screen)
        self.current_room.door_list2.draw(self.screen)
        self.current_room.door_list3.draw(self.screen)
        self.current_room.lock_list.draw(self.screen)
        self.Zeb.bombs.draw(self.screen)
        self.current_room.bombs_items_list.draw(self.screen)
        if self.current_room == self.rooms[0][2] and len(self.current_room.mob_list) == 0:
            self.Zeb.items = self.current_room.key_list
            self.Zeb.keys.draw(self.screen)
        if self.Zeb.has_sword == False:
            self.current_room.item_list.draw(self.screen)
        else:
            for item in self.current_room.item_list:
                item.kill()
        self.current_room.door_list.draw(self.screen)
        pygame.display.flip()
        
    def change_room(self):
        if self.Zeb.enter_door:
            self.current_room = self.rooms[2][1]
            self.Zeb.in_dungeon = True
            self.Zeb.items = self.current_room.item_list
            if self.Zeb.in_dungeon:
                self.Zeb.walls = self.current_room.wall_list
                self.Zeb.doors = self.current_room.door_list
                self.Zeb.bomb_items = self.rooms[2][1].bombs_items_list
                if self.Zeb.rect.y> 600:
                    self.current_room = self.rooms[self.current_y][self.current_x]
                    self.Zeb.enter_door = False
                    self.Zeb.in_dungeon = False
                    self.Zeb.walls = self.rooms[self.current_y][self.current_x].wall_list
                    self.Zeb.doors = self.rooms[self.current_y][self.current_x].door_list
                    self.Zeb.items = self.rooms[self.current_y][self.current_x].item_list
                    for bomb in self.Zeb.bombs:
                        bomb.kill()
                    self.Zeb.rect.x = 300
                    self.Zeb.rect.y = 120
        if self.Zeb.enter_door2:
            self.current_room = self.rooms[2][2]
            self.Zeb.in_dungeon2 = True
            if self.Zeb.in_dungeon2:
                self.Zeb.walls = self.current_room.wall_list
                self.Zeb.mobs = self.current_room.mob_list
                self.Zeb.bomb_items = self.rooms[2][2].bombs_items_list
                if self.Zeb.rect.y > 600:
                    self.current_room = self.rooms[1][1]
                    self.Zeb.enter_door2 = False
                    self.Zeb.in_dungeon = False
                    self.Zeb.walls = self.rooms[self.current_y][self.current_x].wall_list
                    self.Zeb.doors = self.rooms[self.current_y][self.current_x].door_list
                    self.Zeb.items = self.rooms[self.current_y][self.current_x].item_list
                    self.Zeb.mobs = self.rooms[self.current_y][self.current_x].mob_list
                    self.Zeb.bomb_items = self.rooms[self.current_y][self.current_x].bombs_items_list
                    for bomb in self.Zeb.bombs:
                        bomb.kill()
                    self.Zeb.rect.x = 400
                    self.Zeb.rect.y = 180
        if self.Zeb.enter_door3:
            self.current_room = self.rooms[2][3]
            self.Zeb.in_dungeon3 = True
            if self.Zeb.in_dungeon3:
                self.Zeb.walls = self.current_room.wall_list
                self.Zeb.mobs = self.current_room.mob_list
                self.Zeb.bomb_items = self.rooms[2][2].bombs_items_list
                self.Zeb.doors = self.current_room.door_list
                
        elif self.Zeb.rect.x > 801:
            self.current_x = (self.current_x + 1)
            self.current_room = self.rooms[self.current_y][self.current_x]
            self.Zeb.walls = self.rooms[self.current_y][self.current_x].wall_list
            self.Zeb.mobs = self.rooms[self.current_y][self.current_x].mob_list
            self.Zeb.items = self.rooms[self.current_y][self.current_x].item_list
            self.Zeb.doors = self.rooms[self.current_y][self.current_x].door_list
            self.Zeb.doors2 = self.rooms[self.current_y][self.current_x].door_list2
            self.Zeb.doors3 = self.rooms[self.current_y][self.current_x].door_list3
            self.Zeb.keys = self.rooms[self.current_y][self.current_x].key_list
            self.Zeb.locks = self.rooms[self.current_y][self.current_x].lock_list
            for bomb in self.Zeb.bombs:
                        bomb.kill()
            self.Zeb.rect.x = 0
            if self.current_room == self.rooms[0][2]:
                if len(self.current_room.mob_list) == 0:
                    self.Zeb.items = self.current_room.item_list
                    self.Zeb.keys = self.current_room.key_list
                    self.Zeb.secret.play()
            if self.current_room == self.rooms[0][1]:
                for bomb in self.Zeb.bombs:
                        bomb.kill()
                self.Zeb.walls = self.current_room.wall_list

                    
                    
            
        elif self.Zeb.rect.x < 0:
            self.current_x = (self.current_x - 1)
            self.current_room = self.rooms[self.current_y][self.current_x]
            self.Zeb.walls = self.current_room.wall_list
            self.Zeb.mobs = self.current_room.mob_list
            self.Zeb.items = self.current_room.item_list
            self.Zeb.doors = self.current_room.door_list
            self.Zeb.doors2 = self.current_room.door_list2
            self.Zeb.doors3 = self.rooms[self.current_y][self.current_x].door_list3
            self.Zeb.keys = self.current_room.key_list
            self.Zeb.locks = self.current_room.lock_list
            for bomb in self.Zeb.bombs:
                        bomb.kill()
            self.Zeb.rect.x = 800
            
        elif self.Zeb.rect.y < 0:
            self.current_y = (self.current_y + 1)
            self.current_room = self.rooms[self.current_y][self.current_x]
            self.Zeb.walls = self.current_room.wall_list
            self.Zeb.mobs = self.current_room.mob_list
            self.Zeb.items = self.current_room.item_list
            self.Zeb.doors = self.current_room.door_list
            self.Zeb.doors2 = self.current_room.door_list2
            self.Zeb.doors3 = self.rooms[self.current_y][self.current_x].door_list3
            self.Zeb.keys = self.current_room.key_list
            self.Zeb.locks = self.current_room.lock_list
            for bomb in self.Zeb.bombs:
                        bomb.kill()
            self.Zeb.rect.y = 599
            
        elif self.Zeb.rect.y > 600:
            self.current_y = (self.current_y - 1)
            self.current_room = self.rooms[self.current_y][self.current_x]
            self.Zeb.walls = self.current_room.wall_list
            self.Zeb.mobs = self.current_room.mob_list
            self.Zeb.items = self.current_room.item_list
            self.Zeb.doors = self.current_room.door_list
            self.Zeb.doors2 = self.current_room.door_list2
            self.Zeb.doors3 = self.rooms[self.current_y][self.current_x].door_list3
            self.Zeb.keys = self.current_room.key_list
            self.Zeb.locks = self.current_room.lock_list
            for bomb in self.Zeb.bombs:
                        bomb.kill()
            self.Zeb.rect.y = 0
            
    def handle_events(self):
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN and self.Zeb.can_move == True:
                if event.key == K_ESCAPE:
                    self.done = True
                elif event.key == K_UP:
                    self.Zeb.upKeyPressed = True
                    self.Zeb.downKeyPressed = False
                    self.Zeb.DIRECTION = self.Zeb.UP
                elif event.key == K_DOWN:
                    self.Zeb.downKeyPressed = True
                    self.Zeb.upKeyPressed = False
                    self.Zeb.DIRECTION = self.Zeb.DOWN
                    self.Zeb.change_y = 5
                elif event.key == K_LEFT:
                    self.Zeb.leftKeyPressed = True
                    self.Zeb.rightKeyPressed = False
                    self.Zeb.DIRECTION = self.Zeb.LEFT
                elif event.key == K_RIGHT:
                    self.Zeb.rightKeyPressed = True
                    self.Zeb.leftKeyPressed = False
                    self.Zeb.DIRECTION = self.Zeb.RIGHT
                elif event.key == K_b and self.Zeb.has_bombs:
                    self.Zeb.bombs.add(Bomb(self.Zeb.rect.x, self.Zeb.rect.y,self.Zeb))

                elif event.key == K_r:
                    obj = GameMain()
                    obj.main_loop()

                     
                elif event.key == K_SPACE and self.Zeb.has_sword == True:
                    self.Zeb.spacePressed = True
                    self.Zeb.can_move = False
                    if self.Zeb.DIRECTION == self.Zeb.RIGHT:
                        self.Zeb.image = self.Zeb.attack_right
                        oldRect = self.Zeb.rect
                        self.Zeb.rect = self.Zeb.image.get_rect()
                        self.Zeb.rect.x = oldRect.x + 15
                        self.Zeb.rect.y = oldRect.y
                        self.Zeb.rightKeyPressed = False
                        self.Zeb.leftKeyPressed = False
                        self.Zeb.upKeyPressed = False
                        self.Zeb.downKeyPressed = False
                    elif self.Zeb.DIRECTION == self.Zeb.LEFT:
                        self.Zeb.image = self.Zeb.attack_left
                        self.Zeb.leftKeyPressed = False
                        self.Zeb.rightKeyPressed = False
                        self.Zeb.upKeyPressed = False
                        self.Zeb.downKeyPressed = False
                        self.Zeb.rect.x -= 30
                    elif self.Zeb.DIRECTION == self.Zeb.UP:
                        self.Zeb.image = self.Zeb.attack_up
                        self.Zeb.rightKeyPressed = False
                        self.Zeb.leftKeyPressed = False
                        self.Zeb.downKeyPressed = False
                        self.Zeb.upKeyPressed = False
                        self.Zeb.rect.y -= 30
                    elif self.Zeb.DIRECTION == self.Zeb.DOWN:
                        self.Zeb.image = self.Zeb.attack_down
                        oldRect = self.Zeb.rect
                        self.Zeb.rect = self.Zeb.image.get_rect()
                        self.Zeb.rect.x = oldRect.x
                        self.Zeb.rect.y = oldRect.y + 15
                        self.Zeb.downKeyPressed = False
                        self.Zeb.upKeyPressed = False
                        self.Zeb.leftKeyPressed = False
                        self.Zeb.rightKeyPressed = False
                    self.Zeb.effect.play()
                    self.Zeb.action = 'attacking'

                        
            elif event.type == KEYUP:
                if event.key == K_UP:
                    
                    self.Zeb.upKeyPressed = False
                    if self.Zeb.rightKeyPressed:
                        self.Zeb.DIRECTION = self.Zeb.RIGHT
                    elif self.Zeb.leftKeyPressed:
                        self.Zeb.DIRECTION = self.Zeb.LEFT
                elif event.key == K_DOWN:
                    
                    self.Zeb.downKeyPressed = False
                    if self.Zeb.rightKeyPressed:
                        self.Zeb.DIRECTION = self.Zeb.RIGHT
                    elif self.Zeb.leftKeyPressed:
                        self.Zeb.DIRECTION = self.Zeb.LEFT
                elif event.key == K_LEFT:
                    
                    self.Zeb.leftKeyPressed = False
                    if self.Zeb.upKeyPressed:
                        self.Zeb.DIRECTION = self.Zeb.UP
                    elif self.Zeb.downKeyPressed:
                        self.Zeb.DIRECTION = self.Zeb.DOWN
                elif event.key == K_RIGHT:
                    
                    self.Zeb.rightKeyPressed = False
                    if self.Zeb.upKeyPressed:
                        self.Zeb.DIRECTION = self.Zeb.UP
                    elif self.Zeb.downKeyPressed:
                        self.Zeb.DIRECTION = self.Zeb.DOWN

                elif event.key == K_SPACE and self.Zeb.has_sword == True:
                    self.Zeb.can_move = True
                    self.Zeb.spacePressed = False
                    if self.Zeb.DIRECTION == self.Zeb.RIGHT:
                        self.Zeb.image = self.Zeb.right1
                        oldRect = self.Zeb.rect
                        self.Zeb.rect = self.Zeb.image.get_rect()
                        self.Zeb.rect.x = oldRect.x - 15
                        self.Zeb.rect.y = oldRect.y
                        self.Zeb.downKeyPressed = False
                        self.Zeb.upKeyPressed = False
                        self.Zeb.leftKeyPressed = False
                        self.Zeb.rightKeyPressed = False
                    if self.Zeb.DIRECTION == self.Zeb.LEFT:
                        self.Zeb.image = self.Zeb.left1
                        self.Zeb.downKeyPressed = False
                        self.Zeb.upKeyPressed = False
                        self.Zeb.leftKeyPressed = False
                        self.Zeb.rightKeyPressed = False
                        self.Zeb.rect.x += 30
                    if self.Zeb.DIRECTION == self.Zeb.UP:
                        self.Zeb.image = self.Zeb.up1
                        self.Zeb.downKeyPressed = False
                        self.Zeb.upKeyPressed = False
                        self.Zeb.leftKeyPressed = False
                        self.Zeb.rightKeyPressed = False
                        self.Zeb.rect.y += 30
                    if self.Zeb.DIRECTION == self.Zeb.DOWN:
                        self.Zeb.image = self.Zeb.down1
                        oldRect = self.Zeb.rect
                        self.Zeb.rect = self.Zeb.image.get_rect()
                        self.Zeb.rect.x = oldRect.x 
                        self.Zeb.rect.y = oldRect.y -15
                        self.Zeb.downKeyPressed = False
                        self.Zeb.upKeyPressed = False
                        self.Zeb.leftKeyPressed = False
                        self.Zeb.rightKeyPressed = False
                    self.Zeb.action = "walking"
        
                    
                        
if __name__ == "__main__":
    game = GameMain()
    game.main_loop()
