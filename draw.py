"""Example script that creates an image of 400 lines of rule 102."""

from automaton import Automaton

a = Automaton(102)
a.generate(400)

a.save_image("rule102.svg")
