from manim import *

class SkyBlueRectangle(Scene):
    def construct(self):
        # Define a custom sky blue hex color
        SKY_BLUE = "#87CEEB"
        
        # Create a rectangle
        rect = Rectangle(width=15.0, height=6)
        
        # Set the fill color, fill opacity (1.0 is solid), and border style
        rect.set_fill(SKY_BLUE, opacity=1.0)
        rect.set_stroke(color=WHITE, width=2)
        
        # Animate the rectangle drawing itself onto the screen
        self.play(Create(rect))
        self.wait(2)
