# Tomas Kazmar, 2012, BSD 2-clause license, see LICENSE
#
# This code was adapted from http://syzygy.st/code.html#pyLAPJV
# Thanks to Dr N.D. van Foreest for providing this example code.

"""
The cost matrix is based on Balas and Toth, 1985, Branch and bound
# methods, in Lawler, E.L, et al., The TSP, John Wiley & Sons,
Chischester, pp 361--401.
"""

def test_lap():
    import numpy as np
    import lapjv

    large = 1000
    cost = np.array( [[large,2,11,10,8,7,6,5],
                      [6,large,1,8,8,4,6,7],
                      [5,12,large,11,8,12,3,11],
                      [11,9,10,large,1,9,8,10],
                      [11,11,9,4,large,2,10,9],
                      [12,8,5,2,11,large,11,9],
                      [10,11,12,10,9,12,large,3],
                      [10,10,10,10,6,3,1,large]] )

    ret = lapjv.lap(cost)

    assert ret[0] == 17.0
    assert np.all(ret[1] == [1, 2, 0, 4, 5, 3, 7, 6])
    assert np.all(ret[2] == [2, 0, 1, 5, 3, 4, 7, 6])

    assert cost[range(cost.shape[0]), ret[1]].sum() == ret[0]
    assert cost[ret[2], range(cost.shape[1])].sum() == ret[0]
