#!/usr/bin/env python
"""
Demonstrate how to plot lists of parts
"""

import parasbolv as psv
import matplotlib.pyplot as plt
from collections import namedtuple

#Basic data type to hold the parts
part_list = []
Part = namedtuple('part', ['glyph_type', 'orientation',  'user_parameters', 'style_parameters'])

part_list.append(Part('CDS',
                      'forward',
                      None,
                      {'cds': {'facecolor': (0.5,0.5,0.5),
                               'edgecolor': (1,0,0),
                               'linewidth': 2}}))
part_list.append(Part('CDS',
                      'forward',
                      {'height':25, 'arrowbody_height':25, 'width':40},
                      {'cds': {'facecolor': (1,1,1),
                               'edgecolor': (0,0,1),
                               'linewidth': 2}}))
part_list.append(Part('Promoter',
                      'forward',
                      None,
                      None))
part_list.append(Part('CDS',
                      'forward',
                      None,
                      None))
part_list.append(Part('CDS',
                      'reverse',
                      {'orientation':'reverse'},
                      None))
part_list.append(Part('CDS',
                      'forward',
                      {'orientation':'reverse'},
                      None))

# Create renderer
renderer = psv.GlyphRenderer()

# Draw construct
construct = psv.Construct(part_list, renderer)
fig, ax, baseline_start, baseline_end, bounds = construct.draw()
ax.plot([baseline_start[0], baseline_end[0]], [baseline_start[1], baseline_end[1]], color=(0,0,0), linewidth=1.5, zorder=0)

plt.show()
