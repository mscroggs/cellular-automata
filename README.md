Cellular automata
=================

This repo contains code to draw svg images of cellular automata.

Example
-------
Before using this code, you should install the Python dependencies:

```bash
pip3 install -r requirements.txt
```

To make an image, first import the `Automaton` class:

```python
from automaton import Automaton
```

Next, create your automaton. For example to create an automaton using rule 102, run:

```python
a = Automaton(102)
```

You can then use the automaton to generate rows of information. For example,
you can create 400 rows by running:

```python
a.generate(400)
```

Finally, you can save the image as a SVG by running:

```python
a.save_image("rule102.svg")
```

This full example is included in the file [`draw.py`](/draw.py).
