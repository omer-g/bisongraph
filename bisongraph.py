# Creates a visual svg graph of a Bison LALR(1) automata.

# Requirements:
# pip install graphviz
# pip install pydot

# Usage: 'python bisongraph.py my_parser.ypp'
# Output: 'my_parser.svg'

import pydot
import sys
import subprocess

bison_file = sys.argv[1]
subprocess.call(["bison", "--graph", bison_file])
graphs = pydot.graph_from_dot_file(bison_file.split('.')[0] + ".dot")
graphs[0].write_svg(bison_file.split('.')[0] + ".svg")
