import numpy as np
import csv
import sig_extract
import time
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances

#hyperparameters
sign_num = 5
iteration = 500
remove_perc = 0.1

signatures = np.load('example-signatures.npy')
#load csv file into a list
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
        
#transpose list so dimension is as M requires		
M = np.transpose(np.asarray(list))

#get the indices of the eliminated weak signatures, and use M_dot from now on
elim_type = sig_extract.dim_reduction(M)
M_dot = np.delete(M, elim_type, axis=0)
M_dot = M_dot.astype(float)

#for every iteration of NMF, get the error and P and put them into a list
P_list = []
error_list = []
since = time.time()
for i in xrange(iteration):
    P, error = sig_extract.iteration(M_dot, sign_num)
    P_list.append(P)
    error_list.append(error)
	
	
time_elapsed = time.time() - since
print 'completed in ' + str(time_elapsed) + 'seconds.'

#remove iterations that have high error
remove_iter = iteration*remove_perc
sorted_index = np.argsort(error_list)
temp = sorted_index[len(sorted_index)-int(remove_iter):len(sorted_index)]
error_list = np.delete(error_list, temp)
P_list = np.delete(P_list, temp, axis = 0)

#putting all verisions of mutation signatures into one matrix
cluster_vec = np.transpose(P_list[0])
for i in range(1,len(P_list)):
    cluster_vec = np.vstack([cluster_vec, np.transpose(P_list[i])])

    
#use kmeans to find clusters of N    
kmeans = KMeans(n_clusters=sign_num, random_state=0).fit(cluster_vec)

#seperating clusters into its own list and calculate the average silhoutte width
#of each cluster
cluster = {}
for i in range(sign_num):
    cluster[i] = []
    
for i in range(sign_num):
    for j in range(len(kmeans.labels_)):
        if kmeans.labels_[j] == i:
            cluster[i].append(cluster_vec[j])

cluster_sil = []
    
for i in range(sign_num):
        cluster_sil.append(sig_extract.avg_sil_width(cluster[i], kmeans.cluster_centers_[i]))
    
print cluster_sil
    

#putting the eliminated signatures back into the extracted signatures for 
#comparison's sake
elim_type = np.sort(elim_type)
result = []
for i in range(sign_num):
    a = kmeans.cluster_centers_[i]
    for j in elim_type:
        a = np.insert(a, j, 0)
        
    result.append(a)

    
#compare results to the original signatures:
for i in range(5):
    val = []
    for j in range(5):
        val.append(sig_extract.cos_sim(signatures[i], result[j]))
    index = np.argsort(val)    
    print "orig signature " + str(i) + " has the highest similarity with extracted signature " + str(index[len(index)-1]) + " with " + str(val[index[len(index)-1]]) 
