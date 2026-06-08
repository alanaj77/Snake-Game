from turtle import  Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SCREEN_SIZE = 300
class Snake:
    def __init__(self):
        self.segments = []
        self.create_segment()
        self.head = self.segments[0]
    def create_segment(self):
        if len(self.segments) == 0:
            for pos in STARTING_POSITIONS:
                if pos == STARTING_POSITIONS[0]:
                    new_segment = Turtle("circle")
                else:
                    new_segment = Turtle("square")
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(pos)
                self.segments.append(new_segment)
        else:
            lst_segment = len(self.segments)
            pos = self.segments[lst_segment - 1].pos()
            for _ in range(3):
                new_segment = Turtle("square")
                new_segment.color("white")
                new_segment.penup()
                new_segment.goto(pos)
                self.segments.append(new_segment)



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            return  None
        self.head.setheading(90)
        return None


    def left(self):
        if self.head.heading() == 90 or  self.head.heading() == 270:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)
    def down(self):
        if self.head.heading() ==  90:
            return None
        self.head.setheading(270)
        return None
    def position_of_snake(self):
        return self.head.pos()
    def is_collided(self):
        for seg in self.segments:
            if seg.distance(self.head) < 20:
                return  True
            else:
                return False
        return None