# Project 1a: Mutation Signatures

For this project, you will implement and run the NMF mutation signature decomposition described in [Alexandrov, et al. (Cell Reports, 2013)](https://www.nature.com/nature/journal/v500/n7463/full/nature12477.html) on the data from [Alexandrov, et al. (Nature, 2013)](http://www.cell.com/cell-reports/abstract/S2211-1247(12)00433-0).

### Data

The input data for your algorithm is a mutation count matrix. The mutation count matrices are stored in a tab-separated text file, where each line lists the number of mutations of a given category for a single patient. The patient name will be stored in the first column, and the category names in the first row.

#### Example data

You can find a small example dataset for your project in [data/examples](https://github.com/cmsc828p-f17/project1a-mutation-signatures/blob/master/data/examples). The examples directory also includes the signatures used to generate the data, which you can use to sanity check your results.

#### Real data

You will need to download real data for your project and process it into the same format as the example data. You can find the Pan-Cancer mutation counts originally used by Alexandrov, et al. (Nature, 2013) at [ftp://ftp.sanger.ac.uk/pub/cancer/AlexandrovEtAl](ftp://ftp.sanger.ac.uk/pub/cancer/AlexandrovEtAl).


Progress:
1. combine all 96-mutation-type mat file into one numpy matrix and output to a .npy file
2. writing on the 6 steps pipeline, first test on the sample data provided by Max


![Alt text](result-1.jpg?raw=true "Optional Title")

update on average silhoutte width from this method:
[0.99725215726847416, 0.99848950992710583, 0.9976778738015889, 0.99932513185526106, 0.44953848114122957]

orig signature 0 has the highest similarity with extracted signature 1 with 0.919813771667

orig signature 1 has the highest similarity with extracted signature 4 with 0.710527936681

orig signature 2 has the highest similarity with extracted signature 3 with 0.896844557153

orig signature 3 has the highest similarity with extracted signature 2 with 0.921147707168

orig signature 4 has the highest similarity with extracted signature 0 with 0.800587169291



3. Seems like the bootstrapping part isn't helping with the result. Here is the result of skipping the bootstrapping part, just using NMF with random initialization. (since the "bootstrap" method uses every observation's distribution normalized as the "true" multinomial distribution, it possibly caused a softmax approximation and made the most apparent mutation the only mutation. Interestingly, the average Frobenius reconstruction error is significantly lower for the bootstrapped data than for the no bootstrap data (6.0169 vs 80.295))

![Alt text](without_bootstrap.jpg?raw=true "Optional Title")

also attaching the average silhoutte width for each cluster and consine simlarity of the generating mutation type and extracted mutation type:
average silhoutte width:

[0.99858662755549643, 0.99767012215251183, 0.99683224927509451, 0.99906200467683937, 0.99017610283904545]

orig signature 0 has the highest similarity with extracted signature 3 with 0.995844890677

orig signature 1 has the highest similarity with extracted signature 4 with 0.99012718356

orig signature 2 has the highest similarity with extracted signature 0 with 0.995805403673

orig signature 3 has the highest similarity with extracted signature 2 with 0.993754773022

orig signature 4 has the highest similarity with extracted signature 1 with 0.995061139948


4. Collect stats on running on different assumed number of mutation signatures
With Bootstrap

![Alt text](with_bootstrap_stats.jpg?raw=true "Optional Title")

Without Bootstrap

![Alt text](without_bootstrap_afr.jpg?raw=true "Optional Title")

![Alt text](without_bootstrap_asw.jpg?raw=true "Optional Title")

Applying to real dataset:

After applying the pipeline (bootstrapping taken out) to the real dataset, and comparing the result to the author's signatures, I couldn't find very consistent agreements given the number of signatures of 27. This may be due to reasons such as:


1. Didn't run enough iterations to reach convergence: I ran the pipeline for about 8 hours, totaling 500 iterations. According to the Cell article, rarely do we need more than 500 iterations to converge; however, this could still be a reason.

2. Ignored bootstrapping caused the algorithm to be stuck on local solutions/implemented bootstrapping wrong. 

To make sure that I am consistent with the Author's implementation, I downloaded and looked over his matlab examples. Here is some observations:

1. Both algorithm successfully extracted Max's sample data signatures.
2. The sample data given by the example seems to yield different results.


1. Although the author's implementation's bootstrapping seems to work, we have the same kind of bootstrap set up and observing the difference of his bootstrap instance with mine doesn't seem to dispute this --> graph here


2. By saving the author's bootstrap instances and use them in the result of my pipeline, we seem to still get different results.

3. By saving the author's nmf results and use them in the kmeans part of the pipeline, we get consistent results. The problem seems to be in the different implementations of NMF. 

4. Looking at/using different methods NMF listed in the example, it seems like every NMF produces slightly different results. ---> graph here



