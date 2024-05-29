from manim import *
class Subtree(VGroup):
    def __init__(self, meal, sides, drinks, meal_color=RED, side_color=BLUE, drink_color=GREEN, **kwargs):
        super().__init__(**kwargs)

        # Meal text
        meal_text = Text(meal, color=meal_color, font_size=48)
        self.add(meal_text)

        side_texts = []
        for j, side in enumerate(sides):
            side_text = Text(side, color=side_color, font_size=36)
            side_texts.append(side_text)

        # Align side texts vertically
        side_texts_group = VGroup(*side_texts).arrange(DOWN, buff=1)

        # Position side texts group to the right of meal text 
        side_texts_group.next_to(meal_text, RIGHT*1.0, buff=2.0)

        for j, side_text in enumerate(side_texts_group):
            arrow = Arrow(meal_text.get_right(), side_text.get_left(), color=side_color, buff=0.1, stroke_width=5, tip_length=0.4)
            self.add(arrow, side_text)

            drink_texts = []
            for k, drink in enumerate(drinks):
                drink_text = Text(drink, color=drink_color, font_size=24)
                drink_texts.append(drink_text)

            # Align drink texts vertically
            drink_texts_group = VGroup(*drink_texts).arrange(DOWN, buff=.7)

            # Position drink texts group to the right of side text 
            drink_texts_group.next_to(side_text, RIGHT*1.0, buff=2)

            for k, drink_text in enumerate(drink_texts_group):
                arrow2 = Arrow(side_text.get_right(), drink_text.get_left(), color=drink_color, buff=0.1, stroke_width=5, tip_length=0.3 )
                self.add(arrow2, drink_text)

class VerticalMultiplicationPrincipleTree(Scene):
    def construct(self):
        # Title
        title = Text("Multiplication Principle").to_edge(UP)
        self.play(Write(title), run_time=1.5)

        # Meal options
        meals = ["Salad", "Burger", "Noodles"]
        sides = ["Chips", "Fries", "Fruit"]
        drinks = ["Soda", "Water"]

        # Create subtrees
        subtrees = VGroup(*[Subtree(meal, sides, drinks) for meal in meals])

        # Align subtrees horizontally
        subtrees.arrange(RIGHT, buff=1.6)

        # Shift subtrees slightly upwards
        subtrees.shift(UP*0.1).scale(0.5)

        # Draw subtrees one by one
        for subtree in subtrees:
            self.play(Write(subtree), run_time =1.5)
        
        result = Text("18 possible combinations").to_edge(DOWN)
        self.play(Write(result), run_time=1.5)
            
        # Add a pause at the end
        self.wait(2)