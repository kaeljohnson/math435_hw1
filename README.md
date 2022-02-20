(1) Download the dataset and turn the adjacency list into matrix.

(2) Explain the implication of the damping factor.
**Explain Damping Factor**

Damping factor necessity comes from the notion that a web 
surfer randomly clicking/typing links in a web browser will stop at some point. 
Formally, damping factor is the probability that at any step, 
a said web surfer will continue clicking/typing links. The 
damping factor is subtracted from one and divided by number of documents.

(3) Develop the transition matrices T for this network respectively using algorithm with and with-
out damping.

(4) Find the stationary distribution of the either matrix T using fixed point iterations and eigen-
vector calculation.

(5) Discuss the whether and how your final distribution depends on your initial choice of the
distribution in your iterations.

It does not matter. As long as the data is normalized the distribution vector will converge to the 
correct stationary distribution.

(6) In your iterations, what about if the summation of the distribution vector does not sum to 1?
Discuss the possible consequence and whether a treatment is necessary (and how to develop a
treatment).

(7) Properly illustrate this network (https://www.mathworks.com/help/matlab/graph-and-network-algorithms.
html with MATLAB, or https://networkx.org/ with Python. You may present the ranking
of nodes using different colors.)

(8) Write report no less than 4 pages (computer code does not count), attach your computer code,
and prepare for class presentation with Powerpoint.

