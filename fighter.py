import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

spear_img = pygame.image.load(
    "assets/images/Huntress/Sprites/Spear.png"
).convert_alpha()


class Fighter:
    def __init__(self, player, x, y, flip, Character):
        self.id = player
        self.player = player
        self.special_move_ready = False
        self.special_move_timer = pygame.time.get_ticks()
        if player == 1:

            self.DATA = [
                Character.SIZEX,
                Character.SIZEY,
                Character.scaleX,
                Character.scaleY,
                Character.OFFSET1,
                Character.information,
            ]
        else:
            self.DATA = [
                Character.SIZEX,
                Character.SIZEY,
                Character.scaleX,
                Character.scaleY,
                Character.OFFSET2,
                Character.information,
            ]

        self.sizeX = self.DATA[0]
        self.sizeY = self.DATA[1]
        self.image_scaleX = self.DATA[2]
        self.image_scaleY = self.DATA[3]
        self.offset = self.DATA[4]
        self.flip = flip
        self.animation_list = self.load_images(
            Character.sheet, Character.animation_steps
        )
        self.action = (
            0  # 0:idle, 1:run, 2:jump, 3:attack1, 4:attack2, 5:attack3, 6:hit, 7:death
        )
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attack_sound = Character.sound
        self.hit = False
        self.health = 100

        self.mana = 100
        self.information = self.DATA[5]
        self.alive = True
        self.characterName = Character.name
        self.direction = 1
        self.shoot_delay = 400  # Delay before shooting (in milliseconds)
        self.shoot_ready = (
            False  # Ensure the attack cooldown only allows 1 spear at a time
        )
        self.shoot_start_time = 0  # Track when the shooting starts
        self.performing_action = False

    def gain_mana(self, amount):
        self.mana += amount
        if self.mana > 100:
            self.mana = 100


    def ability_e(self, hit_successful):
        if hit_successful:
            self.gain_mana(10)

    def ability_r(self, hit_successful):
        if hit_successful:
            self.gain_mana(5)

    def ability_u(self, hit_successful):
        if hit_successful:
            self.gain_mana(10)

    def ability_i(self, hit_successful):
        if hit_successful:
            self.gain_mana(5)

    def increase_mana(self, amount):
        self.mana = min(100, self.mana + amount)  # Giới hạn mana tối đa là 100

    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(
                    x * self.sizeX, y * self.sizeY, self.sizeX, self.sizeY
                )
                temp_img_list.append(
                    pygame.transform.scale(
                        temp_img,
                        (
                            self.sizeX * self.image_scaleX,
                            self.sizeY * self.image_scaleY,
                        ),
                    )
                )
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, target, round_over):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0

        key = pygame.key.get_pressed()

        if not self.attacking and self.alive and not round_over:
            if self.player == 1:
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_w] and not self.jump:
                    self.vel_y = -30
                    self.jump = True

                if (
                    self.hit == False
                    and key[pygame.K_e]
                    or key[pygame.K_r]
                    or key[pygame.K_t]
                    and self.attack_cooldown == 0
                ):
                    if key[pygame.K_e]:
                        self.attack_type = 1
                        self.attack(target, self.attack_type)
                    if key[pygame.K_r]:
                        self.attack_type = 2

                        self.attack(target, self.attack_type)
                    if key[pygame.K_t] and (self.mana >= 20):
                        self.attack_type = 3
                        if self.characterName == "Huntress":
                            if not self.shoot_ready:
                                self.shoot_ready = True
                                self.shoot_start_time = (
                                    pygame.time.get_ticks()
                                )  # Set start time for spear delay
                                self.attacking = True  # Start attack animation
                        else:
                            self.attack(target, self.attack_type)
                        self.mana -= 20
                        if self.mana < 0:
                            self.mana = 0

            if self.player == 2:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_UP] and not self.jump:
                    self.vel_y = -30
                    self.jump = True

                if (
                    self.hit == False
                    and key[pygame.K_u]
                    or key[pygame.K_i]
                    or key[pygame.K_o]
                    and self.attack_cooldown == 0
                ):

                    if key[pygame.K_u]:
                        self.attack_type = 1
                        self.attack(target, self.attack_type)
                    if key[pygame.K_i]:
                        self.attack_type = 2

                        self.attack(target, self.attack_type)
                    if key[pygame.K_o] and (self.mana >= 20):
                        self.attack_type = 3
                        if self.characterName == "Huntress":
                            if not self.shoot_ready:
                                self.shoot_ready = True
                                self.shoot_start_time = (
                                    pygame.time.get_ticks()
                                )  # Set start time for spear delay
                                self.attacking = True  # Start attack animation
                        else:
                            self.attack(target, self.attack_type)
                        self.mana -= 20
                        if self.mana < 0:
                            self.mana = 0

        self.vel_y += GRAVITY
        dy += self.vel_y

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 95:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 95 - self.rect.bottom

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
            self.direction = 1
        else:
            self.flip = True
            self.direction = -1

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 2

        self.rect.x += dx
        self.rect.y += dy

        if self.shoot_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_start_time >= self.shoot_delay:  # Check delay
                self.fire_spear(target)
                self.shoot_ready = False  # Reset after shooting
                self.attacking = False
                self.attack_cooldown = 50

    def fire_spear(self, target):
        if self.mana >= 20:
            spear = Spear(
                target,
                self.rect.centerx + (0.1 * self.rect.size[0] * self.direction),
                self.rect.centery - 40,
                self.direction,
                self.flip,
            )
            spear_group.add(spear)
            self.mana -= 20

    def attack(self, target, type):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_sound.play()
            attacking_rect = pygame.Rect(
                self.rect.centerx - (2 * self.rect.width * self.flip),
                self.rect.y,
                2 * self.rect.width,
                self.rect.height,
            )
            if attacking_rect.colliderect(target.rect):
                target.health -= self.information[type]
                target.hit = True

    def check_hit(self, explosion_rect):
        """Kiểm tra va chạm với vụ nổ."""
        if self.rect.colliderect(explosion_rect):
            self.health -= 10  # Giảm sức khỏe khi bị trúng
            self.hit = True  # Đánh dấu là bị trúng
        return self.hit

    def update(self):
        current_time = pygame.time.get_ticks()

        # Kiểm tra nếu đã 3 giây (3000 ms), thì cho phép dùng chiêu
        if not self.special_move_ready and (
            current_time - self.special_move_timer >= 3000
        ):
            self.special_move_ready = True
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(7)  # 7:death
        elif self.hit:
            self.update_action(6)  # 6:hit
        elif self.attacking:
            if self.attack_type == 1:
                self.update_action(3)  # 3:attack1
            elif self.attack_type == 2:
                self.update_action(4)  # 4:attack2
            elif self.attack_type == 3:
                self.update_action(5)  # 5:attack3
        elif self.jump:
            self.update_action(2)  # 2:jump
        elif self.running:
            self.update_action(1)  # 1:run
        else:
            self.update_action(0)  # 0:idle

        animation_cooldown = 50
        self.image = self.animation_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

        if self.frame_index >= len(self.animation_list[self.action]):
            if not self.alive:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                if self.action in [3, 4, 5]:
                    self.attacking = False
                    self.attack_cooldown = 50
                if self.action == 6:
                    self.hit = False
                    self.attacking = False
                    self.attack_cooldown = 50

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):

        # debug
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)

        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(
            img,
            (
                self.rect.x - (self.offset[0] * self.image_scaleX),
                self.rect.y - (self.offset[1] * self.image_scaleY),
            ),
        )


class Spear(pygame.sprite.Sprite):
    def __init__(self, target, x, y, direction, flip):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15

        # Define the dimensions for the rect
        self.rect = pygame.Rect((x, y, 150, 80))
        self.rect.center = (x, y)

        # Scale the image to match the size of the rect
        self.image = pygame.transform.scale(
            spear_img, (self.rect.width * 1.5, self.rect.height)
        )

        # Flip the image
        self.image = pygame.transform.flip(self.image, flip, False)

        self.rect.width = 100
        self.rect.height = 80
        self.target = target
        self.direction = direction

    def update(self):
        # debug
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)

        # move bullet
        self.rect.x += self.direction * self.speed

        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        # check collision with characters
        if pygame.sprite.spritecollide(self.target, spear_group, False):
            if self.target.alive:
                self.target.health -= 5
                self.target.hit = True
                self.kill()


spear_group = pygame.sprite.Group()
