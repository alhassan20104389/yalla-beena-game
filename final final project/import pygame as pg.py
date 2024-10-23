import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math as mm
from math import sin, cos, pi

def draw_circle(center_x, center_y, radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        angle = 2.0 * 3.14159265358979323846 * i / num_segments
        x = center_x + radius * mm.cos(angle)
        y = center_y + radius * mm.sin(angle)
        
        glVertex2f(x, y)
    glEnd()

def DrawLine(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_enemy(x, y):
    glColor3f(1, 1, 0)
    DrawRectangle(x+0.07,y+0.1,x-0.07,y-0.1) #legs
    glColor3f(1,0, 1)
    DrawRectangle(x+0.07,y+0.3,x-0.07,y+0.1) #stomach
    glColor3f(0,0, 1)
    DrawRectangle(x+0.1,y+0.3,x+0.07,y+0.1) # right arms
    glColor3f(0,0, 1)
    DrawRectangle(x-0.1,y+0.3,x-0.07,y+0.1) # left arm arms
    glColor3f(0.5,0.5, 0.5)
    draw_circle(x,y+0.35,0.06,180)
    glColor3f(0,0,0)
    DrawLine(x,y+0.05,x,y-0.1)
    
def draw_character(x, y):
    glColor3f(1, 1, 0)
    DrawRectangle(x+0.07,y+0.1,x-0.07,y-0.1) #legs
    glColor3f(1,0, 1)
    DrawRectangle(x+0.07,y+0.3,x-0.07,y+0.1) #stomach
    glColor3f(0,0, 1)
    DrawRectangle(x+0.1,y+0.3,x+0.07,y+0.1) # right arms
    glColor3f(0,0, 1)
    DrawRectangle(x-0.1,y+0.3,x-0.07,y+0.1) # left arm arms
    glColor3f(0.5,0.5, 0.5)
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

    # Draw the first cloud

    global cloud_angle  # Access the global variable

    glColor3f(1, 1, 1)
    cloud_x = -1.7 + 0.5 * mm.cos(cloud_angle)
    cloud_y = 1 + 0.5 * mm.sin(cloud_angle)
    draw_cloud(cloud_x, cloud_y)

    # Draw the second cloud, mirrored across the x-axis
    glColor3f(1, 1, 1)
    opposite_cloud_x = 1.7 - 0.5 * mm.cos(cloud_angle)
    opposite_cloud_y = cloud_y  # same y, mirrored x
    draw_cloud(1.7 - 0.5 * mm.cos(cloud_angle), cloud_y)

    # Draw the third cloud in the middle with its own rotation pattern
    glColor3f(1, 1, 1)
    middle_cloud_x = 0 + 0.5 * mm.cos(cloud_angle + mm.pi)  # Added phase shift
    middle_cloud_y = 1.5 + 0.5 * mm.sin(cloud_angle + mm.pi)  # Higher and with a phase shift
    draw_cloud(middle_cloud_x, middle_cloud_y)


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
    

    

    


def main():

    global cloud_angle  # Access the global variable
    pg.init()

    #SOUNDS
    # try:   
    #       pg.mixer.music.load(r"D:\AAST\semester 8\COMPUTER GRAPHICS\final final project\Forest Frenzy.wav")
 
    #       pg.mixer.music.play()
    # except pg.error:
    #       print("Failed to load sound file.")
    # # #end of wallpaper music 
    try:
        jump_sound = pg.mixer.Sound(r"D:\AAST\semester 8\COMPUTER GRAPHICS\final final project\yallabena.wav")
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
    
    enemy_x = 1.3
    enemy_y = 0.9  # Enemy starts on a specific BETA3T EL Y AXIS
    enemy_direction = 1
    enemy_speed = 0.005
    #draw the behind steps that interact with the shape
    steps = [(0.5, 1.7, -0.8),(-1.3, 0, -0.3),(0.6, 1.8, 0.2),(1.3, 2.5, 0.9),(-1.2, 0.7, 1.6)]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()



         # Update enemy position
        enemy_x += enemy_direction * enemy_speed
        if enemy_x > 2.5 or enemy_x < 1.3:
            enemy_direction *= -1  # Change direction at boundaries



        # Check for collision with enemy
        if abs(x_position - enemy_x) < 0.2 and abs(y_position - enemy_y) < 0.2:
            print("Game Over")
            pg.quit()
            quit()       

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
        
        pg.display.flip()
        pg.time.wait(10)

    pg.quit()

main()

