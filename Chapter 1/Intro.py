from manim import *

class ProbabilityConcepts(Scene):
    def construct(self):
        # Sample space
        sample_space_rect = Rectangle(width=6, height=4, color=TEAL)
        sample_space_label = Text("Sample space", font_size=24, color=TEAL).next_to(sample_space_rect, DOWN)
        sample_space_label.shift(LEFT*2)  # Adjust this value as needed

        # Add sample space and its label to the scene
        self.play(AnimationGroup(Create(sample_space_rect), FadeIn(sample_space_label), lag_ratio=0.5))
        self.wait(3)

        # Outcomes
        outcome_positions = [
            (-2.2, 0.5-.7, 0), (-1.7, 0.7-.7, 0), (-2, 0.2-.7, 0),  
            (0.5, 1.2-.5, 0), (0.7, 1-.5, 0), (0.2, 1.5-.5, 0),  
            (2.2, 0.5-1, 0), (1.7, 0.7-1, 0), (2, 0.2-1, 0)  
        ]
        outcomes = [Dot(point=pos, color=MAROON) for pos in outcome_positions]
        outcomes_group = VGroup(*outcomes)
        outcome_label = Text("Outcome", font_size=24, color=MAROON).next_to(sample_space_rect, DOWN)
        #outcome_label.shift(RIGHT*2)

        # Animate outcomes synchronously
        self.play(AnimationGroup(FadeIn(outcomes_group), FadeIn(outcome_label), lag_ratio=0.5))

        # Example of synchronous animation: all dots move up and then back down
        self.play(outcomes_group.animate.shift(UP * 0.1))
        self.play(outcomes_group.animate.shift(DOWN * 0.1))
        self.wait(5)

        # Events
        event1 = Ellipse(width=2, height=1.5, color=BLUE).shift(LEFT*1.7)
        event2 = Ellipse(width=2, height=1.5, color=BLUE).shift(RIGHT*0.5 + UP*0.7)
        event3 = Ellipse(width=2, height=1.5, color=BLUE).shift(RIGHT*1.7 + DOWN*0.7)
        event_label = Text("Event", font_size=24, color=BLUE).next_to(sample_space_rect, DOWN)
        event_label.shift(RIGHT*2)

        self.play(AnimationGroup(Create(event1), Create(event2), Create(event3), FadeIn(event_label), lag_ratio=0.5))

        self.wait(2)