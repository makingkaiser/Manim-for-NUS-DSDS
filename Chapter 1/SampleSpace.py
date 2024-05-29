from manim import *

class ProbabilityConcepts(Scene):
    def construct(self):
        # Sample space
        sample_space_rect = Rectangle(width=6, height=4, color=TEAL)
        sample_space_label = Text("Sample space", font_size=24, color=TEAL).next_to(sample_space_rect, DOWN)
        sample_space_label.shift(LEFT*3.5)  # Adjust this value as needed

        # Events
        event1 = Ellipse(width=2, height=1.5, color=BLUE).shift(LEFT*1.7)
        event2 = Ellipse(width=2, height=1.5, color=BLUE).shift(RIGHT*0.5 + UP*0.7)
        event3 = Ellipse(width=2, height=1.5, color=BLUE).shift(RIGHT*1.7 + DOWN*0.7)
        event_label = Text("Event", font_size=24, color=BLUE).next_to(sample_space_rect, DOWN)

        # Outcomes
        outcome_positions = [
            (-2.2, 0.5-.7, 0), (-1.7, 0.7-.7, 0), (-2, 0.2-.7, 0),  
            (0.5, 1.2-.5, 0), (0.7, 1-.5, 0), (0.2, 1.5-.5, 0),  
            (2.2, 0.5-1, 0), (1.7, 0.7-1, 0), (2, 0.2-1, 0)  
        ]
        outcomes = [Dot(point=pos, color=MAROON) for pos in outcome_positions]
        outcomes_group = VGroup(*outcomes)
        outcome_label = Text("Outcome", font_size=24, color=MAROON).next_to(event_label)
        sample_space_label.shift(RIGHT*2)

        
        # Add all elements to the scene
        self.play(Create(sample_space_rect))
        self.play(FadeIn(sample_space_label))
        self.play(Create(event1), Create(event2), Create(event3))
        self.play(FadeIn(event_label))

        # Animate outcomes synchronously
        self.play(FadeIn(outcomes_group))
        self.play(FadeIn(outcome_label))
        
        # Example of synchronous animation: all dots move up and then back down
        self.play(outcomes_group.animate.shift(UP * 0.1))
        self.play(outcomes_group.animate.shift(DOWN * 0.1))

        self.wait(2)