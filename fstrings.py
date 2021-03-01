#!/usr/bin/env python
b = '"""'
g = """#!/usr/bin/env python
b = '{b}'
g = {b}{g}{b}
print(g.format(g=g, b=b))
"""
print(g.format(g=g, b=b))

