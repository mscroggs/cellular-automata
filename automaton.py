"""Creating cellular automata."""

from itertools import product


class Automaton:
    """A cellular automaton."""

    def __init__(self, rule, start=[1]):
        self.rule = rule
        self.data = [start]

        self.rule_map = {}
        for i in product([0, 1], repeat=3):
            self.rule_map[i] = rule % 2
            rule //= 2

    def generate(self, rows):
        """Generate a given number of rows."""
        while len(self.data) < rows:
            self.data.append([
                self.rule_map[self.get_recent_block(i)]
                for i in range(-1, len(self.data[-1]) + 1)
            ])

    def get_recent_block(self, n):
        """Get the three cells next to the nth cell in the most recent row."""
        return tuple(self.get_recent_value(n + i) for i in [-1, 0, 1])

    def get_recent_value(self, n):
        """Get the nth cell in the most recent row."""
        if n < 0 or n >= len(self.data[-1]):
            return 0
        return self.data[-1][n]

    def save_image(self, filename="picture.svg"):
        """Save the rows as a SVG."""
        import svgwrite

        rows = len(self.data)
        cols = len(self.data[-1])
        svg = svgwrite.Drawing(filename, size=(2 * cols, 2 * rows))

        for row, data in enumerate(self.data):
            for col, i in enumerate(data):
                if i == 1:
                    svg.add(svg.rect((cols - row * 2 + 2 * col, 2 * row), (2, 2)))
        svg.save()
