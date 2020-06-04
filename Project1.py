from math import sqrt
import time

def project_function(n):

    #iterate through function x times
    for _ in range (10):

        #capture start time
        start_time = time.time()

        #initialize and start outer loop
        j = 5
        while j < (n / 2):
            k = 5
            total = 0

            #initialize and start inner loop
            while k < n:
                total += j * k
                k = k * sqrt(2)
            j = sqrt(3) * j

        #capture end time
        end_time = time.time()

        #calculate running time
        time_delta = (end_time - start_time) * 1000000000 #measure time delta and convert to nanoseconds

        #print results
        print("Running Time for n = " + str(n) + " is " + str(int(time_delta)) + " nanoseconds")

        #increment n
        n = n * 10

project_function(100)
