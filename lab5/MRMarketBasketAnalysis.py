"""
.. module:: MRMarketBasketAnalysis

MRMarketBasketAnalysis
**********************

:Description: MRMarketBasketAnalysis

    Executes the MRMarketBasket1 and MRMarketBasket2 scripts


:Created on: 16/11/2023

"""

from MRMarketBasket1 import MRMarketBasket1
from MRMarketBasket2 import MRMarketBasket2
import argparse
import time
from mrjob.util import to_lines
import pandas as pd
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='groceries.csv', help='Groceries file')
    parser.add_argument('--ncores', default=2, type=int, help='Number of parallel processes to use')
    
    args = parser.parse_args()
   
    tinit = time.time()  # For timing the execution
    
    mr_job1 = MRMarketBasket1(args=['-r', 'local', args.file,'--num-cores', str(args.ncores)])
    # Runs the script1
    with mr_job1.make_runner() as runner1:
        runner1.run()
        pairs = {}
        # Process the results of the script iterating the (key,value) pairs
        for key, value in mr_job1.parse_output(runner1.cat_output()):
            
            # You should store things here probably in a data structure
            
        
    mr_job2 = MRMarketBasket2(args=['-r', 'local', args.file,'--num-cores', str(args.ncores)])
    # Runs the script2     
    with mr_job2.make_runner() as runner2:
        runner2.run()
        # Process the results of the script iterating the (key,value) pairs
        singles = {}
        for key, value in mr_job2.parse_output(runner2.cat_output()):
            
            # You should store things here probably in a data structure
            
    print(f'Time= {(time.time() - tinit)} seconds')
    
        
    # Get the total number of transaction in the file given as argument
    ntrans = int(subprocess.check_output(["wc", "-l", args.file]).decode("utf8").split()[0])
    print(f'\nNumber of transactions {ntrans}')
    print()
    
    
    print("******************************************************************************* ")
    print("************ Values and rules to fill the required table ********************** ")
    print("******************************************************************************* ")    
    for support, conf in [(0.01,0.01),(0.01,0.25),(0.01,0.5),(0.01,0.75),(0.05,0.25),(0.07,0.25),(0.20,0.25),(0.5,0.25)]:
        
        # Compute the number of rules (nr) for each pair of support and confidence thresholds
        # and show the rules for the pairs of support and confidence values required
 
        print("Support=", str(support),"confidence=", str(conf)+".", "Rules found", nr, '\n') 
    

