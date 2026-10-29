from manim import *

class DefaultAddScene(Scene):
    def construct(self):
        text_1 = Text("Ramram samsam")
        text_2 = Text("Chona rema")
        text_3 = Text("Man'dikatsranga ang' janggi tangao")
        texts = VGroup(text_1, text_2, text_3).arrange(DOWN)
        rect = SurroundingRectangle(texts, buff=0.5)

        self.play(
            Create(rect, run_time=3.0),
            Succession(
                Wait(1.0),
                # You can Add a Mobject in the middle of an animation...
                Add(text_1),
                Wait(1.0),
                # ...or multiple Mobjects at once!
                Add(text_2),
                Wait(1.0),
                Add(text_3)
            ),
        )
        self.wait()