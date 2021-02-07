#!/usr/bin/env python3
#
# Author: Tetsuya Ishikawa <tiskw111gmail.com>
# Date  : Jun 29, 2019
#################################### SOURCE START ###################################

import numpy as np
import matplotlib.pyplot as mpl
import pulp

def solve_linear_svm(xs, ys):

    ### データ点数および入力データの次元を取得
    M, N = len(xs[0]), len(xs)

    ### 線形計画問題で使用する変数を宣言
    var_w  = pulp.LpVariable.dicts("w",  (range(M)), None, None, "Continuous")
    var_xi = pulp.LpVariable.dicts("xi", (range(N)), 0,    None, "Continuous")

    ### 線形計画問題（最小化）のソルバを作成
    problem = pulp.LpProblem("Naive linear SVM", pulp.LpMinimize)

    ### 目的関数の設定
    problem += pulp.lpSum(var_xi)

    ### 制約条件の設定
    for n in range(N):
        problem += var_xi[n] >= 1.0 - ys[n] * pulp.lpSum([var_w[m] * xs[n][m] for m in range(M)])

    ### ソルバの実行
    problem.solve()

    ### 結果の取得
    status  = pulp.LpStatus[problem.status]
    val_obj = pulp.value(problem.objective)
    val_w   = [var_w[n].varValue for n in range(3)]

    return (val_w, val_obj, status)

if __name__ == "__main__":

    ### 入力変数の次元（2 次元に定数項の分を追加して 3 次元とする）
    M = 2 + 1

    ### 各クラスのサンプル数
    N = 100

    ### 各クラスのサンプル点を生成
    xs_class1 = [(*np.random.normal(0.2, 0.2, (M - 1, )), 1) for _ in range(N)]
    xs_class2 = [(*np.random.normal(0.8, 0.2, (M - 1, )), 1) for _ in range(N)]

    ### 各クラスのラベルを生成
    ys_class1 = [+1] * N
    ys_class2 = [-1] * N

    ### 線形判別直線を算出
    xs = xs_class1 + xs_class2
    ys = ys_class1 + ys_class2
    ws, _, status = solve_linear_svm(xs, ys)

    ### 判別曲線を描画できるよう点列に変換
    us = np.linspace(0, 1, 2)
    vs = -(ws[0] * us + ws[2]) / ws[1]

    ### 各クラスの点群および判別曲線を描画
    mpl.figure()
    mpl.plot([x[0] for x in xs_class1], [x[1] for x in xs_class1], "o")
    mpl.plot([x[0] for x in xs_class2], [x[1] for x in xs_class2], "o")
    mpl.plot(us, vs, "-")
    mpl.grid()
    mpl.show()

#################################### SOURCE FINISH ##################################
# vim: expandtab tabstop=4 shiftwidth=4
