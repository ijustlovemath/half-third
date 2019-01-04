import math
import random
import sys
from collections import defaultdict
import matplotlib.pyplot as plt

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

def test_a_bunch(max_N=1000, iterations=100, result_dict=defaultdict(list)):
    for N in range(3, max_N+1):
        for j in range(iterations):
            k, _ = thirdsday(N, estimate=random.random(), silent=True)
            result_dict[N].append(k)
    return result_dict

def plot_tests(max_N=1000, iterations=100):
    d = test_a_bunch(max_N, iterations)
    maxs = []
    mins = []

    # Assume d ordered...
    for _, v in d.items():
        maxs.append(max(v))
        mins.append(min(v))

    plt.plot(maxs)
    plt.plot(mins)
    plt.title('Thirsday convergence for N={}'.format(max_N))
    plt.xlabel('N')
    plt.ylabel('Iterations to convergence')
    plt.show(block=False)
