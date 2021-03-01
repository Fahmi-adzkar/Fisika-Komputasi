# module swap
"""
swapRows(v,i,j)
Swaps baris i dan j dari suatu vector atau matriks [v]

swapCols(v,i,j)
Swaps kolom matrik [v]
"""


def swapRows(v, i, j):
    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j], :] = v[[j, i], :]


def swapCols(v, i, j):
    v[:, [i, j]] = v[:, [j, i]]
