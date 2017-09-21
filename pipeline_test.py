import numpy as np
import csv

signatures = np.load('example-signatures.npy')
with open('example-mutation-counts.tsv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    flag = 0
    list = []
    for row in csvReader:
        if flag == 0:
            flag = 1
            continue
        a = row[0].split('\t')
        observ = []
        for i in range(1, len(a)):
            observ.append(int(a[i]))
        list.append(observ)
		
M = np.transpose(np.asarray(list))



def dim_reduction( M ):
    """
    this reduce all the mutataion types that in total add up to no more than 1 percent of the total
    mutation counts, assuming M is of size # of types * # of observation
    """
    tot_count_per_type = M.sum(axis = 1)
    tot_count = float(tot_count_per_type.sum())
    sorted_index = np.argsort(tot_count_per_type)
    threshold = 0.01
    accu = 0
    for i in range(len(sorted_index)):
        perc = float(tot_count_per_type[sorted_index[i]])/tot_count
        accu = accu + perc
        if accu > threshold:
            break;
            
    return sorted_index[0:i]
    
    
elim_type = dim_reduction(M)
M_dot = np.delete(M, elim_type, axis=0)