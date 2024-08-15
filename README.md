I graphed the cumulative GC-skew (#G - #C) and used the absolute minimum of the curve to determine the approximate location of the bacterium’s oriC. My variable was the window of DNA in which I searched for DnaA boxes. I changed the window length (L = 500 bp or 1000 bp) and whether the absolute minimum was located at the beginning (start) or middle (mid) of the window.

The algorithm I used to find potential DnaA boxes searched for all the approximate 9-mers (sequences that were 9 bp long and had a Hamming distance less than a threshold d=1) that appeared most frequently within the given window, including the occurrences of their reverse complement.

I first used the skew and algorithm on the genome of E. coli, which has an experimentally confirmed oriC and DnaA box (TTATCCACA), to test out my code’s validity. I then applied my code to predict the oriCs and DnaA boxes of Synechococcus sp. JA-2-3B’a(2–13) and Synechococcus sp. JA-3-3Ab, both of which don’t have experimentally confirmed data. I compared my results with the research conducted by Sernova and Gelfand (2008). 

I used the NumPy, Matplotlib, and Requests Python libraries to scrape websites for their genome data and graph the GC-skews of the bacteria.
