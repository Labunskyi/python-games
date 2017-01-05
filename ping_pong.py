# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
# make first paddle
PAD_pos = [4, 160] 
PAD_pos1 = [4, 240] 
# make second paddle
PAD2_pos = [596, 160] 
PAD2_pos1 = [596, 240]  
# common peddles velocity
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, vel, PAD_pos, PAD_pos1, PAD2_pos, PAD2_pos1         
    if direction == True:
        PAD_pos = [4, 160] 
        PAD_pos1 = [4, 240]
        PAD2_pos = [596, 160] 
        PAD2_pos1 = [596, 240] 
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        vel = [-random.randrange(2, 4), -random.randrange(1, 3)]
    
    if direction == False:
        PAD_pos = [4, 160] 
        PAD_pos1 = [4, 240]
        PAD2_pos = [596, 160] 
        PAD2_pos1 = [596, 240]   
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        vel = [random.randrange(2, 4), -random.randrange(1, 3)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
      
spawn_ball(True)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # first paddle    
    PAD_pos[0] += paddle1_vel[0]
    PAD_pos[1] += paddle1_vel[1]
    PAD_pos1[0] += paddle1_vel[0]
    PAD_pos1[1] += paddle1_vel[1]
    # second paddle
    PAD2_pos[0] += paddle2_vel[0]
    PAD2_pos[1] += paddle2_vel[1]
    PAD2_pos1[0] += paddle2_vel[0]
    PAD2_pos1[1] += paddle2_vel[1]
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    if ball_pos[1] > HEIGHT - BALL_RADIUS:
        vel[1] = - vel[1]        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    # first paddle
    if PAD_pos[1] <= 0:
        paddle1_vel[1] = 0
    if PAD_pos[1] == HEIGHT - PAD_HEIGHT:
        paddle1_vel[1] = 0
    # second paddle    
    if PAD2_pos[1] <= 0:
        paddle2_vel[1] = 0
    if PAD2_pos[1] == HEIGHT - PAD_HEIGHT:
        paddle2_vel[1] = 0    
    # draw paddles
    canvas.draw_line(PAD_pos, PAD_pos1, PAD_WIDTH, "White")
    canvas.draw_line(PAD2_pos, PAD2_pos1, PAD_WIDTH, "White")

    # determine whether paddle and ball collide    
    # left paddle
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if (PAD_pos[1] <= ball_pos[1] <= PAD_pos1[1]):
            vel[0] = - vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball(False)
    # right paddle    
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if (PAD2_pos[1] <= ball_pos[1] <= PAD2_pos1[1] ):
            vel[0] = - vel[0] * 1.1
        else:
            score1 += 1
            spawn_ball(True)
    
    # draw scores
    canvas.draw_text(str(score1) + '/' + str(score2), (350,30), 30, "green")
    

def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acc
        
      
    acc = 5
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle_vel 
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    
def reset():
    global score1, score2
    score1 = 0
    score2 = 0
    spawn_ball(True)
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", reset, 100)

# start frame
new_game()
frame.start()