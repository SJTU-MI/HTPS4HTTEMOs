#!/usr/bin/env python
# coding: utf-8

from gplearn.genetic import SymbolicRegressor
import gplearn.fitness
import pandas as pd
import numpy as np
import scipy
from scipy.spatial.distance import pdist, squareform
from scipy import stats
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

train_file_path = r"../data/filter_data3.csv"
train_csv = pd.read_csv(train_file_path)
train_csv = train_csv.set_index(["ID"])

# Training samples
X_train = np.array(train_csv.iloc[:,1:19])
scaler.fit(X_train)
X_train_scaler = scaler.transform(X_train)
y_train = np.array(train_csv.iloc[:,train_csv.columns == "pf_log"])


def _dis_corr(y, y_pred, w):
    with np.errstate(divide='ignore', invalid='ignore', over='ignore', under='ignore'):
        X = np.atleast_1d(y)
        Y = np.atleast_1d(y_pred)
        if np.prod(X.shape) == len(X):
            X = X[:, None]
        if np.prod(Y.shape) == len(Y):
            Y = Y[:, None]
        X = np.atleast_2d(X)
        Y = np.atleast_2d(Y)
        n = X.shape[0]

        a = squareform(pdist(X))
        b = squareform(pdist(Y))
        A = a - a.mean(axis=0)[None, :] - a.mean(axis=1)[:, None] + a.mean()
        B = b - b.mean(axis=0)[None, :] - b.mean(axis=1)[:, None] + b.mean()

        dcov2_xy = float((A * B).sum() / float(n * n))
        dcov2_xx = float((A * A).sum() / float(n * n))
        dcov2_yy = float((B * B).sum() / float(n * n))
        return float(np.where((float(dcov2_xx) > 0.001) & (float(dcov2_yy) > 0.001), float(np.sqrt(dcov2_xy) / np.sqrt(np.sqrt(dcov2_xx) * np.sqrt(dcov2_yy))), 0.01))

dis_corr = gplearn.fitness.make_fitness(function=_dis_corr,greater_is_better=True)

est_gp = SymbolicRegressor(function_set=['add','sub','mul','div','sqrt','log','abs','neg','inv'],
                           population_size=5000,generations=300,tournament_size=20,max_samples=0.9,verbose=0,
                           parsimony_coefficient = 'auto',metric = dis_corr,stopping_criteria=0.9,
                           init_depth=(2,6),
                           p_crossover=pc_round_set,
                           p_subtree_mutation=ps_round_set,
                           p_hoist_mutation=ph_round_set,
                           p_point_mutation=pp_round_set,
                           random_state=random_state_set)

est_gp.fit(X_train, y_train.ravel())

print(est_gp._program.raw_fitness_, est_gp._program.fitness_, est_gp._program.oob_fitness_,
      est_gp._program.depth_, est_gp._program.length_, est_gp._program)