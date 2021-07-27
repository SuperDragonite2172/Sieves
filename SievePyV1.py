# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Python Prime Sieve - Version 1                      #
# Written by SuperDragonite2172                       #
# Idea from Dave Plummer's Software Dragracing series #
# Algorithm: Sieve of Eratosthenes (Implemented Well) #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

from argparse import ArgumentParser # For command-line arguments
from timeit import default_timer # For timing the sieve
from math import sqrt # Used by the sieve

class PrimeSieve:

    primes = None # Array to store the primes
    size = 0 # The size of the sieve to run

    def __init__(self, limit):
        self.size = limit
        self.primes = [True] * (self.size + 1)
    
    # runSieve: Runs the prime calculations.
    def runSieve(self):
        for i in range(2, int(sqrt(len(self.primes)))+1):
            if self.primes[i] == True:
                for j in range(i*i, len(self.primes), i):
                    self.primes[j] = False
        self.primes = self.primes[1:]
        self.primes[0] = None
        
    # printResults: Prints the statistics from the sieve run.
    def printResults(self, duration, passes, show_results):
        print(f"Time: {duration}\nPasses: {passes:,}\nPasses/sec: {passes / duration:,}\nAverage: {duration / passes}")
        if show_results:
            print(dict(enumerate(self.primes,1)))

# Command-line Parsing
parser = ArgumentParser(description="Language: Python, Algorithm: Sieve of Eratosthenes, Dependencies: None")
parser.add_argument("--limit"  , "-l", help="The upper limit of the sieve.", type=int, default=1000000)
parser.add_argument("--time"   , "-t", help="How long the sieve will run.", type=float, default=10)
parser.add_argument("--results", "-r", help="Display the primes found.", action="store_true")

# Main Body
args = parser.parse_args()
limit = args.limit
time_limit = args.time
show_results = args.results

timer_start = default_timer()
passes = 0

while (default_timer() - timer_start < time_limit):
    sieve = PrimeSieve(limit)
    sieve.runSieve()
    passes += 1

time_elapsed = default_timer() - timer_start

sieve.printResults(time_elapsed, passes, show_results)