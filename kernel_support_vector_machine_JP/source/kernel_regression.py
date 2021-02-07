# Python script
#
# Author: Tetsuya Ishikawa <tiskw111gmail.com>
# Date  : Aug  3, 2019
#################################### SOURCE START ###################################

import numpy as np
import matplotlib.pyplot as mpl

### RBF カーネル関数
def kernel_func_RBF(x1, x2, gamma):
    return np.exp(-gamma * (x1 - x2)**2)

### カーネル関数を生成する関数
def generate_kernel_matrix(xs, func):
    return np.array([[func(xs[m], xs[n]) for n in range(len(xs))] for m in range(len(xs))])

### カーネル回帰の最適化問題を解く関数
def solve_kernel_regression(ys, K, l):
    return np.linalg.inv(K + l * np.eye(K.shape[0])).dot(ys)

### 回帰のための点群を生成する関数
def generate_regression_curve(zs, cs, xs, func):
    return np.array([sum([c * func(z, x) for c, x in zip(cs, xs)]) for z in zs])

if __name__ == "__main__":

    np.random.seed(111)

    ### 各クラスのサンプル数
    N = 21

    ### サンプル点を生成
    xs = np.linspace(0, np.pi, N)
    ys = np.sin(xs) + 0.2 * np.random.randn(N)

    ### カーネル関数の設計（カリー化しておかないと後の関数で使えない）
    sigma = 1.0E+1
    gamma = 1 / (4 * sigma**2)
    func  = lambda x1, x2: kernel_func_RBF(x1, x2, gamma)

    ### カーネル行列の生成
    K = generate_kernel_matrix(xs, func)

    ### カーネル回帰の最適化問題を解く
    l  = 1.0E-5
    cs = solve_kernel_regression(ys, K, l)

    ### カーネル回帰の結果を描画するための点群を生成
    us = np.linspace(0, np.pi, 101)
    vs = generate_regression_curve(us, cs, xs, func)

    ### サンプル点と回帰結果を描画
    mpl.figure()
    mpl.plot(xs, ys, "o", label = "Sample points")
    mpl.plot(us, vs, "-", label = "Regression curve (sigma = %.1e)" % sigma)
    mpl.legend()
    mpl.grid()
    mpl.show()

#################################### SOURCE FINISH ##################################
# vim: expandtab tabstop=4 shiftwidth=4
