import scipy.io as io
import os
#This loads all mat files in exome and genome dataset, 
#append the matrices and create final matrix with all 
#the observations in column.
root = 'data/mutational_catalogs/'
flag = False
root_folders = os.listdir(root)
for folder in root_folders:
	cancer_root = root + folder + '/'
	cancers = os.listdir(cancer_root)
	for cancer in cancers:
		if cancer == '.DS_Store':
			continue
		file_path = cancer_root + cancer + '/'
		files = os.listdir(cancer_root + cancer)
		for file in files:
			if '96' in file and '.mat' in file:
				mat_path = file_path + file
				if flag:
					temp = A
					A = io.loadmat(mat_path)
					A = A['originalGenomes']
					A = np.concatenate((temp,A), axis = 1)
				else:
					flag = True
					A = io.loadmat(mat_path)
					A = A['originalGenomes']					
					



