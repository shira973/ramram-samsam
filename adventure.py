from manim import *

class SideScrollingAdventure(MovingCameraScene):
    def construct(self):
        # ----------------------------------------------------
        # 1. SETUP THE SCENERY (Laid out horizontally)
        # ----------------------------------------------------
        
        # SCENE 1: The Sky Blue Forest (centered at X = 0)
        bg1 = Rectangle(width=8, height=6, fill_color="#87CEEB", fill_opacity=1).shift(RIGHT * 0)
        ground1 = Line(LEFT*4, RIGHT*4, color=GREEN_E, stroke_width=8).next_to(bg1, DOWN, buff=0)
        tree = Triangle(color=GREEN).scale(0.8).move_to(bg1.get_bottom() + UP * 0.8)
        scene1 = VGroup(bg1, ground1, tree)

        # SCENE 2: The Sunset Desert (centered at X = 8) - FIXED TYPO HERE
        bg2 = Rectangle(width=8, height=6, fill_color=ORANGE, fill_opacity=0.6).shift(RIGHT * 8)
        ground2 = Line(LEFT*4, RIGHT*4, color=GOLD_E, stroke_width=8).next_to(bg2, DOWN, buff=0)
        cactus = VGroup(
            Rectangle(width=0.3, height=1.2, fill_color=GREEN_D, fill_opacity=1),
            Square(side_length=0.4, fill_color=GREEN_D, fill_opacity=1).shift(UP*0.2 + RIGHT*0.2)
        ).move_to(bg2.get_bottom() + UP * 0.6)
        scene2 = VGroup(bg2, ground2, cactus)

        # SCENE 3: The Dark Night City (centered at X = 16)
        bg3 = Rectangle(width=8, height=6, fill_color="#111122", fill_opacity=1).shift(RIGHT * 16)
        ground3 = Line(LEFT*4, RIGHT*4, color=GREY_E, stroke_width=8).next_to(bg3, DOWN, buff=0)
        building = Rectangle(width=1.5, height=3, fill_color=GREY, fill_opacity=1).move_to(bg3.get_bottom() + UP * 1.5)
        scene3 = VGroup(bg3, ground3, building)

        # Render all environment assets on screen simultaneously
        self.add(scene1, scene2, scene3)

        # ----------------------------------------------------
        # 2. CREATE THE CHARACTER
        # ----------------------------------------------------
        body = Circle(radius=0.3, color=YELLOW, fill_color=YELLOW, fill_opacity=1)
        eye1 = Dot(color=BLACK).scale(0.8).move_to(body.get_center() + UP*0.1 + RIGHT*0.1)
        eye2 = Dot(color=BLACK).scale(0.8).move_to(body.get_center() + UP*0.1 + RIGHT*0.25)
        mouth = ArcBetweenPoints(start=body.get_center() + DOWN*0.1 + LEFT*0.05, end=body.get_center() + DOWN*0.1 + RIGHT*0.05, angle=-PI/6, color=BLACK)
        character = VGroup(body, eye1, eye2, mouth)
        
        # Start character on the left edge of Scene 1
        character.move_to(bg1.get_left() + RIGHT * 0.8 + UP * 0.3)
        self.add(character)

        # ----------------------------------------------------
        # 3. ANIMATION: CAMERA TRACKING & CHARACTER MOVEMENT
        # ----------------------------------------------------
        
        # Frame 1: Walk across Scene 1
        self.play(
            character.animate.shift(RIGHT * 4), 
            run_time=2, 
            rate_func=linear
        )
        
        # Frame 2: Move into Scene 2 (Camera pans right alongside the character)
        self.play(
            character.animate.shift(RIGHT * 8),
            self.camera.frame.animate.shift(RIGHT * 8),
            run_time=4,
            rate_func=linear
        )
        
        # Frame 3: Move into Scene 3 (Camera tracks right again)
        self.play(
            character.animate.shift(RIGHT * 8),
            self.camera.frame.animate.shift(RIGHT * 8),
            run_time=4,
            rate_func=linear
        )
        
        self.wait(1)
