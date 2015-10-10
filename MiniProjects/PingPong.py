# Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

score1=0
score2=0
ball_vel=[]
ball_pos=[]
paddle1_vel=0
paddle2_vel=0
paddle1_pos=HEIGHT/3
paddle2_pos=HEIGHT/3

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2 - 1, HEIGHT / 2 - 1]
    if direction == LEFT:
        ball_vel = [random.randrange(120, 240) / 50, -random.randrange(60, 180) / 50]
    elif direction == RIGHT:
        ball_vel = [-random.randrange(120, 240) / 50, -random.randrange(60, 180) / 50]

 # define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    #spawn_ball(direction=[2,-1])
    score1 = score2 = 0
    spawn_ball(RIGHT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global RIGHT, LEFT
    ball_pos[0] += ball_vel[0]


    ball_pos[1] += ball_vel[1]
    if ball_pos[1] > HEIGHT -BALL_RADIUS or ball_pos[1]<= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle( [ball_pos[0], ball_pos[1]] , BALL_RADIUS, 3, "WHITE", "WHITE")
    # update ball

    # draw ball

    # update paddle's vertical position, keep paddle on the screen


    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel

    if paddle1_pos < 1:
        paddle1_pos = 0
    if paddle2_pos < 0:
        paddle2_pos = 0
    if paddle1_pos > HEIGHT - (PAD_HEIGHT ):
        paddle1_pos = HEIGHT - (PAD_HEIGHT )
    if paddle2_pos > HEIGHT - (PAD_HEIGHT ):
        paddle2_pos = HEIGHT - (PAD_HEIGHT)

    # draw paddles
    canvas.draw_line([0, paddle1_pos],[0, paddle1_pos+80], 16, "White")
    canvas.draw_line([WIDTH, paddle2_pos],[WIDTH, paddle2_pos+80], 16, "White")


    # determine whether paddle and ball collide
    if ball_pos[0]+ BALL_RADIUS >= WIDTH-PAD_WIDTH and(ball_pos[1]>=paddle2_pos and ball_pos[1]<=paddle2_pos+PAD_HEIGHT):

        ball_vel[0] *= -1.1
    elif ball_pos[0] + BALL_RADIUS > WIDTH-PAD_WIDTH:
        score1+=1
        RIGHT = False
        LEFT = True
        spawn_ball(RIGHT)




    if ball_pos[0]- BALL_RADIUS <= PAD_WIDTH and(ball_pos[1]>=paddle1_pos and ball_pos[1]<=paddle1_pos + PAD_HEIGHT ):

        ball_vel[0] *= -1.1

    elif ball_pos[0]- BALL_RADIUS < PAD_WIDTH:
        score2+=1
        RIGHT = True
        LEFT = False
        spawn_ball(LEFT)
        

    # draw scores
    canvas.draw_text(str(score1), [250,80], 45, "WHITE")
    canvas.draw_text(str(score2), [350,80], 45, "WHITE")

def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel=-8
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel=8



    if key == simplegui.KEY_MAP['w']:
        paddle1_vel=-8

    elif key == simplegui.KEY_MAP['s']and paddle1_pos<=HEIGHT:
        paddle1_vel=8

def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel=0

    elif key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel=0



def restart():
    new_game()
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", restart , 100)


# start frame
new_game()
frame.start()
