from sprite_object import *

class ObjectHandler:
    def __init__(self,game):
        self.game=game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprites_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(15,10.1)))
        add_sprite(AnimatedSprite(game, pos=(18,10.1)))
        add_sprite(AnimatedSprite(game, pos=(21,10.1)))
        add_sprite(AnimatedSprite(game, pos=(24,10.1)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprites_path + 'HangingCorpse1.png', pos=(1.5,2.6), animation_time=480))
        add_sprite(AnimatedSprite(game, path=self.animated_sprites_path + 'HangingCorpse1.png', pos=(1.5,1.5), animation_time=480))
        add_sprite(AnimatedSprite(game, path=self.animated_sprites_path + 'HangingCorpse1.png', pos=(8,3), animation_time=480))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self,sprite):
        self.sprite_list.append(sprite)