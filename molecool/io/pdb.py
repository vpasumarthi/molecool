"""
pdb.py

Handles the read and write of pdb files
"""

import numpy as np

def open_pdb(file_location):
    """
    This function reads in a pdb file and returns the atom names and coordinates.

    Parameters
    ----------
    file_location : str
        The location of the PDB file to read in

    Returns
    -------
    symbols : list
        List of atomic symbols from the PDB file
    coords : np.ndarray
        The coordinates from the PDB file
    """

    with open(f_loc) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coordinates = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coordinates)

    coords = np.array(coordinates)

    return symbols, coords
