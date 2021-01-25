import numpy as np
import pandas as pd

import sys
import os
sys.path.append(os.getcwd() + '/Util')
sys.path.append(os.getcwd() + '/config')

from configs import *

from DGH import DGH

file_data = os.getcwd() + '/data/adult.csv'
file_age = os.getcwd() + '/Config/Age_hierarchy.txt'
file_marital_status = os.getcwd() + '/Config/Age_hierarchy.txt'
file_race = os.getcwd() + '/Config/Age_hierarchy.txt'
file_sex = os.getcwd() + '/Config/Age_hierarchy.txt'

dgh_age = DGH(file_age)
dgh_marital_status = DGH(file_marital_status)
dgh_race = DGH(file_race)
dgh_sex = DGH(file_sex)

df = pd.read_csv(file_data)

quasi = df[['age', 'race' ,'marital.status', 'sex']]
quasi = quasi.astype(str)

# file_result = os.getcwd() + f'/result/adult_{k}.csv' 

a = 1
b = 1
fibo_list=[a, b]
while b < quasi.shape[0]:
    a, b = b, a+b
    fibo_list.append(b)

k_list = []
prec_list = []



K=2
step_k= 2
quasi = df[QUASI_FIELDS]
quasi = quasi.astype(str)

dgh = {}

for q in quasi.columns:
    dgh[q] = DGH(DIR_HIERARCHY + q + POSTFIX + FILE_EXTENSION)   


def cal_prec(K):
    precision_metric = 0

    while quasi.value_counts()[quasi.value_counts() < K].count() > 0:
        quasi_nunique = []
        for c in quasi.columns:
            quasi_nunique.append([c, quasi[c].nunique()])
        quasi_nunique_df = pd.DataFrame(quasi_nunique, columns=['column_name', 'n_unique' ])

        max_column_name = quasi_nunique_df[quasi_nunique_df.n_unique == quasi_nunique_df.n_unique.max()]['column_name'].values[0]

        for v in quasi[max_column_name].unique():
            status, result = dgh[max_column_name].next_gen(str(v))
            quasi.replace(v, result,inplace=True) 

    precision_metric = 0
    for c in QUASI_FIELDS:
        prec = quasi[c].apply(lambda v: dgh[c].height(v)/(dgh[c].max_height-1)).sum()
        precision_metric += prec

    precision_metric = 1 - precision_metric/(quasi.shape[0] * quasi.shape[1])
    return precision_metric
    

while True:
    if len(prec_list) == 0 :
        k_list.append(K)
        prec_list.append(cal_prec(K))
        print(f'k = {k_list[-1]} --- precision metric: {prec_list[-1]}')
        continue 
    
    k_next = (K + step_k) if ((K + step_k) < quasi.shape[0]) else (quasi.shape[0]-1)
    if prec_list[-1] != cal_prec(k_next):
        K += 1
        step_k = 2
        k_list.append(K)
        prec_list.append(cal_prec(K))
        print(f'k = {k_list[-1]} --- precision metric: {prec_list[-1]}')
    else:
        K = (K + step_k) if (K + step_k) < quasi.shape[0] else quasi.shape[0]-1
        step_k = step_k * 2 


    if K >= quasi.shape[0]:
        break
    if K == quasi.shape[0]-1:
        k_list.append(K)
        prec_list.append(cal_prec(K))
        print(f'k = {k_list[-1]} --- precision metric: {prec_list[-1]}')
        break

# # a = 1
# # b = 1
# # fibo_list=[a, b]
# # while b < quasi.shape[0]:
# #     a, b = b, a+b
# #     fibo_list.append(b)
# test_k = [1,1,2,2,2,3,3,4,5,5,5,5]
# b = 1
# fibo_list = [1]
# while b < len(test_k):
#     b = b *2
#     fibo_list.append(b)
# # fibo_list

# step_k = 2

# k_list = []
# prec_list = []
# K= 0
# prev_k = 0
# prev_prec = 0

# while True:
#     if len(prec_list) == 0 :
#         k_list.append(K)
#         prec_list.append(test_k[K])
#         print(f'k = {k_list[-1]} --- precision metric: {prec_list[-1]}')
#         continue 
    
#     k_next = (K + step_k) if ((K + step_k) < len(test_k)) else (len(test_k)-1)
#     if prec_list[-1] != test_k[k_next]:
#         K += 1
#         step_k = 2
#         k_list.append(K)
#         prec_list.append(test_k[K])
#         print(f'k = {k_list[-1]} --- precision metric: {prec_list[-1]}')
#     else:
#         K = (K + step_k) if (K + step_k) < len(test_k) else len(test_k)-1
#         step_k = step_k * 2 


#     if K >= len(test_k):
#         break
#     if K == len(test_k)-1:
#         k_list.append(K)
#         prec_list.append(test_k[K]) 
#         print(f'k = {k_list[-1]} --- precision metric: {prec_list[-1]}')
#         break


