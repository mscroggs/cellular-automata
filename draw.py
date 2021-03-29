from automaton import Automaton

a = Automaton(102)
a.generate(400)

print(a.data)

a.save_image()
