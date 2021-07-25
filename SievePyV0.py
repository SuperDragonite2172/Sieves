# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Python Prime Sieve - Version 0                        #
# Written by SuperDragonite2172                         #
# Idea from Dave Plummer's Software Dragracing series   #
# Algorithm: Sieve of Eratosthenes (Implemented Poorly) #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from argparse import ArgumentParser # For command-line arguments
from timeit import default_timer # For timing the sieve

class PrimeSieve:

    primes = None # Array to store the primes
    size = 0 # The size of the sieve to run

    def __init__(self, limit):
        self.size = limit
        self.primes = [True] * (self.size)
    
    # runSieve: Runs the prime calculations.
    def runSieve(self):
        factor = 3
        
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
        self.primes[0] = None
        
    # printResults: Prints the statistics from the sieve run.
    def printResults(self, duration, passes, show_results):
        # TODO: Refine statistics.
        print("Time: %s\nPasses: %s\nAverage: %s" % (duration, passes, duration / passes))
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