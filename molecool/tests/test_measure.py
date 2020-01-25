"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np


def test_calculate_distance():
    """test will pass so long as `calculate_distance` function within `measure`
    module run as expected"""

    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])

    expected_distance = 1.0
    calculated_distance = molecool.calculate_distance(r1, r2)
    assert calculated_distance == expected_distance

def test_calculate_distance_typeerror():
    """test will pass so long as calling `calculate_distance` function within
    `measure` module does not raise TypeError"""

    r1 = [1, 0, 0]
    r2 = [0, 0, 0]

    with pytest.raises(TypeError):
        calculated_distance = molecool.calculate_distance(r1, r2)

def test_calculate_angle():
    """test will pass so long as `calculate_angle` function within `measure`
    module run as expected"""

    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_angle_in_degrees = 90
    calculated_angle_in_degrees = molecool.calculate_angle(r1, r2, r3, degrees=True)
    assert calculated_angle_in_degrees == expected_angle_in_degrees

@pytest.mark.parametrize("p1, p2, p3, expected_angle_in_degrees", [
(np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([0, 1, 0]), 45),
(np.array([1, 0, 0]), np.array([0, 0, 0]), np.array([0, 1, 0]), 90)
])
def test_calculate_angle_many(p1, p2, p3, expected_angle_in_degrees):
    """test will pass so long as `calculate_angle` function within `measure`
    module run as expected"""

    calculated_angle_in_degrees = molecool.calculate_angle(p1, p2, p3, degrees=True)
    assert calculated_angle_in_degrees == expected_angle_in_degrees
