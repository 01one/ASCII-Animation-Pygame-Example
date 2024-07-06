import pygame
import glob
import os
import time

pygame.init()


width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ASCII Animation Pygame")

font_path = "DejaVuSans.ttf"
font_size = 12
font = pygame.font.Font(font_path, font_size)



if os.path.exists("text_frame"):
    try:
        frame_files = glob.glob("text_frame/*.txt")
    except Exception as e:
        print(f"Error accessing text files: {e}")
else:
    from zipfile import ZipFile
    try:
        with ZipFile('text_frame.zip', 'r') as mainfile:
            mainfile.extractall()
        frame_files = glob.glob("text_frame/*.txt")
    except Exception as e:
        print(f"Error extracting zip file: {e}")
        frame_files = []



frame_files.sort()
frames = []

for filename in frame_files:
    with open(filename, "r", encoding="utf8") as f:
        frames.append(f.readlines())


running = True
frame_index = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))
    
    #adjust y offset .. its ajusted to -100 for this program. 
    #y_offset=0
    y_offset = -100
    for line in frames[frame_index]:
        text_surface = font.render(line.strip(), True, (255, 255, 255))
        screen.blit(text_surface, (10, y_offset))
        y_offset += font_size

    pygame.display.update()


    frame_index = (frame_index + 1) % len(frames)
    time.sleep(0.040)
    clock.tick(25)

pygame.quit()
