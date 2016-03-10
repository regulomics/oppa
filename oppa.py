from functions import *
import argparse
import warnings,sys

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='OPPA - Optimal PCA-like Profile Aggregation')
    parser.add_argument("--data", metavar='data', type=str, help='A normalized Hi-C matrix for a single chromosome in .npy format')
    parser.add_argument("--output", metavar='output', type=str, help='The name of the ouptut file')
    
    args = parser.parse_args()
    if not args.data:
        print "you need to provide the --data argument. See oppa.py --help"
    else:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            M=numpy.load(args.data)
            M_c=numpy.clip(numpy.nan_to_num(M),-10,M.shape[0]/10) #clipped M matrix
            S = smooth_fast(M_c, width=1)
            N = normalize(S)
            C=pearson_fast(N)
            doms=dynamic_hier(N)
        if args.output:
            f=open(args.output,"w")
        else:
            f=sys.stdout
        to_file(doms,f)
        f.close()
        
        
 
        
