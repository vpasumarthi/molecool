"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np


def test_measure():
    """Sample test, will always pass so long as functions within 'measure'
    module run as expected"""

    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_distance = 1.0
    calculated_distance = molecool.calculate_distance(r1, r2)
    assert calculated_distance == expected_distance

    expected_angle_in_degrees = 90
    calculated_angle_in_degrees = molecool.calculate_angle(r1, r2, r3, degrees=True)
    assert calculated_angle_in_degrees == expected_angle_in_degrees
