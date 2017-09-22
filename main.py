import numpy as np
import csv
import sig_extract
import time
from sklearn.cluster import KMeans

sign_num = 5
iteration = 500
remove_perc = 0.1

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
elim_type = sig_extract.dim_reduction(M)
M_dot = np.delete(M, elim_type, axis=0)
M_dot = M_dot.astype(float)

P_list = []
error_list = []
since = time.time()
for i in xrange(iteration):
	#record = [P, error]
    P, error = sig_extract.iteration(M_dot, sign_num)
    P_list.append(P)
    error_list.append(error)
	
	
time_elapsed = time.time() - since
print 'completed in ' + str(time_elapsed) + 'seconds.'

remove_iter = iteration*remove_perc
sorted_index = np.argsort(error_list)
temp = sorted_index[len(sorted_index)-int(remove_iter):len(sorted_index)]
error_list = np.delete(error_list, temp)
P_list = np.delete(P_list, temp, axis = 0)
cluster_vec = np.transpose(P_list[0])
for i in range(1,len(P_list)):
    cluster_vec = np.vstack([cluster_vec, np.transpose(P_list[i])])

kmeans = KMeans(n_clusters=5, random_state=0).fit(cluster_vec)
elim_type = np.sort(elim_type)
result = []
for i in range(sign_num):
    a = kmeans.cluster_centers_[i]
    for j in elim_type:
        a = np.insert(a, j, 0)
        
    result.append(a)
    
