"""
molecool
A python package for analyzing and visualizing xyz file. For MolSSI Best Practices Workshop
"""

# Add imports here
from .functions import *
from .atom_data import atom_colors, atomic_weights
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_bond_histogram, draw_molecule

import molecool.io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
