from automaton import Automaton

a = Automaton(102)
a.generate(400)

a.save_image("rule102.svg")
