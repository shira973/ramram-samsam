from manim import *

class TestAnimation(Scene):
    def construct(self):
        # Create a circle and a square
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        # Display them on screen
        self.play(Create(circle))
        self.wait(1)
        # Morph the circle into a square
        self.play(Transform(circle, square))
        self.wait(1)
