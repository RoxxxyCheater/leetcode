# 1514. Path with Maximum Probability
# Medium

# 2719

# 58

# Add to List

# Share
# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

# Example 1:



# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
# Example 2:



# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
# Output: 0.30000
# Example 3:



# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.
 
 
# Constraints:

# 2 <= n <= 10^4
# 0 <= start, end < n
# start != end
# 0 <= a, b < n
# a != b
# 0 <= succProb.length == edges.length <= 2*10^4
# 0 <= succProb[i] <= 1
# There is at most one edge between every two nodes.
# Accepted
# 106,219
# Submissions
# 195,701



class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        return res



list_n = 3, 3, 3 
list_edges = [[0,1],[1,2],[0,2]], [[0,1],[1,2],[0,2]],  [[0,1]]
list_succProb = [0.5,0.5,0.2], [0.5,0.5,0.3], [0.5]
list_start= 0, 0, 0
list_end = 2, 2, 2

for index, num in enumerate(list_n):
   Solution.maxProbability('Success', num, list_edges[index], list_succProb[index], list_start[index], list_end[index])
