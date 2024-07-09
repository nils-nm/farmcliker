# Проэкт для itch.io
# ===загрузка модулей===
import pygame as pg
from random import randint


# ===класс игры===
class Game():
    def __init__(self):
        self.caption = 'farmcliker'
        self.fps = 60
        self.camera_width = 1024
        self.camera_height = 512
        self.score = 0

    def game_initialize(self):
        pg.init()
        # ===музыка===
        pg.mixer.music.load('ref/music/music.mp3')
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
        # ==
        self.kill = pg.mixer.Sound('ref/sound/metronome01.ogg')
        self.upgrade = pg.mixer.Sound('ref/sound/metronome02.ogg')
        # ============
        camera = pg.display.set_mode((self.camera_width, self.camera_height))
        pg.display.set_caption(self.caption)
        self.font = pg.font.Font(None, 20)

        # ===флажки===
        self.enime_die = False
        # ==
        self.car_gro_press = False
        self.car_press = False
        self.car_auto_press = False
        # ==
        self.pot_gro_press = False
        self.pot_press = False
        self.pot_auto_press = False
        self.pot_lock = True
        # ==
        self.tur_gro_press = False
        self.tur_press = False
        self.tur_auto_press = False
        self.tur_lock = True
        # ==
        self.prise_lock = True
        self.pr_press = False
        # ============


        # ===изображения===
        self.background = pg.image.load('ref/images/timebackground.png').convert()
        tileset = pg.image.load('ref/images/tileset.png').convert_alpha()
        self.sprite = pg.image.load('ref/images/enimes.png')
        # =====
        self.enime_stay = self.sprite.subsurface((0, 0, 16, 16))
        self.enime_stay = pg.transform.scale(self.enime_stay,
                                             (self.enime_stay.get_width()*2,
                                              self.enime_stay.get_height()*2))
        self.enime = [self.sprite.subsurface((0, 0, 16, 16)),
                      self.sprite.subsurface((16, 0, 16, 16)),
                      self.sprite.subsurface((32, 0, 16, 16)),
                      self.sprite.subsurface((48, 0, 16, 16))]
        self.boom = [self.sprite.subsurface((0, 16, 16, 16)),
                     self.sprite.subsurface((16, 16, 16, 16)),
                     self.sprite.subsurface((32, 16, 16, 16)),
                     self.sprite.subsurface((48, 16, 16, 16))]
        # =====
        self.carrot_growth_up = tileset.subsurface((0, 0, 128, 64))
        self.carrot_growth_up_press = tileset.subsurface((0, 64, 128, 64))
        self.carrot_growth_up_ready = tileset.subsurface((0, 128, 128, 64))
        # ==
        self.carrot_auto_tile = tileset.subsurface((0, 320, 128, 64))
        self.carrot_auto_press = tileset.subsurface((0, 384, 128, 64))
        self.carrot_auto_ready = tileset.subsurface((0, 448, 128, 64))
        # ==
        self.carrot = tileset.subsurface((0, 192, 128, 64))
        self.carrot_press = tileset.subsurface((0, 256, 128, 64))
        # =====
        self.potato_growth_up = tileset.subsurface((128, 0, 128, 64))
        self.potato_growth_up_press = tileset.subsurface((128, 64, 128, 64))
        self.potato_growth_up_ready = tileset.subsurface((128, 128, 128, 64))
        # ==
        self.potato_auto_tile = tileset.subsurface((128, 320, 128, 64))
        self.potato_auto_press = tileset.subsurface((128, 384, 128, 64))
        self.potato_auto_ready = tileset.subsurface((128, 448, 128, 64))
        # ==
        self.potato = tileset.subsurface((128, 192, 128, 64))
        self.potato_press = tileset.subsurface((128, 256, 128, 64))
        self.potato_lock = tileset.subsurface((384, 0, 128, 64))
        # =====
        self.turnip_growth_up = tileset.subsurface((256, 0, 128, 64))
        self.turnip_growth_up_press = tileset.subsurface((256, 64, 128, 64))
        self.turnip_growth_up_ready = tileset.subsurface((256, 128, 128, 64))
        # ==
        self.turnip_auto_tile = tileset.subsurface((256, 320, 128, 64))
        self.turnip_auto_press = tileset.subsurface((256, 384, 128, 64))
        self.turnip_auto_ready = tileset.subsurface((256, 448, 128, 64))
        # ==
        self.turnip = tileset.subsurface((256, 192, 128, 64))
        self.turnip_press = tileset.subsurface((256, 256, 128, 64))
        self.turnip_lock = tileset.subsurface((384, 64, 128, 64))
        # ==
        self.prise_lc = tileset.subsurface((384, 128, 128, 64))
        self.prise_ready = tileset.subsurface((384, 448, 128, 64))
        self.prise_press = tileset.subsurface((384, 384, 128, 64))

        # =================

        # ===плата за уровни===
        self.car_growth = 1
        self.car_growth_max = 10
        self.carrot_growth_step = 0
        self.carrot_growth = [1, 5, 10, 20, 35, 55, 80, 110, 145, 185, 'MAX']
        # ==
        self.car_auto_score = 0
        self.carrot_auto_step = 0
        self.carrot_auto = [2, 10, 20, 40, 70, 110, 160, 220, 290, 370, 'MAX']
        # =====
        self.pot_growth = 5
        self.pot_growth_max = 10
        self.potato_growth_step = 0
        self.potato_growth = [20, 50, 100, 200, 350, 550, 800, 1100, 1450, 1850, 'MAX']
        # ==
        self.pot_auto_score = 0
        self.potato_auto_step = 0
        self.potato_auto = [40, 100, 200, 400, 700, 1100, 1600, 2200, 2900, 3700, 'MAX']
        # =====
        self.tur_growth = 10
        self.tur_growth_max = 10
        self.turnip_growth_step = 0
        self.turnip_growth =  [60, 150, 300, 600, 1050, 1650, 2400, 3300, 4350, 5550, 'MAX']
        # ==
        self.tur_auto_score = 0
        self.turnip_auto_step = 0
        self.turnip_auto = [120, 300, 600, 1200, 2100, 3300, 4800, 7200, 9300, 11700, 'MAX']

        # =====================
        self.kills = 0
        self.count_enimes = 6
        self.enime_ = 0
        self.price_enime = 1
        self.enime_step = 0
        self.list_of_enimes = []
        self.timer = 0
        clock = pg.time.Clock()
        self.create_enime(self.count_enimes)
        self.game_run(camera, clock)

    def create_enime(self, num):
        for i in range(num):
            x, y = randint(520, 1000), 16
            vel = randint(1, 3)
            self.list_of_enimes.append([x, y, vel])


    def draw_me(self, camera, enime_num=0):
        camera.blit(self.background, [0, 0])
        # ===убитые враги===
        camera.blit(self.enime_stay, [540, 430])
        camera.blit(self.font.render(f'{self.kills}', True, (210, 210, 210)), [590, 440])
        # ==================
        # ===prise===
        if self.prise_lock is False:
            if self.pr_press is True:
                camera.blit(self.prise_press, [740, 430])
            else:
                camera.blit(self.prise_ready, [740, 430])
        else:
            camera.blit(self.prise_lc, [740, 430])
        # ===враг===
        for i in self.list_of_enimes:
            if self.timer % 20 == 0:
                self.enime_step += 1
                i[1] += i[2]
            if self.enime_step >= 4:
                self.enime_step = 0
            camera.blit(self.enime[self.enime_step], (i[0], i[1]))


        # ===морковь - грядка===
        if self.car_press is False:
            camera.blit(self.carrot, [96, 67])
        else:
            camera.blit(self.carrot_press, [96, 67])
        # ===картоха - грядка===
        if self.pot_lock is False:
            if self.pot_press is False:
                camera.blit(self.potato, [272, 67])
            else:
                camera.blit(self.potato_press, [272, 67])
        else:
            camera.blit(self.potato_lock, [272, 67])
        # ===репа - грядка===
        if self.tur_lock is False:
            if self.tur_press is False:
                camera.blit(self.turnip, [184, 163])
            else:
                camera.blit(self.turnip_press, [184, 163])
        else:
            camera.blit(self.turnip_lock, [184, 163])
        # ======================

        camera.blit(self.font.render(f'score: {self.score}', True, (255, 0, 0)), [200, 20])

        # ===улучшение моркови===
        # ==growth==
        if self.car_gro_press is False:
            if self.carrot_growth[self.carrot_growth_step] != 'MAX' and self.score >= self.carrot_growth[self.carrot_growth_step]:
                camera.blit(self.carrot_growth_up_ready, [16, 420])
            else:
                camera.blit(self.carrot_growth_up, [16, 420])
        else:
            camera.blit(self.carrot_growth_up_press, [16, 420])

        camera.blit(self.font.render(
            f'price:{self.carrot_growth[self.carrot_growth_step]}',
            True, (255, 0, 0)), [54, 462])

        # ==auto==
        if self.car_auto_press is False:
            if self.carrot_auto[self.carrot_auto_step] != 'MAX' and self.score >= self.carrot_auto[self.carrot_auto_step]:
                camera.blit(self.carrot_auto_ready, [16, 340])
            else:
                camera.blit(self.carrot_auto_tile, [16, 340])
        else:
            camera.blit(self.carrot_auto_press, [16, 340])

        camera.blit(self.font.render(
            f'price:{self.carrot_auto[self.carrot_auto_step]}',
            True, (255, 0, 0)), [54, 382])

        # ===улучшение картохи===
        # ==growth==
        if self.pot_lock is False:
            if self.pot_gro_press is False:
                if self.potato_growth[self.potato_growth_step] != 'MAX' and self.score >= self.potato_growth[self.potato_growth_step]:
                    camera.blit(self.potato_growth_up_ready, [160, 420])
                else:
                    camera.blit(self.potato_growth_up, [160, 420])
            else:
                camera.blit(self.potato_growth_up_press, [160, 420])

            camera.blit(self.font.render(
                f'price:{self.potato_growth[self.potato_growth_step]}',
                True, (255, 0, 0)), [198, 462])

        # ==auto==
            if self.pot_auto_press is False:
                if self.potato_auto[self.potato_auto_step] != 'MAX' and self.score >= self.potato_auto[self.potato_auto_step]:
                    camera.blit(self.potato_auto_ready, [160, 340])
                else:
                    camera.blit(self.potato_auto_tile, [160, 340])
            else:
                camera.blit(self.potato_auto_press, [160, 340])

            camera.blit(self.font.render(
                f'price:{self.potato_auto[self.potato_auto_step]}',
                True, (255, 0, 0)), [198, 382])

        # ===улучшение репы===
        # ==growth==
        if self.tur_lock is False:
            if self.tur_gro_press is False:
                if self.turnip_growth[self.turnip_growth_step] != 'MAX' and self.score >= self.turnip_growth[self.turnip_growth_step]:
                    camera.blit(self.turnip_growth_up_ready, [304, 420])
                else:
                    camera.blit(self.turnip_growth_up, [304, 420])
            else:
                camera.blit(self.turnip_growth_up_press, [304, 420])

            camera.blit(self.font.render(
                f'price:{self.turnip_growth[self.turnip_growth_step]}',
                True, (255, 0, 0)), [342, 462])

        # ==auto==
            if self.tur_auto_press is False:
                if self.turnip_auto[self.turnip_auto_step] != 'MAX' and self.score >= self.turnip_auto[self.turnip_auto_step]:
                    camera.blit(self.turnip_auto_ready, [304, 340])
                else:
                    camera.blit(self.turnip_auto_tile, [304, 340])
            else:
                camera.blit(self.turnip_auto_press, [304, 340])

            camera.blit(self.font.render(
                f'price:{self.turnip_auto[self.turnip_auto_step]}',
                True, (255, 0, 0)), [342, 382])

    def kill_enime(self, camera, i):
        for j in self.boom:
            camera.blit(j, [i[0], i[1]])
        self.list_of_enimes.remove(i)
        x, y = randint(520, 1000), 16
        vel = randint(1, 3)
        self.list_of_enimes.append([x, y, vel])
        self.enime_die = False


    def game_run(self, camera, clock):
        while True:
            pos = pg.mouse.get_pos()
            self.timer += 1
            for i in self.list_of_enimes:
                if i[1] >= 331-16:
                    self.score = 0
                    self.list_of_enimes.remove(i)
                    x, y = randint(520, 1000), 16
                    vel = randint(1, 4)
                    self.list_of_enimes.append([x, y, vel])

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        quit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # ===грядки===
                        if 96 <= pos[0] <= 96+128 and 67 <= pos[1] <= 67+64:
                            self.score += self.car_growth
                            self.car_press = True
                        # ==
                        if self.pot_lock is False:
                            if 272 <= pos[0] <= 272+128 and 67 <= pos[1] <= 67+64:
                                self.score += self.pot_growth
                                self.pot_press = True
                        # ==
                        if self.tur_lock is False:
                            if 184 <= pos[0] <= 184+128 and 163 <= pos[1] <= 163+64:
                                self.score += self.tur_growth
                                self.tur_press = True
                        # ==
                        if self.prise_lock is False:
                            if 740 <= pos[0] <= 740+128 and 430 <= pos[1] <= 430+64:
                                self.pr_press = True
                                self.create_enime(20)

                        # ============
                        # ===детекция врагов===
                        for i in self.list_of_enimes:
                            if i[0] <= pos[0] <= i[0]+16 and i[1] <= pos[1] <= i[1]+16:
                                if self.score >= self.price_enime:
                                    self.score -= self.price_enime
                                    self.kills += 1
                                    self.kill.play()
                                    self.price_enime += 1
                                    self.enime_die = True
                                    self.enime_ = i

                        # =====================
                        # ===улучшения===
                        if 16 <= pos[0] <= 16+128 and 420 <= pos[1] <= 420+64:
                            if self.carrot_growth[self.carrot_growth_step] != 'MAX':
                                self.car_gro_press = True

                                if self.score >= self.carrot_growth[self.carrot_growth_step]:
                                    self.score -= self.carrot_growth[self.carrot_growth_step]
                                    self.carrot_growth_step += 1
                                    self.car_growth += 1
                                    self.upgrade.play()

                        if 16 <= pos[0] <= 16+128 and 340 <= pos[1] <= 340+64:
                            if self.carrot_auto[self.carrot_auto_step] != 'MAX':
                                self.car_auto_press = True

                                if self.score >= self.carrot_auto[self.carrot_auto_step]:
                                    self.score -= self.carrot_auto[self.carrot_auto_step]
                                    self.carrot_auto_step += 1
                                    self.car_auto_score += 1
                                    self.upgrade.play()
                        # ==
                        if self.pot_lock is False:
                            if 160 <= pos[0] <= 160+128 and 420 <= pos[1] <= 420+64:
                                if self.potato_growth[self.potato_growth_step] != 'MAX':
                                    self.pot_gro_press = True

                                    if self.score >= self.potato_growth[self.potato_growth_step]:
                                        self.score -= self.potato_growth[self.potato_growth_step]
                                        self.potato_growth_step += 1
                                        self.pot_growth += 2
                                        self.upgrade.play()

                            if 160 <= pos[0] <= 160+128 and 340 <= pos[1] <= 340+64:
                                if self.potato_auto[self.potato_auto_step] != 'MAX':
                                    self.pot_auto_press = True

                                    if self.score >= self.potato_auto[self.potato_auto_step]:
                                        self.score -= self.potato_auto[self.potato_auto_step]
                                        self.potato_auto_step += 1
                                        self.pot_auto_score += 2
                                        self.upgrade.play()
                        # ==
                        if self.tur_lock is False:
                            if 304 <= pos[0] <= 304+128 and 420 <= pos[1] <= 420+64:
                                if self.turnip_growth[self.turnip_growth_step] != 'MAX':
                                    self.tur_gro_press = True

                                    if self.score >= self.turnip_growth[self.turnip_growth_step]:
                                        self.score -= self.turnip_growth[self.turnip_growth_step]
                                        self.turnip_growth_step += 1
                                        self.tur_growth += 5
                                        self.upgrade.play()

                            if 304 <= pos[0] <= 304+128 and 340 <= pos[1] <= 340+64:
                                if self.turnip_auto[self.potato_auto_step] != 'MAX':
                                    self.tur_auto_press = True

                                    if self.score >= self.turnip_auto[self.turnip_auto_step]:
                                        self.score -= self.turnip_auto[self.turnip_auto_step]
                                        self.turnip_auto_step += 1
                                        self.tur_auto_score += 2
                                        self.upgrade.play()

                        # ===============
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.car_gro_press = False
                        self.car_press = False
                        self.car_auto_press = False
                        self.pot_gro_press = False
                        self.pot_press = False
                        self.pot_auto_press = False
                        self.tur_gro_press = False
                        self.tur_press = False
                        self.tur_auto_press = False
                        self.pr_press = False

            if self.kills >= 50:
                self.pot_lock = False
            if self.kills >= 100:
                self.tur_lock = False
            if self.kills >= 200:
                self.prise_lock = False

            if self.timer >= 60:
                self.score += self.car_auto_score
                self.score += self.pot_auto_score
                self.timer = 0


            self.draw_me(camera)
            if self.enime_die is True:
                self.kill_enime(camera, self.enime_)


            pg.display.flip()
            clock.tick(self.fps)

if __name__ == '__main__':
    new_game = Game()
    new_game.game_initialize()
