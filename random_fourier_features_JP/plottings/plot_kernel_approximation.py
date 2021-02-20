#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as mpl

def plot_heatmap(fig, ax, mat):

    ax.imshow(mat)
    ax.set_xticks(np.linspace(0, 100, 11))
    ax.set_yticks(np.linspace(0, 100, 11))
    ax.set_xticklabels(["%.1f" % x for x in np.linspace(-1, 1, 11)])
    ax.set_yticklabels(["%.1f" % x for x in np.linspace(-1, 1, 11)])


def save_csv(mat, filepath):

    with open(filepath, "wt") as ofp:
        for m in range(mat.shape[0]):
            for n in range(mat.shape[1]):
                ofp.write("%d,%d,%.2e\n" % (m, n, mat[m, n]))

def main():

    def k(x1, x2):
        return np.exp(-0.5 * (x1 - x2)**2)

    def rff(x1, x2, dim):
        w  = np.random.randn(dim)
        u1 = np.array([np.cos(w.T * x1), np.sin(w.T * x1)]).flatten()
        u2 = np.array([np.cos(w.T * x2), np.sin(w.T * x2)]).flatten()
        return np.dot(u1, u2) / dim

    x1s = np.linspace(-1, 1, 101)
    x2s = np.linspace(-1, 1, 101)

    mat0 = [[k(x1, x2) for x1 in x1s] for x2 in x2s]
    mat0 = np.array(mat0)

    mat1 = [[rff(x1, x2, 10) for x1 in x1s] for x2 in x2s]
    mat1 = np.array(mat1)

    mat2 = [[rff(x1, x2, 100) for x1 in x1s] for x2 in x2s]
    mat2 = np.array(mat2)

    mat3 = [[rff(x1, x2, 1000) for x1 in x1s] for x2 in x2s]
    mat3 = np.array(mat3)

    save_csv(mat0, "data_kernel.csv")
    save_csv(mat1, "data_rff_1e1.csv")
    save_csv(mat2, "data_rff_1e2.csv")
    save_csv(mat3, "data_rff_1e3.csv")

    fig = mpl.figure(figsize=(18, 5))

    ax = mpl.subplot(1, 4, 1)
    plot_heatmap(fig, ax, mat1)

    ax = mpl.subplot(1, 4, 2)
    plot_heatmap(fig, ax, mat2)

    ax = mpl.subplot(1, 4, 3)
    plot_heatmap(fig, ax, mat3)

    ax = mpl.subplot(1, 4, 4)
    plot_heatmap(fig, ax, mat0)

    mpl.show()


if __name__ == "__main__":
    main()
