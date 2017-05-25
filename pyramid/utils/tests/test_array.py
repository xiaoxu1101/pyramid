
from __future__ import absolute_import
from pyramid.utils.array import diff, c
from numpy.testing import assert_array_equal
import numpy as np

x = np.arange(5)
m = np.array([10, 5, 12, 23, 18, 3, 2, 0, 12]).reshape(3,3).T


def test_diff():
    # test vector for lag = (1, 2), diff = (1, 2)
    assert_array_equal(diff(x, lag=1, differences=1), np.ones(4))
    assert_array_equal(diff(x, lag=1, differences=2), np.zeros(3))
    assert_array_equal(diff(x, lag=2, differences=1), np.ones(3) * 2)
    assert_array_equal(diff(x, lag=2, differences=2), np.zeros(1))

    # test matrix for lag = (1, 2), diff = (1, 2)
    assert_array_equal(diff(m, lag=1, differences=1), np.array([[-5, -5, -2], [7, -15, 12]]))
    assert_array_equal(diff(m, lag=1, differences=2), np.array([[12, -10, 14]]))
    assert_array_equal(diff(m, lag=2, differences=1), np.array([[2, -20, 10]]))
    assert diff(m, lag=2, differences=2).shape[0] == 0


def test_concatenate():
    assert_array_equal(c(1, np.zeros(3)), np.array([1.0, 0.0, 0.0, 0.0]))
    assert_array_equal(c([1], np.zeros(3)), np.array([1.0, 0.0, 0.0, 0.0]))