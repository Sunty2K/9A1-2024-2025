import pygame as unity
import random
import time
import threading
import queue
import os
import json
import requests
import psutil
from pygame import mixer


# Khởi tạo unity
unity.init()
mixer.init()
WIDTH, HEIGHT = 1000, 600
screen = unity.display.set_mode((WIDTH, HEIGHT))
unity.display.set_caption("Click Game")
clock = unity.time.Clock()

# Đường dẫn tới thư mục người dùng
user_dir = os.path.join(os.path.expanduser("~"), "click_game")
os.makedirs(user_dir, exist_ok=True)
user_data_file = os.path.join(user_dir, "user_data.json")

# Webhook Discord
#WEBHOOK_URL = "https://discord.com/api/webhooks/1362268125005086820/vAlReIlTfkj528jkYMWEAdYS1DTw8o2eAuwZPW_bbNWzuiXTtDOGpAR6ujqgXzSCvil0"

# Trạng thái game
MENU = 0
COUNTDOWN = 1
PLAYING = 2
GAME_OVER = 3
game_state = MENU

# Ẩn con trỏ chuột mặc định
unity.mouse.set_visible(False)

# Load hình ảnh crosshair
try:
    crosshair_img = unity.image.load("mouse.png").convert_alpha()
    original_width, original_height = crosshair_img.get_size()
    crosshair_img = unity.transform.scale(crosshair_img, (int(original_width * 5/3), int(original_height * 5/3)))
except:
    # Fallback nếu không tìm thấy file
    crosshair_img = unity.Surface((20, 20), unity.SRCALPHA)
    unity.draw.circle(crosshair_img, (255, 0, 0), (10, 10), 10)
    unity.draw.circle(crosshair_img, (0, 0, 0, 0), (10, 10), 5)

crosshair_rect = crosshair_img.get_rect()

# Cài đặt thời gian và điểm
time_spam = 0.5
time_despam = 2
last_spawn_time = 5
point = 0
max_point = 0
point_down = 0.5
click_count = 0
cps = 0
last_cps_reset = time.time()
countdown_timer = 10
countdown_start_time = 0
player_name = ""
highest_score_in_session = 0  # Để theo dõi điểm cao nhất trong phiên chơi hiện tại

# Fonts
font = unity.font.SysFont(None, 30)
big_font = unity.font.SysFont(None, 100)
medium_font = unity.font.SysFont(None, 50)

# Vùng spawn hình tròn (toàn màn hình)
RECT_X = 0
RECT_Y = 0
RECT_WIDTH = WIDTH
RECT_HEIGHT = HEIGHT
spawn_area = unity.Rect(RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT)

# Vùng cấm spawn (góc trái trên)
forbidden_area = unity.Rect(0, 0, 250, 100)

# Danh sách các hình tròn và khóa để truy cập an toàn
circles = []
circles_lock = threading.Lock()

# Queue cho việc truyền dữ liệu giữa các luồng
circle_queue = queue.Queue()
point_queue = queue.Queue()
removal_queue = queue.Queue()

# Các thư mục âm thanh
sounds_dir = "sounds"
if not os.path.exists(sounds_dir):
    os.makedirs(sounds_dir)

# Đường dẫn tới các file âm thanh
sound_files = {
    "hit_center": os.path.join(sounds_dir, "hit_center.wav"),
    "hit_inner": os.path.join(sounds_dir, "hit_inner.wav"),
    "hit_outer": os.path.join(sounds_dir, "hit_outer.wav"),
    "miss": os.path.join(sounds_dir, "miss.wav"),
    "game_over": os.path.join(sounds_dir, "game_over.wav"),
    "countdown": os.path.join(sounds_dir, "countdown.wav"),
    "countdown_final": os.path.join(sounds_dir, "countdown_final.wav"),
    "bg_music": os.path.join(sounds_dir, "bg_music.mp3"),
    "game_over_music": os.path.join(sounds_dir, "game_over_music.mp3")
}

# Tạo một số file âm thanh đơn giản nếu chúng không tồn tại
def create_default_sounds():
    try:
        # Tạo âm thanh đơn giản sử dụng pygame
        for sound_name in ["hit_center", "hit_inner", "hit_outer", "miss", "countdown", "countdown_final", "game_over"]:
            if not os.path.exists(sound_files[sound_name]):
                try:
                    # Tạo âm thanh tạm thời
                    dummy_sound = unity.Surface((10, 10))  # Tạo Surface giả
                    dummy_sound_path = os.path.join(sounds_dir, f"{sound_name}_temp.wav")
                    unity.mixer.Sound(dummy_sound_path).play()  # Sẽ gây lỗi nhưng không sao
                except:
                    # Tạo file âm thanh trống nếu không thể tạo âm thanh
                    with open(sound_files[sound_name], 'wb') as f:
                        f.write(b'RIFF$\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00\x00\x04\x00\x00\x01\x00\x08\x00data\x00\x00\x00\x00')
                
        # Lưu ý: để tạo file MP3, bạn cần sử dụng thư viện khác
        # Tại đây chúng ta chỉ kiểm tra xem file có tồn tại không
        if not os.path.exists(sound_files["bg_music"]):
            print(f"Warning: {sound_files['bg_music']} not found. Background music will be disabled.")
        if not os.path.exists(sound_files["game_over_music"]):
            print(f"Warning: {sound_files['game_over_music']} not found. Game over music will be disabled.")
    except Exception as e:
        print(f"Error creating default sounds: {e}")
        # Không ngăn trò chơi tiếp tục nếu có lỗi tạo âm thanh

# Hàm để phát âm thanh
def play_sound(sound_name):
    try:
        if os.path.exists(sound_files[sound_name]):
            sound = mixer.Sound(sound_files[sound_name])
            sound.play()
    except Exception as e:
        print(f"Error playing sound {sound_name}: {e}")

# Hàm để phát nhạc nền
def play_music(music_name, loops=-1):
    try:
        if os.path.exists(sound_files[music_name]):
            mixer.music.load(sound_files[music_name])
            mixer.music.play(loops)
    except Exception as e:
        print(f"Error playing music {music_name}: {e}")

# Hàm dừng nhạc nền
def stop_music():
    try:
        mixer.music.stop()
    except Exception as e:
        print(f"Error stopping music: {e}")

# Hàm gửi điểm số lên Discord qua webhook
def send_score_to_discord(name, score):
    try:
        # Đảm bảo score không âm khi hiển thị
        display_score = max(0, score)
        
        # Tạo tin nhắn với emoji
        emojis = {
            "start": "🎮",
            "good": "🎯",
            "medium": "👍",
            "bad": "😢"
        }
        
        # Chọn emoji dựa trên điểm số
        if display_score > 20:
            emoji = emojis["good"]
        elif display_score > 10:
            emoji = emojis["medium"]
        else:
            emoji = emojis["bad"]
            
        message = {
            "content": f"{emojis['start']} **{name}** đã đạt được **{display_score:.2f}** điểm! {emoji}"
        }
        
        # Gửi webhook
        response = requests.post(WEBHOOK_URL, json=message)
        if response.status_code != 204:
            print(f"Failed to send score to Discord: {response.status_code}")
    except Exception as e:
        print(f"Error sending score to Discord: {e}")

# Hàm đọc dữ liệu người dùng
def load_user_data():
    global player_name, max_point
    try:
        if os.path.exists(user_data_file):
            with open(user_data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                player_name = data.get("name", "")
                max_point = data.get("max_score", 0)
    except Exception as e:
        print(f"Error loading user data: {e}")

# Hàm lưu dữ liệu người dùng
def save_user_data():
    try:
        with open(user_data_file, 'w', encoding='utf-8') as f:
            json.dump({
                "name": player_name,
                "max_score": max_point
            }, f)
    except Exception as e:
        print(f"Error saving user data: {e}")

# Hàm tạo hình tròn bên trong vùng cho phép
def spawn_circle():
    while True:
        radius = random.randint(20, 50) + 2
        x = random.randint(spawn_area.left + radius, spawn_area.right - radius)
        y = random.randint(spawn_area.top + radius, spawn_area.bottom - radius)
        if not forbidden_area.collidepoint(x, y):
            return {
                'pos': (x, y),
                'radius': radius,
                'spawn_time': time.time(),
                'id': time.time()  # Unique ID for each circle
            }

# Hàm cập nhật điểm cao nhất
def update_max_score(current_score):
    global max_point, highest_score_in_session
    
    # Cập nhật điểm cao nhất trong phiên chơi hiện tại
    highest_score_in_session = max(highest_score_in_session, current_score)
    
    # Cập nhật điểm cao nhất toàn thời gian
    if highest_score_in_session > max_point:
        max_point = highest_score_in_session
        save_user_data()
        return True  # Có điểm cao mới
    return False  # Không có điểm cao mới

# Luồng xử lý việc spawn và despawn các hình tròn
def circle_management():
    global last_spawn_time
    while running:
        if game_state == PLAYING:
            current_time = time.time()
            
            # Spawn hình tròn mới
            if current_time - last_spawn_time >= time_spam:
                circle_queue.put(spawn_circle())
                last_spawn_time = current_time
            
            # Xử lý despawn
            with circles_lock:
                for circle in circles[:]:
                    if current_time - circle['spawn_time'] >= time_despam:
                        circles.remove(circle)
                        point_queue.put(-point_down)  # Giảm điểm
                        play_sound("miss")
            
            # Nếu không còn hình tròn nào, tạo mới ngay
            with circles_lock:
                if len(circles) == 0:
                    circle_queue.put(spawn_circle())
                    last_spawn_time = current_time
        
        # Delay để giảm tải CPU
        time.sleep(0.01)

# Luồng xử lý CPS và các tác vụ tính toán khác
def stats_processing():
    global cps, click_count, last_cps_reset, game_state, point
    while running:
        if game_state == PLAYING:
            current_time = time.time()
            
            # Reset CPS
            if current_time - last_cps_reset >= 3:
                with circles_lock:  # Bảo vệ biến toàn cục
                    cps = click_count / 3
                    click_count = 0
                    last_cps_reset = current_time
            
            # Kiểm tra điểm số
            if point < 0:
                # Cập nhật điểm cao nhất
                update_max_score(highest_score_in_session)
                
                # Chuyển sang trạng thái game over
                game_state = GAME_OVER
                play_sound("game_over")
                stop_music()
                play_music("game_over_music", 0)  # Phát 1 lần
                
                # Gửi điểm lên Discord
                if player_name:
                    threading.Thread(target=send_score_to_discord, args=(player_name, highest_score_in_session)).start()
        
        # Delay để giảm tải CPU
        time.sleep(0.1)

# Hàm xử lý input text
def get_input_text(prompt, initial_text=""):
    text = initial_text
    input_active = True
    
    while input_active and running:
        for event in unity.event.get():
            if event.type == unity.QUIT:
                return None
            elif event.type == unity.KEYDOWN:
                if event.key == unity.K_RETURN:
                    input_active = False
                elif event.key == unity.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        
        # Vẽ nền
        screen.fill((30, 30, 30))
        
        # Vẽ prompt
        prompt_text = medium_font.render(prompt, True, (255, 255, 255))
        screen.blit(prompt_text, (WIDTH//2 - prompt_text.get_width()//2, HEIGHT//2 - 50))
        
        # Vẽ input box
        input_text = medium_font.render(text + "|", True, (255, 255, 255))
        screen.blit(input_text, (WIDTH//2 - input_text.get_width()//2, HEIGHT//2 + 10))
        
        # Vẽ crosshair
        mouse_x, mouse_y = unity.mouse.get_pos()
        crosshair_rect.center = (mouse_x, mouse_y)
        screen.blit(crosshair_img, crosshair_rect)
        
        unity.display.flip()
        clock.tick(float('inf'))
    
    return text

# Tạo âm thanh mặc định nếu chưa có
create_default_sounds()

# Đọc dữ liệu người dùng
load_user_data()

# Biến điều khiển trạng thái các luồng
running = True

# Khởi động các luồng
circle_thread = threading.Thread(target=circle_management)
stats_thread = threading.Thread(target=stats_processing)
circle_thread.daemon = True
stats_thread.daemon = True
circle_thread.start()
stats_thread.start()

# Vòng lặp chính
while running:
    dt = clock.tick(float("inf"))
    
    # Lấy tên người chơi nếu chưa có
    if game_state == MENU:
        if not player_name:
            player_name = get_input_text("enter your name:", player_name)
            save_user_data()
        
        # Vẽ menu
        screen.fill((30, 30, 30))
        
        title_text = big_font.render("Click Game", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//4))
        
        if player_name:
            welcome_text = medium_font.render(f"Welcome , {player_name}!", True, (255, 255, 255))
            screen.blit(welcome_text, (WIDTH//2 - welcome_text.get_width()//2, HEIGHT//2 - 50))
        
        start_text = medium_font.render("click SPACE to start", True, (255, 255, 255))
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2 + 50))
        
        max_score_text = medium_font.render(f"highest point: {max_point:.2f}", True, (255, 255, 0))
        screen.blit(max_score_text, (WIDTH//2 - max_score_text.get_width()//2, HEIGHT//2 + 100))
        
        # Xử lý sự kiện trong menu
        for event in unity.event.get():
            if event.type == unity.QUIT:
                running = False
            if event.type == unity.KEYDOWN:
                if event.key == unity.K_ESCAPE:
                    running = False
                elif event.key == unity.K_SPACE:
                    # Reset điểm cao nhất trong phiên chơi
                    highest_score_in_session = 0
                    
                    # Chuyển sang trạng thái đếm ngược
                    game_state = COUNTDOWN
                    countdown_start_time = time.time()
                    countdown_timer = 5
                    play_sound("countdown")
    
    # Xử lý đếm ngược
    elif game_state == COUNTDOWN:
        current_time = time.time()
        elapsed = current_time - countdown_start_time
        remaining = countdown_timer - int(elapsed)
        
        if remaining <= 0:
            # Bắt đầu game
            game_state = PLAYING
            point = 0
            last_spawn_time = time.time()
            with circles_lock:
                circles.clear()
            play_music("bg_music")
        else:
            # Vẽ đếm ngược
            screen.fill((30, 30, 30))
            
            countdown_text = big_font.render(str(remaining), True, (255, 255, 255))
            screen.blit(countdown_text, (WIDTH//2 - countdown_text.get_width()//2, HEIGHT//2 - countdown_text.get_height()//2))
            
            # Phát âm thanh đếm ngược khi còn 1 giây
            if remaining == 1 and int(elapsed) != int(elapsed - 0.1):
                play_sound("countdown_final")
            
            # Xử lý sự kiện trong đếm ngược
            for event in unity.event.get():
                if event.type == unity.QUIT:
                    running = False
                if event.type == unity.KEYDOWN and event.key == unity.K_ESCAPE:
                    game_state = MENU
    
    # Xử lý chơi game
    elif game_state == PLAYING:
        # Xử lý các hình tròn mới từ luồng quản lý
        while not circle_queue.empty():
            try:
                new_circle = circle_queue.get_nowait()
                with circles_lock:
                    circles.append(new_circle)
                circle_queue.task_done()
            except queue.Empty:
                break
        
        # Xử lý thay đổi điểm từ các luồng khác
        while not point_queue.empty():
            try:
                point_change = point_queue.get_nowait()
                point += point_change
                point_queue.task_done()
            except queue.Empty:
                break
        
        # Cập nhật điểm cao nhất trong phiên chơi
        highest_score_in_session = max(highest_score_in_session, point)
        
        # Xử lý sự kiện
        for event in unity.event.get():
            if event.type == unity.QUIT:
                running = False
            if event.type == unity.KEYDOWN:
                if event.key == unity.K_ESCAPE:
                    # Cập nhật điểm cao nhất
                    if update_max_score(highest_score_in_session):
                        # Gửi điểm lên Discord nếu đạt điểm cao mới
                        if player_name:
                            threading.Thread(target=send_score_to_discord, args=(player_name, max_point)).start()
                    game_state = MENU
                    stop_music()

            elif event.type == unity.MOUSEBUTTONDOWN or (event.type == unity.KEYDOWN and event.key in [unity.K_SPACE, unity.K_z, unity.K_x]):

                mouse_pos = unity.mouse.get_pos()
                with circles_lock:
                    for circle in circles[:]:
                        x, y = circle['pos']
                        r = circle['radius']
                        inner_r = r // 2  # Vòng giữa (inner ring)
                        center_r = r // 4  # Vòng tâm (center)

                        dx = mouse_pos[0] - x
                        dy = mouse_pos[1] - y
                        dist_sq = dx**2 + dy**2

                        if dist_sq <= center_r ** 2:
                            # Bắn trúng tâm
                            point += 1
                            click_count += 1
                            circles.remove(circle)
                            play_sound("hit_center")
                            break
                        elif dist_sq <= inner_r ** 2:
                            # Bắn trúng vòng giữa
                            point += 0.5
                            click_count += 1
                            circles.remove(circle)
                            play_sound("hit_inner")
                            break
                        elif dist_sq <= r ** 2:
                            # Bắn trúng rìa
                            point += 0.5
                            click_count += 1
                            circles.remove(circle)
                            play_sound("hit_outer")
                            break

        # Vẽ nền
        screen.fill((30, 30, 30))

        # Vẽ các hình tròn
        with circles_lock:
            for circle in circles:
                x, y = circle['pos']
                r = circle['radius']
                inner_r = r // 2
                center_r = r // 4
                unity.draw.circle(screen, (0, 255, 0), (x, y), r)
                unity.draw.circle(screen, (255, 255, 0), (x, y), inner_r)
                unity.draw.circle(screen, (0, 0, 255), (x, y), center_r)

        # Hiển thị thông tin
        fps_text = font.render(f"FPS: {clock.get_fps():.2f}", True, (255, 255, 255))
        cps_text = font.render(f"PointPerSecond: {cps:.2f}", True, (255, 255, 255))
        point_text = font.render(f"Point: {point:.2f}", True, (255, 255, 255))
        max_point_text = font.render(f"Max Point: {max_point:.2f}", True, (255, 255, 255))
        high_session_text = font.render(f"Session Best: {highest_score_in_session:.2f}", True, (255, 255, 255))
        
        # Hiển thị RAM usage
        process = psutil.Process(os.getpid())
        ram_usage = process.memory_info().rss / 1024 / 1024  # Convert to MB
        ram_text = font.render(f"RAM: {ram_usage:.2f} MB", True, (255, 255, 255))

        screen.blit(fps_text, (10, 10))
        screen.blit(cps_text, (10, 40))
        screen.blit(point_text, (10, 70))
        screen.blit(max_point_text, (10, 100))
        screen.blit(high_session_text, (10, 130))
        screen.blit(ram_text, (10, 160))

    # Xử lý game over
    elif game_state == GAME_OVER:
        screen.fill((30, 30, 30))
        
        game_over_text = big_font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//4))
        
        # Hiển thị điểm cao nhất trong phiên chơi hiện tại, không phải điểm khi thua
        session_score_text = medium_font.render(f"highest point: {highest_score_in_session:.2f}", True, (255, 255, 255))
        screen.blit(session_score_text, (WIDTH//2 - session_score_text.get_width()//2, HEIGHT//2 - 50))
        
        # Kiểm tra xem có phải là điểm cao mới hay không
        if highest_score_in_session > max_point:
            max_point = highest_score_in_session
            save_user_data()
            high_score_text = medium_font.render("new high point", True, (255, 255, 0))
            screen.blit(high_score_text, (WIDTH//2 - high_score_text.get_width()//2, HEIGHT//2))
        
        restart_text = medium_font.render("click SPACE to restart", True, (255, 255, 255))
        menu_text = medium_font.render("click ESC to back menu", True, (255, 255, 255))
        
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 50))
        screen.blit(menu_text, (WIDTH//2 - menu_text.get_width()//2, HEIGHT//2 + 100))
        
        # Xử lý sự kiện trong game over
        for event in unity.event.get():
            if event.type == unity.QUIT:
                running = False
            if event.type == unity.KEYDOWN:
                if event.key == unity.K_ESCAPE:
                    game_state = MENU
                    stop_music()
                elif event.key == unity.K_SPACE:
                    # Chơi lại
                    highest_score_in_session = 0  # Reset điểm phiên chơi
                    game_state = COUNTDOWN
                    countdown_start_time = time.time()
                    countdown_timer = 5
                    play_sound("countdown")
                    stop_music()

    # Vẽ crosshair
    mouse_x, mouse_y = unity.mouse.get_pos()
    crosshair_rect.center = (mouse_x, mouse_y)
    screen.blit(crosshair_img, crosshair_rect)

    unity.display.flip()

# Lưu điểm cao nhất trước khi thoát
update_max_score(highest_score_in_session)

# Đảm bảo tất cả các luồng đều dừng lại khi thoát
running = False
unity.quit()