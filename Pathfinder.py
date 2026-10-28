"""
================================================================================
PROJECT: Deterministic Grid-Based Path Planning & Heuristic Search Benchmark
COURSE: CSC 632 Artificial Intelligence Final Project (Option 1)
STUDENT NAME: Zachariah Ignatius McCullough
================================================================================

REFERENCES:

[1] Python Software Foundation, "heapq — Heap queue algorithm," Python Documentation, 2025. [Online]. Available: https://docs.python.org/3/library/heapq.html
[2] Python Software Foundation, "collections — Container datatypes," Python Documentation, 2025. [Online]. Available: https://docs.python.org/3/library/collections.html
[3] C. R. Harris et al., "Array programming with NumPy," Nature, vol. 585, no. 7825, pp. 357–362, 2020. https://www.nature.com/articles/s41586-020-2649-2
[4] J. D. Hunter, "Matplotlib: A 2D graphics environment," Computing in Science & Engineering, vol. 9, no. 3, pp. 90–95, 2007. https://ieeexplore.ieee.org/document/4160265
[5] S. Russell and P. Norvig, Artificial Intelligence: A Modern Approach, 4th ed. Pearson, 2020.
[6] P. E. Hart, N. J. Nilsson, and B. Raphael, "A formal basis for the heuristic determination of minimum cost paths," IEEE Transactions on Systems Science and Cybernetics, vol. 4, no. 2, pp. 100–107, 1968. https://ieeexplore.ieee.org/document/4082128
[7] E. W. Dijkstra, "A note on two problems in connexion with graphs," Numerische Mathematik, vol. 1, no. 1, pp. 269–271, 1959. https://ir.cwi.nl/pub/9256/9256D.pdf
[8] The Farama Foundation, "Toy Text Environments: FrozenLake," Gymnasium Documentation, 2025. [Online]. Available: https://gymnasium.farama.org/environments/toy_text/frozen_lake/
[9] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction, 2nd ed. MIT Press, 2018. https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf
[10] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, Introduction to Algorithms, 4th ed. MIT Press, 2022. https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf
[11] J. Pearl, Heuristics: Intelligent Search Strategies for Computer Problem Solving. Addison-Wesley, 1984. https://www.scribd.com/document/820231576/Judea-Pearl-Heuristics-Intelligent-Search-Strategies-for-Computer-Problem-Solving#page=45
[12] W. G. Macready and D. H. Wolpert, "Cost-free, value-free parameter configuration for search algorithms," IEEE Transactions on Evolutionary Computation, vol. 1, no. 1, pp. 41–58, Apr. 1997. [Online]. Available: https://www.cs.ubc.ca/~hutter/earg/papers07/00585893.pdf
[13] C. Demetrescu and G. F. Italiano, "Engineering shortest path algorithms," in Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), vol. 3046, May 2004, pp. 238–259. doi: 10.1007/978-3-540-24838-5_14.
[14] C. Stachniss, "Introduction to Mobile Robotics: Graph Search and Dijkstra/A*," University of Bonn, 2016.
[15] J. C. Latombe, Robot Motion Planning. Kluwer Academic Publishers, 1991. https://www.researchgate.net/publication/242351349_Robot_Motion_Planning_A_Distributed_Representation_Approach
[16] R. E. Korf, "Depth-first iterative-deepening: An optimal admissible search strategy," Artificial Intelligence, vol. 27, no. 1, pp. 97–109, 1985. https://www.cse.sc.edu/~mgv/csce580f09/gradPres/korf_IDAStar_1985.pdf
[17] R. Dechter and J. Pearl, "Generalized best-first search strategies and the optimality of A*," Journal of the ACM, vol. 32, no. 3, pp. 505–536, 1985. https://dl.acm.org/doi/pdf/10.1145/3828.3830
[18] D. E. Knuth, The Art of Computer Programming, Volume 1: Fundamental Algorithms, 3rd ed. Addison-Wesley, 1997. http://f.javier.io/rep/books/Donald-Knuth---The-Art-of-Computer-Programming-Vol-1-Fundamental-Algorithms.pdf
[19] R. Sedgewick and K. Wayne, Algorithms, 4th ed. Addison-Wesley, 2011. https://cs-web.bu.edu/fac/snyder/cs112/CourseMaterials/AlgorithmsChapterOne.pdf
[20] J. S. Baras and D. Theodorakopoulos, "Path planning in dynamic environments," in IEEE Conference on Decision and Control, 2002. https://arxiv.org/pdf/1605.06853
[21] S. Koenig and M. Likhachev, "Improved fast replanning for robot navigation in unknown terrain," in AAAI, 2002. https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite.pdf
[22] S. Thrun, W. Burgard, and D. Fox, Probabilistic Robotics. MIT Press, 2005. https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf
[23] S. M. LaValle, Planning Algorithms. Cambridge University Press, 2006. https://lavalle.pl/planning/book.pdf
[24] N. J. Nilsson, Artificial Intelligence: A New Synthesis. Morgan Kaufmann, 1998.
[25] P. H. Winston, Artificial Intelligence, 3rd ed. Addison-Wesley, 1992. https://courses.csail.mit.edu/6.034f/ai3/rest.pdf
[26] Z. Zertz, Graph Theory and Its Applications. CRC Press, 1995.
[27] A. Barr and E. A. Feigenbaum, The Handbook of Artificial Intelligence, Volume 1. William Kaufmann, 1981. [Online]. Available: https://dl.acm.org/doi/book/10.5555/540417
[28] S. S. Skiena, The Algorithm Design Manual, 3rd ed. Springer, 2020. https://sureshcseit.wordpress.com/wp-content/uploads/2021/04/skienathealgorithmdesignmanual.pdf
[29] B. Bonet and H. Geffner, "Planning as heuristic search," Artificial Intelligence, vol. 129, no. 1-2, pp. 5–33, 2001. https://www.cs.toronto.edu/~sheila/2542/s14/A1/bonetgeffner-heusearch-aij01.pdf
[30] R. C. Holte et al., "Suboptimal search for optimal pathfinding," in IJCAI, 2006.
[31] N. R. Sturtevant, "Benchmarks for grid-based pathfinding," IEEE Transactions on Computational Intelligence and AI in Games, 2012. https://ieeexplore.ieee.org/document/6194296
[32] A. Botea et al., "Near-optimal hierarchical path-finding," JAIR, vol. 21, pp. 1–28, 2004. https://www.researchgate.net/publication/228785110_Near_optimal_hierarchical_path-finding_HPA
[33] A. Patel, "Red Blob Games: Introduction to A* Pathfinding," 2017. [Online]. Available: https://www.redblobgames.com/pathfinding/a-star/introduction.html
[34] The Farama Foundation, "Gymnasium: A standard API for reinforcement learning," 2025. [Online]. Available: https://gymnasium.farama.org/
[35] Matplotlib Development Team, "Matplotlib Animation API," Matplotlib Documentation, 2025. [Online]. Available: https://matplotlib.org/stable/api/animation_api.html
================================================================================
"""
import time
import heapq  # Used for priority queues in pathfinding algorithms like Dijkstra and A* [1]
from collections import deque  # Used for queues in Breadth-First Search (BFS) [2]
import numpy as np  # Used for random number generation and math [3]
import matplotlib.pyplot as plt  # Used for drawing the grid and paths [4]
import matplotlib.animation as animation  # Used for animating search progress [35]

class DeterministicGridWorld:
    # Manages the grid map, randomly places walls, and handles valid moves
    def __init__(self, width=15, height=15, obstacle_prob=None):
        self.width = width
        self.height = height
        
        # Set the starting point at the top-left and the goal at the bottom-right
        self.start = (0, 0)                  
        self.goal = (width - 1, height - 1) # [23]
        
        # Random obstacle density percentage between 12% and 24%
        if obstacle_prob is None:
            self.obstacle_prob = np.random.uniform(0.12, 0.24) # [3]
        else:
            self.obstacle_prob = obstacle_prob
            
        # Store obstacles in a set for fast lookup (checks if a spot is blocked) [15, p. 640; 26]
        self.obstacles = set()  
        
        # Loop through every coordinate on the grid to randomly place obstacles
        for x in range(width):
            for y in range(height):
                pos = (x, y)
                # Don't put walls on the start or finish squares
                if pos != self.start and pos != self.goal:
                    # Roll a random number; if it's lower than the probability, make it a wall
                    if np.random.rand() < self.obstacle_prob: # [3; 20, p. 3]
                        self.obstacles.add(pos)

    def get_neighbors(self, node):
        """
        Given a coordinate (node), this checks all 4 surrounding directions (Up, Down, Left, Right)
        and returns the ones you can actually move to (i.e., inside the grid and not a wall).
        """
        x, y = node
        neighbors = []
        
        # 4-way movement vectors (no diagonal moves allowed) [24]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check 1: Make sure the neighbor is still inside the grid boundaries [15, p. 640]
            if 0 <= nx < self.width and 0 <= ny < self.height:  
                # Check 2: Make sure the spot doesn't have an obstacle on it
                if (nx, ny) not in self.obstacles:
                    # It's a valid move! Add it with a standard movement cost of 1.0 [7; 13]
                    neighbors.append(((nx, ny), 1.0))  
                    
        return neighbors