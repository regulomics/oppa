# oppa
Optimal PCA-like Profile Aggregation

Written Bartek Wilczyński

You need to have python2.7, matplotlib and  numpy installed.

Hi-C data are taken as normalized numpy matrices (.npy)

To find domains run:

python find_domains.py test_data.npy > output.doms

To show them on your data (you can show the same files on both halves of the matrix or show two different datasets for contrast), you need to use show_domains from sherpa package.

python show_domains.py data_upper.npy doms_upper.doms data_lower.npy data_lower.doms
