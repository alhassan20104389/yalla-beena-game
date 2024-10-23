import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math as mm
from math import sin, cos, pi

def start_menu():
    pg.init()
    

    screen = pg.display.set_mode((800, 600))
    font_title = pg.font.Font(None, 72)
    font_prompt = pg.font.Font(None, 36)
    

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                return
            if event.type == KEYDOWN and event.key == K_RETURN:
                return
        
        screen.fill((255, 255, 255))
        
        text_title = font_title.render("YALLA BEENA", True, (0.5, 0, 0))
        text_prompt = font_prompt.render("Press ENTER to start", True, (0, 0, 0))
        
        text_title_rect = text_title.get_rect(center=(400, 200))
        text_prompt_rect = text_prompt.get_rect(center=(400, 400))
        
        screen.blit(text_title, text_title_rect)
        screen.blit(text_prompt, text_prompt_rect)
        

        pg.display.flip()

    pg.init()
    clock = pg.time.Clock()
    angle = 0

    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
    font = pg.font.Font(None, 72)
    font_prompt = pg.font.Font(None, 36)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return  # Return to the previous screen if ESC key is pressed
                elif event.key == pg.K_r:  # Restart the game if 'R' key is pressed
                    pg.quit()
                    main()  # Restart the game
                elif event.key == pg.K_q:  # Quit the game if 'Q' key is pressed
                    pg.quit()
                    return

        screen.fill((255, 255, 255))
        
        # Update rotation angle
        angle += 1
        
        # Rotate the text
        rotated_text = pg.transform.rotate(font.render("GAME OVER", True, (255, 0, 0)), angle)
        rotated_text_rect = rotated_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        
        text_prompt_restart = font_prompt.render("Press R to Restart", True, (0, 0, 0))
        text_prompt_quit = font_prompt.render("Press Q to Quit", True, (0, 0, 0))
        
        # Position "Press R to Restart" on the left
        text_prompt_restart_rect = text_prompt_restart.get_rect(left=50, top=screen.get_height() // 2 + 50)
        
        # Position "Press Q to Quit" on the right
        text_prompt_quit_rect = text_prompt_quit.get_rect(right=screen.get_width() - 50, top=screen.get_height() // 2 + 50)
        
        screen.blit(rotated_text, rotated_text_rect)
        screen.blit(text_prompt_restart, text_prompt_restart_rect)
        screen.blit(text_prompt_quit, text_prompt_quit_rect)
        
        pg.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

def game_over():
    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
    font = pg.font.Font(None, 72)
    font_prompt = pg.font.Font(None, 36)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return
                elif event.key == pg.K_r:  # Restart the game if 'R' key is pressed
                    pg.quit()
                    main()  # Restart the game
                elif event.key == pg.K_q:  # Quit the game if 'Q' key is pressed
                    pg.quit()
                    return

        screen.fill((255, 255, 255))
        
        angle = 1  # Define rotation angle for the "Game Over" text
        rotated_text = pg.transform.rotate(font.render("GAME OVER", True, (255, 0, 0)), angle)
        rotated_text_rect = rotated_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        
        text_prompt_restart = font_prompt.render("Press R to Restart", True, (0, 0, 0))
        text_prompt_quit = font_prompt.render("Press Q to Quit", True, (0, 0, 0))
        
        text_prompt_restart_rect = text_prompt_restart.get_rect(left=50, top=screen.get_height() // 2 + 50)
        text_prompt_quit_rect = text_prompt_quit.get_rect(right=screen.get_width() - 50, top=screen.get_height() // 2 + 50)
        
        screen.blit(rotated_text, rotated_text_rect)
        screen.blit(text_prompt_restart, text_prompt_restart_rect)
        screen.blit(text_prompt_quit, text_prompt_quit_rect)
        
        pg.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

def draw_circle(center_x, center_y, radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        angle = 2.0 * 3.14159265358979323846 * i / num_segments
        x = center_x + radius * mm.cos(angle)
        y = center_y + radius * mm.sin(angle)
        
        glVertex2f(x, y)
    glEnd()

def congratulations_menu():
    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
    font = pg.font.Font(None, 72)
    font_prompt = pg.font.Font(None, 36)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return
                elif event.key == pg.K_r:  # Restart the game if 'R' key is pressed
                    pg.quit()
                    main()  # Restart the game
                elif event.key == pg.K_q:  # Quit the game if 'Q' key is pressed
                    pg.quit()
                    return

        screen.fill((255, 255, 255))
        
        angle = 1  # Define rotation angle for the "Congratulations" text
        rotated_text = pg.transform.rotate(font.render("Congratulations! You Won!", True, (0, 255, 0)), angle)
        rotated_text_rect = rotated_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        
        text_prompt_restart = font_prompt.render("Press R to Restart", True, (0, 0, 0))
        text_prompt_quit = font_prompt.render("Press Q to Quit", True, (0, 0, 0))
        
        text_prompt_restart_rect = text_prompt_restart.get_rect(left=50, top=screen.get_height() // 2 + 50)
        text_prompt_quit_rect = text_prompt_quit.get_rect(right=screen.get_width() - 50, top=screen.get_height() // 2 + 50)
        
        screen.blit(rotated_text, rotated_text_rect)
        screen.blit(text_prompt_restart, text_prompt_restart_rect)
        screen.blit(text_prompt_quit, text_prompt_quit_rect)
        
        pg.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

def DrawLine(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_enemy(x, y):
    glColor3f(1, 1, 1)
    DrawRectangle(x+0.07,y+0.1,x-0.07,y-0.1) #legs
    glColor3f(0.5,0.5, 0.5)
    DrawRectangle(x+0.07,y+0.3,x-0.07,y+0.1) #stomach
    glColor3f(0,0, 0)
    DrawRectangle(x+0.1,y+0.3,x+0.07,y+0.1) # right arms
    glColor3f(0,0, 0)
    DrawRectangle(x-0.1,y+0.3,x-0.07,y+0.1) # left arm arms
    glColor3f(0.8235,0.7058, 0.5490)
    draw_circle(x,y+0.35,0.06,180)
    glColor3f(0,0,0)
    DrawLine(x,y+0.05,x,y-0.1)
    
def draw_character(x, y):
    glColor3f(0, 0, 1)
    DrawRectangle(x+0.07,y+0.1,x-0.07,y-0.1) #legs
    glColor3f(1,0, 0)
    DrawRectangle(x+0.07,y+0.3,x-0.07,y+0.1) #stomach
    glColor3f(1,1, 0)
    DrawRectangle(x+0.1,y+0.3,x+0.07,y+0.1) # right arms
    glColor3f(1,1, 0)
    DrawRectangle(x-0.1,y+0.3,x-0.07,y+0.1) # left arm arms
    glColor3f(0.8235,0.7058, 0.5490)
    draw_circle(x,y+0.35,0.06,180)
    glColor3f(0,0,0)
    DrawLine(x,y+0.05,x,y-0.1)

def DrawRectangle(x1, y1, x2, y2):
    glBegin(GL_QUADS)
    
    glVertex2f(x1, y1)
    glVertex2f(x1, y2)
    glVertex2f(x2, y2)
    glVertex2f(x2, y1)
    glEnd()

def DrawLine(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def DrawTriangle(x1, y1, x2, y2, x3, y3, color=(1, 1, 1)):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def draw_semi_circle(radius, segments, x_offset, y_offset,angle):
    glBegin(GL_TRIANGLE_FAN)
      
    glVertex2f(x_offset, y_offset)
    for i in range(segments + 1):
        theta = i * pi / segments +angle
        x = radius * cos(theta) + x_offset  
        y = -radius * sin(theta) + y_offset  
        glVertex2f(x, y)
    glEnd()

def draw_cloud(x, y):
    """ Helper function to draw a cloud at a given x, y position """
    draw_circle(x, y, 0.2, 360)
    draw_circle(x - 0.3, y, 0.2, 360)
    draw_circle(x - 0.6, y, 0.2, 360)
    draw_circle(x - 0.45, y - 0.1, 0.2, 360)
    draw_circle(x - 0.15, y - 0.1, 0.2, 360)
    draw_circle(x - 0.45, y + 0.1, 0.2, 360)
    draw_circle(x - 0.15, y + 0.1, 0.2, 360)

def Drawquiz():
    #x axis y axis that helps only 
    glColor3f(0, 0, 0)
    DrawLine(3,0,-3,0)
    DrawLine(0,3,0,-3)

    # Draw the code

    #draw sun

    glColor3f(1, 1, 0.8235)
    draw_circle(-1.7, 1.7,0.3, 360)

    
    
    

    #draw the ground

    glColor3f(0.62745, 0.353, 0.1725)
    DrawRectangle(4, -1.7, -4, -3) #loon el teina 2b2a hato men google b3den 
    glColor3f(0.3725,0.5490,0.15686)
    DrawRectangle(4, -1.6, -4, -1.7) #loon akhdar zar3  

    #draw thw mountains 

    DrawTriangle(-1, -1.6, 1.25,-0.1, 3.5, -1.6, color=(0.1, 0.25, 0.41))
    DrawTriangle(-1, -1.6, 1.25,-0.1, 1, -1.6, color=(0.29, 0.4078, 0.5294))

    DrawTriangle(-1, -1.6,2.1,-0.3, 4, -1.6, color=(0.1, 0.3, 0.5))
    DrawTriangle(-1, -1.6,2.1,-0.3, 1.85, -1.6, color=(0.4470, 0.5451, 0.6549))
    DrawTriangle(2.03, -0.7,2.1,-0.3, 2.55, -0.6, color=(1, 1, 1))
    DrawTriangle(1.6, -0.5,2.1,-0.3, 2.03, -0.7, color=(0.9411, 0.9725, 0.996))
    
    DrawTriangle(-3, -1.6, 0,0.2, 3, -1.6, color=(0.114, 0.282, 0.446))
    DrawTriangle(-3, -1.6, 0,0.2, -0.25, -1.6, color=(0.29, 0.4078, 0.5294))
    DrawTriangle(-0.68, -0.2, 0,0.2, -0.1, -0.5, color=(0.9411, 0.9725, 0.996)) 
    DrawTriangle(-0.1, -0.5, 0,0.2,0.68 , -0.2, color=(1, 1, 1)) 

    DrawTriangle(-3, -1.6, -1.5,-0.1, 0, -1.6, color=(0.1, 0.3, 0.5))
    DrawTriangle(-3, -1.6, -1.5,-0.1, -1.75, -1.6, color=(0.4470, 0.5451, 0.6549))
    DrawTriangle(-1.9, -0.5, -1.5,-0.1, -1.6, -0.75, color=(0.9411, 0.9725, 0.996))
    DrawTriangle(-1.6, -0.75, -1.5,-0.1, -1.1, -0.5, color=(1, 1, 1))

    #draw upsteps
     
    glColor3f(0.2627, 0.1764, 0.1255)
    DrawRectangle(1.7, -1 , 0.5, -1.2)
    glColor3f(0.2510, 0.4823, 0.1803)
    DrawRectangle(1.75, -0.9 , 0.45, -1)

    glColor3f(0.2627, 0.1764, 0.1255)
    DrawRectangle(0, -0.5 , -1.3, -0.7)
    glColor3f(0.2510, 0.4823, 0.1803)
    DrawRectangle(0.05,-0.4,-1.35,-0.5)

    glColor3f(0.2627, 0.1764, 0.1255)
    DrawRectangle(1.8, 0 , 0.6, -0.2)
    glColor3f(0.2510, 0.4823, 0.1803)
    DrawRectangle(1.85, 0.1 , 0.55, 0)

    glColor3f(0.2627, 0.1764, 0.1255)
    DrawRectangle(2.5, 0.7 , 1.3, 0.5)
    glColor3f(0.2510, 0.4823, 0.1803)
    DrawRectangle(2.55, 0.8 , 1.25, 0.7)

    glColor3f(0.2627, 0.1764, 0.1255)
    DrawRectangle(0.7, 1.4 , -1.2, 1.2)
    glColor3f(0.2510, 0.4823, 0.1803)
    DrawRectangle(0.75, 1.5 , -1.25, 1.4)

    

    #draw house of start

    glColor3f(0.8745,0.6156,0.1607) 
    DrawRectangle(-1.6,-1,-2.4,-1.6) 
    glColor3f(0.6784, 0.4196, 0.1960) 
    DrawRectangle(-1.6,-1.2,-2.4,-1.4) 
    glColor3f(0.0470,0.7921,0.9686) 
    DrawRectangle(-2.1,-1.2,-2.3,-1.4) 
    glColor3f(0.43137, 0.2941, 0.13333)
    DrawRectangle(-1.7,-1.2,-1.9,-1.6) 
    DrawTriangle(-2.5, -1, -2,-0.6, -1.5, -1, color=(0.43137, 0.2941, 0.13333))

    #draw the winning area
    
    glColor3f(1, 0, 0)
    DrawRectangle(-0.5, 1.6 , -1.2, 1.5)
   
def draw_lives(x, y, num_lives):
    """Draws life indicators as circles on the screen."""
    for i in range(num_lives):
        glColor3f(1, 0, 0)  # Red color for lives
        draw_circle(x + i* 0.2, y, 0.05, 20)  # Draw individual life circle
        draw_circle((x + i* 0.2)+0.07, y, 0.05, 20)  # Draw individual life circle
        DrawTriangle((x + i* 0.2)-0.06,y,  (x + i* 0.2)+0.04,y-0.1, (x + i* 0.2)+0.125, y ,color=(1, 0, 0) )
         # Draw individual life circle
        # DrawRectangle((x + i* 0.2)+0.03 , y+0.03, (x + i* 0.2)-0.03 , y-0.03)
        # DrawRectangle((x + i* 0.2)+0.06 , y+0.07, (x + i* 0.2)-0.06 , y+0.03)
        # DrawRectangle((x + i* 0.2)+0.09 , y+0.11, (x + i* 0.2)-0.09 , y+0.07)
        # DrawRectangle((x + i* 0.2)+0.11 , y+0.16, (x + i* 0.2)-0.11 , y+0.11)

def main():
    start_menu()

    global cloud_angle  # Access the global variable
    pg.init()

    #SOUNDS
    try:   
        pg.mixer.music.load(r"D:\AAST\old semesters\semester 8\done\COMPUTER GRAPHICS\lab\final final project\Forest Frenzy.wav")
 
        pg.mixer.music.play()
    except pg.error:
        print("Failed to load sound file.")
    #end of wallpaper music 
    try:
        jump_sound = pg.mixer.Sound(r"D:\AAST\old semesters\semester 8\done\COMPUTER GRAPHICS\lab\final final project\yallabena.wav")
    except pg.error:
        print("Failed to load jump sound file.")
        jump_sound = None

    #END OF SOUNDS

    display=(1000, 800)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]),0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)



    cloud_angle = 0
    x_position = -1.8
    y_position = -1.4
    velocity_y = 0
    gravity = -0.0017

    # Define winning area
    win_area_left = -1.2
    win_area_right = -0.5
    win_area_top = 1.6
    win_area_bottom = 1.5
    
    enemy_x = 1.3
    enemy_y = 0.9  # Enemy starts on a specific BETA3T EL Y AXIS
    enemy_direction = 1
    enemy_speed = 0.005
    trials = 3  # Initializing the trials counter
    #draw the behind steps that interact with the shape
    steps = [(0.5, 1.7, -0.8),(-1.3, 0, -0.3),(0.6, 1.8, 0.2),(1.3, 2.5, 0.9),(-1.2, 0.7, 1.6)]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # Check if character is within the winning area
        if win_area_left <= x_position <= win_area_right and win_area_bottom <= y_position <= win_area_top:
            print("Congratulations! You've won the game!")

            congratulations_menu()
            return

         # Update enemy position
        enemy_x += enemy_direction * enemy_speed
        if enemy_x > 2.5 or enemy_x < 1.3:
            enemy_direction *= -1  # Change direction at boundaries



        # Check for collision with enemy
        if abs(x_position - enemy_x) < 0.2 and abs(y_position - enemy_y) < 0.2:
            trials -= 1  # Decrement the trials counter on collision
            if trials <= 0:
                print("Game Over")
                game_over()
                return
            else:
                print(f"Collision detected. {trials} trials remaining.")
                x_position = -1.8  # Reset the character's position after collision
                y_position =-1.3

        # Update rotation angle for cloud
        cloud_angle += 0.004  # Adjust the rotation speed as needed        

        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            x_position += 0.02
        if keys[pg.K_LEFT]:
            x_position -= 0.02

        # Check if the character is on the ground or on a step
        on_ground = y_position == -1.5
        for (x1, x2, y) in steps:
            if x1 <= x_position <= x2 and y_position <= y:
                if y_position > y - 0.1:  # Check if within descent range to land on the step
                    y_position = y
                    velocity_y = 0
                    on_ground = True
                    break

        if keys[pg.K_UP] and on_ground and jump_sound:
            velocity_y = 0.05# jump speed
            jump_sound.play() 

        # Apply gravity and update character position
        velocity_y += gravity
        y_position += velocity_y

        # Prevent falling below the ground
        if y_position < -1.5:
            y_position = -1.5
            velocity_y = 0        
        

        glClearColor(0.678, 0.847, 0.902,0)  # Baby blue color
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Drawquiz()
        draw_character(x_position, y_position)
        draw_enemy(enemy_x, enemy_y)
        draw_lives(-1.9, 1.7, trials)  # Draw lives at the top left corner
        pg.display.flip()
        pg.time.wait(10)
   
    pg.quit()
    
main()