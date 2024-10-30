import  random
import time

import pygame

class Bomb:
    def __init__(self, screen, img_sheet, animation_step, width=50, height=50, color=(255, 0, 0)):
        """
        Khởi tạo đối tượng Bomb
        :param screen: Màn hình game (pygame.Surface) nơi vẽ hình vuông
        :param width: Chiều rộng của hình vuông
        :param height: Chiều cao của hình vuông
        :param color: Màu của hình vuông (RGB)
        """
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color
        self.img_sheet= img_sheet
        self.step = animation_step
        self.frame_index = 0
        self.action = 0
        self.explode = False
        self.falling = True
        self.fire_size = 50
        self.explode_size = 200

        self.img_animation = self.load_img(self.img_sheet, self.step)
        self.image = self.img_animation[self.action][self.frame_index]

        # Đặt vị trí ban đầu ngẫu nhiên cho Bomb
        self.x = random.randint(0, screen.get_width() - self.width)
        self.y = -self.height  # Bắt đầu từ trên màn hình để di chuyển xuống

        # Tốc độ di chuyển của hình vuông
        self.speed = 5

    def load_img(self, img_sheet , step):
        animation_list = []
        for y, animation in enumerate(step):
            temp_img_list = []
            for x in range(animation):
                temp_img = img_sheet.subsurface(x * 360, y * 360, 360, 360)
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)
        return animation_list
    def update_bom(self):
        if self.falling:
            self.action = 0
        if self.explode:
            self.action = 1

        self.frame_index = (self.frame_index +1) % len(self.img_animation[self.action])




    def move_down(self):
        """Di chuyển hình vuông xuống dưới theo trục y."""
        if self.falling:
            self.y += self.speed

        if self.y > self.screen.get_height() - 95 - 60:
            self.explode = True
            self.falling = False

    def drawbomb(self):
        x_img = 0
        y_img = 0
        if self.falling:
            size = self.fire_size
            x_img = self.x
            y_img = self.y
        if self.explode:
            size = self.explode_size
            self.frame_index = -1
            x_img = self.x + self.width // 2 - size // 2  # Tính toán vị trí x từ tâm
            y_img = self.y + self.height // 2 - size // 2  # Tính toán vị trí y từ tâm
            self.frame_index = (self.frame_index + 1) % len(self.img_animation[self.action])
            print(self.frame_index)
        resize_img = pygame.transform.scale(self.img_animation[self.action][self.frame_index], (size, size))
        self.screen.blit(resize_img, (x_img, y_img))

    def is_off_screen(self):
        """Kiểm tra xem hình vuông có di chuyển ra khỏi màn hình hay không."""
        return self.y > self.screen.get_height() - 95 - 60

    def draw_explosion(self):
        """Vẽ vụ nổ (hình vuông lớn gấp đôi kích thước Bomb)."""
        explosion_size = self.width * 3  # Kích thước vụ nổ gấp đôi kích thước Bomb
        explosion_x = self.x + self.width // 2 - explosion_size // 2  # Tính toán vị trí x từ tâm
        explosion_y = self.y + self.height // 2 - explosion_size // 2  # Tính toán vị trí y từ tâm
        #pygame.draw.rect(self.screen, (255, 255, 0),(explosion_x, explosion_y, explosion_size, explosion_size))  # Vẽ hình vuông vụ nổ
        return pygame.Rect(explosion_x, explosion_y, explosion_size, explosion_size)




