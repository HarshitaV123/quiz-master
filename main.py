import pgzrun

TITLE= "Are you a Quiz Master?"
WIDTH = 870
HEIGHT= 650

marquee_box=Rect(0,0,880,80)
question_box=Rect(0,0,650,150)
score_box=Rect(0,0,150,50)
timer_box=Rect(0,0,150,150)
answer1_box=Rect(0,0,300,150)
answer2_box=Rect(0,0,300,150)
answer3_box=Rect(0,0,300,150)
answer4_box=Rect(0,0,300,150)
skip_box=Rect(0,0,150,330)

score=0
time_left=10
question_text_file="questions.txt"
marquee_text=""
game_over=False
questions=[]
answer_boxes=[answer1_box,answer2_box,answer3_box,answer4_box]
question_count=0
question_index=0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
score_box.move_ip(700,50)
timer_box.move_ip(700,100)
answer1_box.move_ip(20,270)
answer2_box.move_ip(370,270)
answer3_box.move_ip(20,450)
answer4_box.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_text
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(timer_box,"red")
    screen.draw.filled_rect(skip_box,"green")
    screen.draw.filled_rect(score_box,"blue")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"orange")

    marquee_text = "Welcome to Quiz Master."
    marquee_text = marquee_text + f"Question: {question_index} of {question_count}"

    screen.draw.textbox(marquee_text, marquee_box, color = "white")
    screen.draw.textbox(str(time_left),timer_box, color="white", shadow=(0.5,0.5),scolor="grey")
    screen.draw.textbox("skip",skip_box,color="black",angle=-90)
    screen.draw.textbox(f"score: {score}",score_box,color="white")
    screen.draw.textbox(question[0].strip(),question_box,color="white",shadow=(0.5,0.5),scolor="grey")
    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(), answer_box, color = "black")
        index = index + 1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x=marquee_box.x-1
    if marquee_box.right<0:
        marquee_box.left=WIDTH

def read_question_file():
    global questions, question_count
    q_file=open(question_text_file,"r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                is_game_over()
        index = index + 1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global question,score, time_left, questions
    score = score + 1
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        is_game_over()

def is_game_over():
    global question, game_over, time_left
    message = f"Game over!\nYou got a total of {score} right!"
    question = [message, "-","-","-","-",5]
    time_left = 0
    game_over=True

def skip_question():
    global time_left, question
    if questions and not game_over:
        question = read_next_question()
        time_left = 10
    else:
        is_game_over()

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        is_game_over()

read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left,1)




pgzrun.go()