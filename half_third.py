import math
import random
import sys
from collections import defaultdict

def calc_one_by_n(n, estimate):
    new_estimate = (1 - estimate) / (n-1)
    return new_estimate

def thirdsday(n=3, estimate=random.random(), silent=False):
    i = 1
    while True:
        estimate = calc_one_by_n(n, estimate)
        if math.isclose(estimate, 1.0 / n):
            if not silent:
                print("converged in {} iterations, ".format(i)
                    +"estimate for 1/{} is: {}".format(n,estimate))
            return i, estimate
        i += 1

def test_a_bunch(max_number=1000, iteration_number=100, result_dict=defaultdict(list)):
    for i in range(3, max_number):
        print('testing number {}'.format(i))
        for j in range(iteration_number):
            k, _ = thirdsday(i, estimate=random.random(), silent=True)
            result_dict[i].append(k)
            print(j, end='\r')
            #sys.stdout.flush()
        print('done collecting results for {}'.format(i))
    return result_dict
