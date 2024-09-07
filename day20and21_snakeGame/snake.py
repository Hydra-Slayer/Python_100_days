from turtle import Turtle
STARTING_POSITIONS = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake():
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def get_len(self):
        return len(self.segments)
    
    #adds length to the snake when food is eaten
    def add_len(self):
        new_part=Turtle()
        new_part.shape("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(self.segments[-1].pos())
        self.segments.append(new_part)   
        
    #initalise the whole snake body
    def create_snake(self):
        
        for pos in STARTING_POSITIONS:
        
            obj=Turtle()
            obj.shape("square")
            obj.color("white")
            obj.penup()
            obj.goto(pos)
            self.segments.append(obj)
    
    #detect collision with tail function
    def is_tailbite(self):
        
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        
        return False    
    
    #default move forward
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.head.forward(MOVE_DISTANCE)
    
    #move set
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        else:
            pass
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        else:
            pass
    def up(self):
        if self.head.heading() != DOWN:    
            self.head.setheading(90)
        else:
            pass
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        else:
            pass