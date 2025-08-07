from manim import *
from zadani import TITLE, MAIN_EQ, STEPS, FINAL_RESULT

main_color = BLUE

def split_long_formula(formula, max_terms=3):
    import re
    parts = re.split(r'(?=[+-])', formula)
    return ["".join(parts[i:i+max_terms]) for i in range(0, len(parts), max_terms)]

class IntegralScene(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(9)
        self.camera.frame.set_height(16)

        title = Text(TITLE, gradient=(main_color, PURPLE)).scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        eq = MathTex(MAIN_EQ).scale(0.9)
        eq.next_to(title, DOWN, buff=1)
        self.play(Write(eq))
        self.wait(1)

        for step in STEPS:
            self.play(self.camera.frame.animate.move_to(eq), run_time=0.8)
            step_tex = MathTex(step).scale(0.8)
            step_tex.next_to(eq, DOWN, buff=0.7)

            if step_tex.width > 8:
                formulas = split_long_formula(step)
                prev = eq
                for part in formulas:
                    part_tex = MathTex(part).scale(0.7)
                    part_tex.next_to(prev, DOWN, buff=0.3)
                    self.play(Write(part_tex))
                    prev = part_tex
                eq = prev
            else:
                self.play(Write(step_tex))
                eq = step_tex

            self.wait(0.5)

        self.play(self.camera.frame.animate.move_to(eq), run_time=0.8)

        final_eq = MathTex(FINAL_RESULT).scale(1.0)
        final_eq.next_to(eq, DOWN, buff=0.8)
        self.play(Write(final_eq))
        self.play(self.camera.frame.animate.move_to(final_eq), run_time=0.8)
        final_box = SurroundingRectangle(final_eq, color=main_color)
        self.play(Create(final_box))
        self.wait(2)
