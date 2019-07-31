import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 8
TIME_STEP = 150

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake

snake = turtle.clone()
snake.shape("circle")
#snake.setup(400,250)
#snake.bgpic("space.gif")

snake.color("black")
turtle.bgcolor("yellow")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    some_thing = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(some_thing)
    #Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(0,START_LENGTH):
    x_pos=snake.xcor() #Get x-position with snake.pos()[0]
    y_pos=snake.ycor() 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

     #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    snake.goto(x_pos,y_pos)
    new_stamp()
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position
snake.direction = "Up"
#here yaahhh
UP_EDGE = 250
def up():
    snake.direction="Up" #Change direction to up
    
    print("You pressed the up key!")


#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, "Up") # Create listener for up key

DOWN_EDGE = -250
def Down():
    snake.direction="Down"
 
    
    print("you pressed the down key")
turtle.onkeypress(Down, "Down")

RIGHT_EDGE = 400
def Right():
    snake.direction="Right"
      
    print("you pressed the Right key")
turtle.onkeypress(Right, "Right")
LEFT_EDGE = -400
def Left():
    snake.direction="Left"
    print("you pressed the Left key")
turtle.onkeypress(Left, "Left")

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()
turtle.register_shape("burger.gif") 

food = turtle.clone()
food.shape("burger.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos :
    food.goto(this_food_pos)
   
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)
    food.hideturtle()
    
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
      #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    rand_food_stamp=food.stamp()
    food_pos.append((food_x,food_y))
    food_stamps.append(rand_food_stamp)

    

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
     #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos <= LEFT_EDGE:
         print("You hit the Left edge! Game over!")
         quit()

    elif new_y_pos >= UP_EDGE:
         print("You hit the Up edge! Game over!")
         quit()

    elif new_y_pos <= DOWN_EDGE:
         print("You hit the Down edge! Game over!")
         quit()
   


    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE
        
    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved Right!")
    elif snake.direction=="Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        
    if len(food_stamps) <= 6 :
                make_food()

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
   

    ######## SPECIAL PLACE - Remember it for Part 5
    
    #If snake is on top of food item

    
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        new_stamp()
        
        

    for lee in pos_list[1:-1]:
        if snake.pos() == lee:
            print("game over")
            
            quit()
                  

    #remove the last piece of the snake (Hint Functions are FUN!)
    new_stamp()
    remove_tail()
    turtle.ontimer(move_snake,TIME_STEP) #<--Last line of function
move_snake()


    #If snake is on top of food item



    
    
    
turtle.mainloop()
    
