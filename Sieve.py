# Prime Sieves - Python Edition
# Written by SuperDragonite2172
# Design Concept from Dave Plummer's Software Dragracing series

import argparse
import timeit

class PrimeSieve:

    primes = None # Array to store the primes
    size = 0 # The size of the sieve to run

    def __init__(self, limit):
        self.size = limit
        self.primes = [True] * self.size
    
    # runSieve: Runs the prime calculations.
    def runSieve(self):
        factor = 3
        self.primes[0] = False
        
        while (factor < len(self.primes)):
            for i in range(len(self.primes)):
                if (i + 1 == factor or i + 1 == 2):
                    pass
                elif ((i + 1) % 2 == 0):
                    self.primes[i] = False
                else:
                    if ((i + 1) % factor == 0):
                        self.primes[i] = False
            factor += 2
    
    # printResults: Prints the results of the sieve runs.
    def printResults(self, time, pass_num):
        print("Time: " + str(time))
        print("Passes: " + str(pass_num))
        print("Average: " + str(time / pass_num))

parser = argparse.ArgumentParser(description="A prime sieve written in Python.  Uses no dependencies.")
parser.add_argument("-l", "--limit", help="The upper limit of the sieve.  Defaults to 1000000", type=int, default=1000000)
args = parser.parse_args()

timer_start = timeit.default_timer()
passes = 0

while (timeit.default_timer() - timer_start < 10):
    sieve = PrimeSieve(args.limit)
    sieve.runSieve()
    passes += 1

time_elapsed = timeit.default_timer() - timer_start

sieve.printResults(time_elapsed, passes)