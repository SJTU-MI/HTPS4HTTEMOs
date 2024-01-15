#!/usr/bin/env python
# coding: utf-8

from gplearn.genetic import SymbolicRegressor
import gplearn.fitness
import pandas as pd
import numpy as np

train_file_path = r"../data/filter_data3.csv"
train_csv = pd.read_csv(train_file_path)
train_csv = train_csv.set_index(["ID"])

# Training samples
X_train = np.array(train_csv.iloc[:,1:19])
y_train = np.array(train_csv.iloc[:,train_csv.columns == "pf_log"])

est_gp = SymbolicRegressor(function_set=['add','sub','mul','div','sqrt','log','abs','neg','inv'],
                           population_size=5000,generations=300,tournament_size=20,max_samples=0.9,verbose=0,
                           parsimony_coefficient = 'auto',metric = 'spearman',stopping_criteria=0.9,
                           init_depth=(2,6),
                           p_crossover=pc_round_set,
                           p_subtree_mutation=ps_round_set,
                           p_hoist_mutation=ph_round_set,
                           p_point_mutation=pp_round_set,
                           random_state=random_state_set)

est_gp.fit(X_train, y_train.ravel())

print(est_gp._program.raw_fitness_, est_gp._program.fitness_, est_gp._program.oob_fitness_,
      est_gp._program.depth_, est_gp._program.length_, est_gp._program)