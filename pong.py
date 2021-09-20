from ursina import *
import time

def update():
    ball.position += ball.right * ball.speed * time.dt

    if paddle1.y != ball.y:
        if paddle1.y > ball.y:
                paddle1.y -= 0.05
        if paddle1.y < ball.y:
                paddle1.y += 0.05
                


    if held_keys['w']: 
        paddle1.y += time.dt * 5
    
    if held_keys['s']: 
        paddle1.y -= time.dt * 5

    if paddle1.y > 4.5:
        paddle1.y -= 0.1

    if paddle1.y < -4.5:
        paddle1.y += 0.1


    if held_keys['up arrow']: 
        paddle2.y += time.dt * 5
    
    if held_keys['down arrow']: 
        paddle2.y -= time.dt * 5

    if paddle2.y > 4.5:
        paddle2.y -= 0.1

    if paddle2.y < -4.5:
        paddle2.y += 0.1

    if ball.y > 5.2 or ball.y < -5.2 :
        ball.rotation_z = -ball.rotation_z

    hit_info = paddle2.intersects()
    if hit_info.hit:
        if hit_info.entity == ball:
            ball.rotation_z = ball.rotation_z + 90
            ball.speed += 2

    hit_info = paddle1.intersects()
    if hit_info.hit:
        if hit_info.entity == ball:
            ball.rotation_z = ball.rotation_z + 90
            ball.speed += 1

    if ball.x > 6.9:
        Text.size = 0.07
        Text.default_resolution = 1080 * Text.size
        died = Text(text="Left Won!")
        died.background = True
        died.color = color.white
        died.y = 0.05
        died.x = -0.15

    if ball.x < -6.9:
        Text.size = 0.05
        Text.default_resolution = 1080 * Text.size
        died = Text(text="Right Won!")
        died.background = True
        died.color = color.white
        died.y = 0.05
        died.x = -0.15


app = Ursina()

paddle1 = Entity(model='quad', color=color.white, scale=(0.2,1.4), collider = "box") 
paddle1.x = -6.5

paddle2 = Entity(model='quad', color=color.white, scale=(0.2,1.4), collider = "box") 
paddle2.x = 6.5

ball = Entity(model='sphere', color=color.white, scale=(0.2,0.2,0.2), collider = "box", speed=15) 


window.windowed_size = 0.3
window.update_aspect_ratio()
window.late_init()

window.color = color.black
ball.rotation_z= -50


app.run()
