
import simplegui

class Circle:
    def __init__(self):
        self.radius = 40
        self.center_point = (100,100)    
        
    def update_x(self, shift_x):
        self.center_point =  (
            self.center_point[0] + shift_x,
            self.center_point[1]
                )
    def update_y(self, shift_y):
        self.center_point =  (
            self.center_point[0],
            self.center_point[1] + shift_y
                )
        
class ShapeAttribute:
    def __init__(self):
        self.line_width = 2
        self.line_color = "Green"
        self.fill_color = ""

class Cliq:
    
    key_map = {
        "up": 38,
        "left": 37,
        "right": 39,
        "down": 40
        
        }
    
    def __init__(self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttribute()
        self.movement = 10
        self.moveLeft = -10
        
    def draw_me(self, canvas):
        canvas.draw_circle(
            self.circle_shape.center_point,
            self.circle_shape.radius,
            self.shape_attributes.line_width,
            self.shape_attributes.line_color,
            self.shape_attributes.fill_color
            )
        
    def move(self, key):
        if key == 39:
            self.circle_shape.update_x(self.movement)
        if key == 37:
            self.circle_shape.update_x(self.moveLeft)
        if key == 38:
            self.circle_shape.update_x(self.moveLeft)
        
        
        

cliq = Cliq()

def draw(canvas):
    cliq.draw_me(canvas)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(cliq.move)
# Start the frame animation
frame.start()
