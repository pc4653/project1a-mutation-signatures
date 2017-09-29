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



3. Seems like the bootstrapping part isn't helping with the result. Here is the result of skipping the bootstrapping part, just using NMF with random initialization.

![Alt text](without_bootstrap.jpg?raw=true "Optional Title")

also attaching the average silhoutte width for each cluster and consine simlarity of the generating mutation type and extracted mutation type:
average silhoutte width:

[0.99858662755549643, 0.99767012215251183, 0.99683224927509451, 0.99906200467683937, 0.99017610283904545]

orig signature 0 has the highest similarity with extracted signature 3 with 0.995844890677

orig signature 1 has the highest similarity with extracted signature 4 with 0.99012718356

orig signature 2 has the highest similarity with extracted signature 0 with 0.995805403673

orig signature 3 has the highest similarity with extracted signature 2 with 0.993754773022

orig signature 4 has the highest similarity with extracted signature 1 with 0.995061139948
