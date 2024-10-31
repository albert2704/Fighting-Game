import random
import sys
import time

import pygame
from pygame import mixer
from button import Button
from character import characters
from fighter import Fighter
from fighter import spear_group
from bomb import Bomb

mixer.init()
pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's Fight!")

# set framerate
clock = pygame.time.Clock()

FPS = 40

current_bomb = None
f1_isHit = f2_isHit = False
explosion_rect = None
last_spawn_time = 0
spawn_interval = random.uniform(1, 3)

# define colours
RED = (255, 50, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

BLUE = (0, 0, 255)  # Màu xanh dương
LIGHTBLUE = (173, 216, 230)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
# define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

# load music and sounds
pygame.mixer.music.load(
    "C:/Users/Admin/OneDrive/Desktop/Python-PTIT/Fighting-Game-Python/assets/audio/music.mp3"
)
# <<<<<<< HEAD
# # pygame.mixer.music.load("../assets/audio/music.mp3")
# pygame.mixer.music.set_volume(0)
# =======
pygame.mixer.music.set_volume(0.3)
# >>>>>>> origin/huy_dev
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound(
    "C:/Users/Admin/OneDrive/Desktop/Python-PTIT/Fighting-Game-Python/assets/audio/sword.wav"
)
sword_fx.set_volume(0.2)

bg_image = pygame.image.load(
    "C:/Users/Admin/OneDrive/Desktop/Python-PTIT/Fighting-Game-Python/assets/images/background/background3.png"
).convert_alpha()
bg_home = pygame.image.load(
    "C:/Users/Admin/OneDrive/Desktop/Python-PTIT/Fighting-Game-Python/assets/images/background/background4.jpg"
).convert_alpha()

# load vicory image
victory_img = pygame.image.load(
    "C:/Users/Admin/OneDrive/Desktop/Python-PTIT/Fighting-Game-Python/assets/images/icons/victory.png"
).convert_alpha()

# define font
count_font = pygame.font.Font(
    "C:/Users/Admin/OneDrive/Desktop/Python-PTIT/Fighting-Game-Python/assets/fonts/turok.ttf",
    80,
)
score_font = pygame.font.Font(
    "C:/Users/Admin/OneDrive/Desktop/Python-PTIT/Fighting-Game-Python/assets/fonts/turok.ttf",
    30,
)
score_font_winner = pygame.font.Font(
    "C:/Users/Admin/OneDrive/Desktop/Python-PTIT/Fighting-Game-Python/assets/fonts/turok.ttf",
    70,
)


# function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


def draw_home():
    scaled_bg = pygame.transform.scale(bg_home, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


def draw_info_attack(type_1, type_2, type_3):
    attack_1 = "power attack 1 : " + str(type_1)
    attack_2 = "power attack 2 : " + str(type_2)
    attack_3 = "power attack 3 : " + str(type_3)
    attack_1_x = SCREEN_WIDTH // 2 - score_font.size(attack_1)[0] // 2
    attack_2_x = SCREEN_WIDTH // 2 - score_font.size(attack_2)[0] // 2
    attack_3_x = SCREEN_WIDTH // 2 - score_font.size(attack_3)[0] // 2
    attack_1_y = 350
    attack_2_y = 400
    attack_3_y = 450
    draw_text(attack_1, score_font, RED, attack_1_x, attack_1_y)
    draw_text(attack_2, score_font, RED, attack_2_x, attack_2_y)
    draw_text(attack_3, score_font, RED, attack_3_x, attack_3_y)


# function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))

    # <<<<<<< HEAD
    #   pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))
    # # Thanh mana
    # def draw_mana_bar(mana, x, y):
    #   ratio = mana / 100  # Giả sử mana tối đa là 100
    #   pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 14))  # Khung thanh mana
    #   pygame.draw.rect(screen, BLUE, (x, y, 400, 10))  # Thanh nền
    #   pygame.draw.rect(screen, BLUE, (x, y, 400 * ratio, 10))  # Thanh mana
    # # Hàm cho màn hình menu chính
    # def main_menu():
    #     selection = 0  # 0: Play, 1: Options, 2: Quit
    #     options = ["Fighting", "Options", "Quit"]  # Danh sách các tùy chọn menu
    #     while True:
    #         # screen.fill(WHITE)  # Xóa màn hình
    #         draw_home()
    # =======
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))


# Hàm cho màn hình menu chính
def main_menu():
    selection = 0  # 0: Play, 1: Options, 2: Quit
    options = ["Fighting", "Options", "Quit"]  # Danh sách các tùy chọn menu


# >>>>>>> origin/huy_dev
# Thanh mana
def draw_mana_bar(mana, x, y):
    ratio = mana / 100  # Giả sử mana tối đa là 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 14))  # Khung thanh mana
    pygame.draw.rect(screen, BLUE, (x, y, 400, 10))  # Thanh nền
    pygame.draw.rect(screen, BLUE, (x, y, 400 * ratio, 10))  # Thanh mana


# Hàm cho màn hình menu chính
def main_menu():
    selection = 0  # 0: Play, 1: Options, 2: Quit
    options = ["Fighting", "Options", "Quit"]  # Danh sách các tùy chọn menu
    while True:
        # screen.fill(WHITE)  # Xóa màn hình
        draw_home()

        # Vẽ tiêu đề
        title_text = count_font.render("Fighter Game", True, RED)
        screen.blit(
            title_text,
            (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3),
        )
        # Cách khoảng giữa tiêu đề và các nút menu
        menu_start_y = SCREEN_HEIGHT // 2 + 50  # Điều chỉnh khoảng cách từ tiêu đề

        # Vẽ các tùy chọn menu
        for i, option in enumerate(options):
            option_y = (
                menu_start_y + (i - (len(options) - 1) / 2) * 50
            )  # Căn giữa theo chiều dọc
            option_x = (
                SCREEN_WIDTH // 2 - score_font.size(option)[0] // 2
            )  # Căn giữa theo chiều ngang
            draw_text(
                option, score_font, GREEN if i == selection else RED, option_x, option_y
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selection = (selection - 1) % len(options)  # Di chuyển lên
                if event.key == pygame.K_DOWN:
                    selection = (selection + 1) % len(options)  # Di chuyển xuống
                if event.key == pygame.K_RETURN:
                    if options[selection] == "Fighting":
                        player1 = character_select("player 1")
                        player2 = character_select("player 2")
                        mode = mode_select()
                        game_loop(player1, player2, mode)
                    elif options[selection] == "Options":
                        continue  # ông Thắng chẹck lại phần này
                    elif options[selection] == "Quit":
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
        clock.tick(FPS)


def mode_select():
    selection = 0
    options = ["Normal", "Hard"]
    while True:
        draw_home()
        title = "Select mode game"
        title_x = SCREEN_WIDTH // 2 - count_font.size(title)[0] // 2
        title_y = 100  # Đặt tiêu đề ở phía trên menu, khoảng 100 pixel từ trên xuống
        draw_text(title, count_font, RED, title_x, title_y)

        option_widths = [score_font.size(option)[0] for option in options]
        total_width = (
            sum(option_widths) + (len(options) - 1) * 20
        )  # Tổng chiều rộng của tất cả các tùy chọn và khoảng cách giữa chúng

        # Căn giữa theo chiều ngang
        menu_start_x = (SCREEN_WIDTH - total_width) // 2
        menu_y = (
            SCREEN_HEIGHT // 2 - score_font.get_height() // 2
        )  # Căn giữa theo chiều dọc

        # Hiển thị từng tùy chọn
        x = menu_start_x
        for i, option in enumerate(options):
            draw_text(option, score_font, GREEN if i == selection else RED, x, menu_y)
            x += option_widths[i] + 20  # Di chuyển vị trí x cho tùy chọn tiếp theo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selection = (selection - 1) % len(options)
                if event.key == pygame.K_RIGHT:
                    selection = (selection + 1) % len(options)
                if event.key == pygame.K_RETURN:
                    if options[selection] == "Normal":
                        return 0
                    if options[selection] == "Hard":
                        return 1

        pygame.display.update()
        clock.tick(FPS)


def character_select(player):
    selection = 0
    options = [
        "Warrior",
        "MartialHero",
        "MedievalKing",
        "MedievalKnight",
        "Knight",
        "Huntress",
    ]
    while True:
        draw_home()
        title = "Choose Your Character"
        title_x = SCREEN_WIDTH // 2 - count_font.size(title)[0] // 2
        title_y = 100  # Đặt tiêu đề ở phía trên menu, khoảng 100 pixel từ trên xuống
        draw_text(title, count_font, RED, title_x, title_y)
        player_text = player
        player_x = SCREEN_WIDTH // 2 - count_font.size(player_text)[0] // 2
        player_y = (
            title_y + 70
        )  # Đặt cách dòng "Choose Your Character" 50 pixel bên dưới
        draw_text(player_text, count_font, RED, player_x, player_y)

        option_widths = [score_font.size(option)[0] for option in options]
        total_width = (
            sum(option_widths) + (len(options) - 1) * 20
        )  # Tổng chiều rộng của tất cả các tùy chọn và khoảng cách giữa chúng

        # Căn giữa theo chiều ngang
        menu_start_x = (SCREEN_WIDTH - total_width) // 2
        menu_y = (
            SCREEN_HEIGHT // 2 - score_font.get_height() // 2
        )  # Căn giữa theo chiều dọc

        # Hiển thị từng tùy chọn
        x = menu_start_x
        for i, option in enumerate(options):
            draw_text(option, score_font, GREEN if i == selection else RED, x, menu_y)
            x += option_widths[i] + 20  # Di chuyển vị trí x cho tùy chọn tiếp theo

        draw_info_attack(
            characters[options[selection]].information[1],
            characters[options[selection]].information[2],
            characters[options[selection]].information[3],
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    selection = (selection - 1) % len(options)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    selection = (selection + 1) % len(options)
                if event.key == pygame.K_RETURN or event.key == pygame.K_j:
                    if options[selection] == "Knight":
                        return characters["Knight"]
                    if options[selection] == "MartialHero":
                        return characters["MartialHero"]
                    if options[selection] == "MedievalKing":
                        return characters["MedievalKing"]
                    if options[selection] == "MedievalKnight":
                        return characters["MedievalKnight"]
                    if options[selection] == "Warrior":
                        return characters["Warrior"]
                    if options[selection] == "Huntress":
                        return characters["Huntress"]

        pygame.display.update()
        clock.tick(FPS)


def pause_menu(paused):
    selection = 0
    options = ["Resume", "Quit"]

    while paused:
        draw_bg()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selection = (selection - 1) % len(options)
                if event.key == pygame.K_DOWN:
                    selection = (selection + 1) % len(options)
                if event.key == pygame.K_RETURN:
                    if options[selection] == "Resume":
                        paused = False  # Tiếp tục chơi
                    elif options[selection] == "Quit":
                        main_menu()

        # Hiển thị menu tạm dừng
        # Vẽ tiêu đề
        title_text = count_font.render("Game Paused", True, RED)
        screen.blit(
            title_text,
            (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3),
        )
        for i, option in enumerate(options):
            option_y = SCREEN_HEIGHT // 2 + (i - (len(options) - 1) // 2) * 50
            option_x = SCREEN_WIDTH // 2 - score_font.size(option)[0] // 2
            draw_text(
                option, score_font, GREEN if i == selection else RED, option_x, option_y
            )

        pygame.display.update()
        clock.tick(FPS)


def game_loop(player1, player2, mode):
    global intro_count, last_count_update, score, round_over, fighter_1, fighter_2  # Cập nhật biến toàn cục

    # player selections
    character_p1 = player1
    character_p2 = player2

    # Khởi tạo hai chiến binh
    fighter_1 = Fighter(1, 200, 310, False, character_p1)
    fighter_2 = Fighter(2, 700, 310, True, character_p2)

    # Reset các biến
    round_over = False
    intro_count = 3
    last_count_update = pygame.time.get_ticks()
    score = [0, 0]
    # Số vòng tối đa

    run = True
    paused = False  # Thêm biến tạm dừng
    while run:
        if paused:  # Kiểm tra trạng thái tạm dừng
            paused = pause_menu(paused)
        else:
            # <<<<<<< HEAD
            #           # Vẽ nền
            #           draw_bg()

            #           # Hiển thị thanh sức khỏe
            #           draw_health_bar(fighter_1.health, 20, 20)
            #           draw_health_bar(fighter_2.health, 580, 20)
            #           draw_mana_bar(fighter_1.mana, 20, 50)  # Vẽ thanh mana cho Player 1
            #           draw_mana_bar(fighter_2.mana, 580, 50) # Vẽ thanh mana cho Player 2
            #           draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
            #           draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)
            # =======
            # Vẽ nền
            draw_bg()
            # >>>>>>> origin/huy_dev
            # Hiển thị thanh sức khỏe
            draw_health_bar(fighter_1.health, 20, 20)
            draw_health_bar(fighter_2.health, 580, 20)
            draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
            draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)

            # Cập nhật đếm ngược
            if intro_count <= 0:
                # Di chuyển chiến binh
                fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2, round_over)
                fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1, round_over)

                if mode == 1:
                    global current_bomb, last_spawn_time, spawn_interval, f1_isHit, f2_isHit, explosion_rect

                    current_time = time.time()

                    if current_bomb is None:
                        if current_time - last_spawn_time >= spawn_interval:
                            current_bomb = Bomb(
                                screen,
                                pygame.image.load(
                                    "assets/images/background/bomb.png"
                                ).convert_alpha(),
                                [4, 8],
                            )
                            last_spawn_time = (
                                current_time  # Cập nhật thời gian tạo Bomb mới
                            )
                            spawn_interval = random.uniform(1, 3)

                    # Di chuyển và vẽ Bomb nếu tồn tại
                    if current_bomb:
                        current_bomb.move_down()  # Di chuyển Bomb xuống
                        current_bomb.update_bom()
                        # current_bomb.draw_explosion()
                        current_bomb.drawbomb()  # Vẽ Bomb trên màn hình

                        # Kiểm tra nếu Bomb ra khỏi màn hình, xóa nó và tạo mới
                        if (
                            current_bomb.is_off_screen()
                            or current_bomb.is_dropped_to_fighter(fighter_1)
                            or current_bomb.is_dropped_to_fighter(fighter_2)
                        ):
                            current_bomb.explode = True
                            explosion_rect = current_bomb.draw_explosion()

                            if not f1_isHit:
                                f1_isHit = fighter_1.check_hit(explosion_rect)
                            if not f2_isHit:
                                f2_isHit = fighter_2.check_hit(explosion_rect)
                        if current_bomb.frame_index == 7:
                            current_bomb = (
                                None  # Đặt lại để tạo Bomb mới ở lần tiếp theo
                            )
                            f1_isHit = f2_isHit = False
                            continue
            else:
                # Hiển thị bộ đếm
                draw_text(
                    str(intro_count),
                    count_font,
                    RED,
                    SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 3,
                )

                # Cập nhật bộ đếm
                if (pygame.time.get_ticks() - last_count_update) >= 1000:
                    intro_count -= 1
                    last_count_update = pygame.time.get_ticks()

            # Cập nhật chiến binh
            fighter_1.update()
            fighter_2.update()

            # Vẽ chiến binh
            fighter_1.draw(screen)
            fighter_2.draw(screen)

            spear_group.update()
            spear_group.draw(screen)

            # Kiểm tra kết quả
            if not round_over:
                if not fighter_1.alive:
                    score[1] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
                elif not fighter_2.alive:
                    score[0] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()

            else:
                # Hiển thị hình chiến thắng
                if score[0] < 2 or score[1] < 2:
                    screen.blit(victory_img, (360, 150))
                    pygame.display.update()  # Cập nhật màn hình
                if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                    # Kiểm tra xem người chơi nào đã thắng (đạt 2 điểm)
                    if score[0] == 2 or score[1] == 2:
                        # Làm mới màn hình
                        draw_bg()
                        winner = "Player 1 Wins!" if score[0] == 2 else "Player 2 Wins!"
                        # Lấy kích thước văn bản
                        text_width, text_height = score_font_winner.size(winner)
                        text_x = (SCREEN_WIDTH - text_width) // 2
                        text_y = 150  # Bạn có thể điều chỉnh vị trí theo ý muốn

                        # Vẽ văn bản
                        draw_text(winner, score_font_winner, YELLOW, text_x, text_y)
                        pygame.display.update()
                        pygame.time.wait(3000)  # Đợi 3 giây trước khi quay lại menu
                        main_menu()  # Quay lại menu chính
                    round_over = False
                    intro_count = 3

                    fighter_1 = Fighter(1, 200, 310, False, character_p1)
                    fighter_2 = Fighter(2, 700, 310, True, character_p2)

                    # Xử lý sự kiện
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if (
                        event.key == pygame.K_SPACE
                    ):  # Nếu nhấn phím Space, tạm dừng trò chơi
                        paused = not paused  # Thay đổi trạng thái tạm dừng
                    if event.key == pygame.K_t:  # Player 1 dùng chiêu
                        fighter_1.ability_t()
                    if event.key == pygame.K_e:  # Player 1 tăng mana
                        fighter_1.ability_e(hit_successful=True)  # Tăng 10 mana
                    if event.key == pygame.K_r:  # Player 1 tăng mana
                        fighter_1.ability_r(hit_successful=True)  # Tăng 5 mana
                    if event.key == pygame.K_o:  # Player 2 dùng chiêu
                        fighter_2.ability_o()
                    if event.key == pygame.K_u:  # Player 2 tăng mana
                        fighter_2.ability_u(hit_successful=True)  # Tăng 10 mana
                    if event.key == pygame.K_i:  # Player 2 tăng mana
                        fighter_2.ability_i(hit_successful=True)  # Tăng 5 mana

            # Cập nhật hiển thị
            pygame.display.update()
            clock.tick(FPS)  # Đảm bảo trò chơi chạy với tốc độ khung hình ổn định


# Bắt đầu màn hình menu chính
main_menu()


# Thoát pygame
pygame.quit()
