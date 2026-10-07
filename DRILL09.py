from pico2d import *
 
canvas_width = 1280
canvas_height = 1024

open_canvas(canvas_width, canvas_height)

background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running
    global dir_x, dir_y, face_dir
 
running = True
x = canvas_width // 2
y = canvas_height // 2
frame = 0
dir_x = 0       # -1: 왼쪽, 0: 정지, 1: 오른쪽
dir_y = 0       # -1: 아래, 0: 정지, 1: 위
face_dir = 1 # 1: 오른쪽, -1: 왼쪽

