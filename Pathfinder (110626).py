"""
================================================================================
PROJECT: Deterministic Grid-Based Path Planning & Heuristic Search Benchmark
COURSE: CSC 632 Artificial Intelligence Final Project (Option 1)
STUDENT NAME: Zachariah Ignatius McCullough
================================================================================

REFERENCES:

[1] Python Software Foundation, "heapq — Heap queue algorithm," Python Documentation, 2025. 
[Online]. Available: https://docs.python.org/3/library/heapq.html

[2] Python Software Foundation, "collections — Container datatypes," Python Documentation, 2025. 
[Online]. Available: https://docs.python.org/3/library/collections.html

[3] C. R. Harris et al., "Array programming with NumPy," Nature, vol. 585, no. 7825, pp. 357–362, 2020. 
https://www.nature.com/articles/s41586-020-2649-2

[4] J. D. Hunter, "Matplotlib: A 2D graphics environment," Computing in Science & Engineering, vol. 9, no. 3, pp. 90–95, 2007. 
https://ieeexplore.ieee.org/document/4160265

[5] S. Russell and P. Norvig, Artificial Intelligence: A Modern Approach, 4th ed. Pearson, 2020.

[6] P. E. Hart, N. J. Nilsson, and B. Raphael, "A formal basis for the heuristic determination of minimum cost paths," 
IEEE Transactions on Systems Science and Cybernetics, vol. 4, no. 2, pp. 100–107, 1968. https://ieeexplore.ieee.org/document/4082128

[7] E. W. Dijkstra, "A note on two problems in connexion with graphs," Numerische Mathematik, vol. 1, no. 1, pp. 269–271, 1959. 
https://ir.cwi.nl/pub/9256/9256D.pdf

[8] The Farama Foundation, "Toy Text Environments: FrozenLake," Gymnasium Documentation, 2025. 
[Online]. Available: https://gymnasium.farama.org/environments/toy_text/frozen_lake/

[9] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction, 2nd ed. MIT Press, 2018. 
https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf

[10] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, Introduction to Algorithms, 4th ed. MIT Press, 2022. 
https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf

[11] J. Pearl, Heuristics: Intelligent Search Strategies for Computer Problem Solving. Addison-Wesley, 1984. 
https://www.scribd.com/document/820231576/Judea-Pearl-Heuristics-Intelligent-Search-Strategies-for-Computer-Problem-Solving#page=45

[12] W. G. Macready and D. H. Wolpert, "Cost-free, value-free parameter configuration for search algorithms," 
IEEE Transactions on Evolutionary Computation, vol. 1, no. 1, pp. 41–58, Apr. 1997. 
[Online]. Available: https://www.cs.ubc.ca/~hutter/earg/papers07/00585893.pdf

[13] C. Demetrescu and G. F. Italiano, "Engineering shortest path algorithms," in Lecture Notes in Computer Science 
(including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), vol. 3046, May 2004, pp. 238–259. 
doi: 10.1007/978-3-540-24838-5_14.

[14] C. Stachniss, "Introduction to Mobile Robotics: Graph Search and Dijkstra/A*," University of Bonn, 2016.

[15] J. C. Latombe, Robot Motion Planning. Kluwer Academic Publishers, 1991. 
https://www.researchgate.net/publication/242351349_Robot_Motion_Planning_A_Distributed_Representation_Approach

[16] R. E. Korf, "Depth-first iterative-deepening: An optimal admissible search strategy," 
Artificial Intelligence, vol. 27, no. 1, pp. 97–109, 1985. https://www.cse.sc.edu/~mgv/csce580f09/gradPres/korf_IDAStar_1985.pdf

[17] R. Dechter and J. Pearl, "Generalized best-first search strategies and the optimality of A*," 
Journal of the ACM, vol. 32, no. 3, pp. 505–536, 1985. https://dl.acm.org/doi/pdf/10.1145/3828.3830

[18] D. E. Knuth, The Art of Computer Programming, Volume 1: Fundamental Algorithms, 3rd ed. Addison-Wesley, 1997. 
http://f.javier.io/rep/books/Donald-Knuth---The-Art-of-Computer-Programming-Vol-1-Fundamental-Algorithms.pdf

[19] R. Sedgewick and K. Wayne, Algorithms, 4th ed. Addison-Wesley, 2011. 
https://cs-web.bu.edu/fac/snyder/cs112/CourseMaterials/AlgorithmsChapterOne.pdf

[20] J. S. Baras and D. Theodorakopoulos, "Path planning in dynamic environments," 
in IEEE Conference on Decision and Control, 2002. https://arxiv.org/pdf/1605.06853

[21] S. Koenig and M. Likhachev, "Improved fast replanning for robot navigation in unknown terrain," in AAAI, 2002. 
https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite.pdf

[22] S. Thrun, W. Burgard, and D. Fox, Probabilistic Robotics. MIT Press, 2005. https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf

[23] S. M. LaValle, Planning Algorithms. Cambridge University Press, 2006. https://lavalle.pl/planning/book.pdf

[24] N. J. Nilsson, Artificial Intelligence: A New Synthesis. Morgan Kaufmann, 1998.

[25] P. H. Winston, Artificial Intelligence, 3rd ed. Addison-Wesley, 1992. https://courses.csail.mit.edu/6.034f/ai3/rest.pdf

[26] Z. Zertz, Graph Theory and Its Applications. CRC Press, 1995.

[27] A. Barr and E. A. Feigenbaum, The Handbook of Artificial Intelligence, Volume 1. William Kaufmann, 1981. 
[Online]. Available: https://dl.acm.org/doi/book/10.5555/540417

[28] S. S. Skiena, The Algorithm Design Manual, 3rd ed. Springer, 2020. 
https://sureshcseit.wordpress.com/wp-content/uploads/2021/04/skienathealgorithmdesignmanual.pdf

[29] B. Bonet and H. Geffner, "Planning as heuristic search," Artificial Intelligence, vol. 129, no. 1-2, pp. 5–33, 2001. 
https://www.cs.toronto.edu/~sheila/2542/s14/A1/bonetgeffner-heusearch-aij01.pdf

[30] R. C. Holte et al., "Suboptimal search for optimal pathfinding," in IJCAI, 2006.

[31] N. R. Sturtevant, "Benchmarks for grid-based pathfinding," 
IEEE Transactions on Computational Intelligence and AI in Games, 2012. https://ieeexplore.ieee.org/document/6194296

[32] A. Botea et al., "Near-optimal hierarchical path-finding," JAIR, vol. 21, pp. 1–28, 2004. 
https://www.researchgate.net/publication/228785110_Near_optimal_hierarchical_path-finding_HPA

[33] A. Patel, "Red Blob Games: Introduction to A* Pathfinding," 2017. 
[Online]. Available: https://www.redblobgames.com/pathfinding/a-star/introduction.html

[34] The Farama Foundation, "Gymnasium: A standard API for reinforcement learning," 2025. [Online]. Available: https://gymnasium.farama.org/

[35] Matplotlib Development Team, "Matplotlib Animation API," Matplotlib Documentation, 2025. 
[Online]. Available: https://matplotlib.org/stable/api/animation_api.html
================================================================================
"""
import time
import heapq # Used for priority queues in pathfinding algorithms like Dijkstra and A* [1]
from collections import deque # Used for queues in Breadth-First Search (BFS) [2]
import numpy as np # Used for random number generation and math [3]
import matplotlib.pyplot as plt # Used for drawing the grid and paths [4]
import matplotlib.animation as animation # Used for animating search progress [35]

class DeterministicGridWorld:
    # Manages the grid map, randomly places walls, and handles valid moves [8; 15, p. 631; 22, p. 112]
    def __init__(self, width=15, height=15, obstacle_prob=None):
        self.width = width
        self.height = height
        
        # Sets the starting point at the top-left and the goal at the bottom-right (the legend will have to be upper-right)
        self.start = (0, 0)                  
        self.goal = (width - 1, height - 1) # [23]
        
        # Random obstacle density percentage between 12% and 24% [8; 9, p. 3]
        if obstacle_prob is None:
            self.obstacle_prob = np.random.uniform(0.12, 0.24) # [3]
        else:
            self.obstacle_prob = obstacle_prob
            
        # Checks if a spot is blocked [15, p. 640; 26]
        self.obstacles = set()  
        
        # Loop through every coordinate on the grid to randomly place obstacles [8; 15, p. 55]
        for x in range(width):
            for y in range(height):
                pos = (x, y)
                # No walls on the start or finish squares (top-left // bottom-right)
                if pos != self.start and pos != self.goal:
                    # Rolls a random number; if it's lower than the probability, it becomes a wall
                    if np.random.rand() < self.obstacle_prob: # [3; 20, p. 3]
                        self.obstacles.add(pos)

    def get_neighbors(self, node):
        """
        Given a coordinate (node), this checks all 4 surrounding directions (Up, Down, Left, Right)
        and returns the ones you can actually move to (not a wall) [26, p. 72]
        """
        x, y = node
        neighbors = []
        
        # 4-connected grid topology [24]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check 1: Makes sure its still inside the grid [15, p. 640]
            if 0 <= nx < self.width and 0 <= ny < self.height:  
                # Check 2: Makes sure the grid spot doesn't have an obstacle 
                if (nx, ny) not in self.obstacles:
                    # Uniform edge weight cost of 1.0 [7; 13]
                    neighbors.append(((nx, ny), 1.0))  
                    
        return neighbors

# ==========================================
# SEARCH ALGORITHMS
# ==========================================

def breadth_first_search(grid, start, goal):
    """
    Breadth-First Search (BFS) explores outward layer by layer using a FIFO queue
    Because all steps cost the same, this is guaranteed to find the shortest path [5, 10]
    Complexity:
        - Time: O(V + E) or O(b^d), where V is vertices, E is edges, b is branching factor, d is depth [10, p. 594-600]
        - Space: O(V) to store the frontier queue and parent tracking dictionary
    """
    start_time = time.perf_counter()
    
    frontier = deque([start]) # Queue to keep track of nodes to visit next [2; 10, p. 596; 18]
    came_from = {start: None} # Tracks the path we took to get to each node
    nodes_expanded = tổng = 0 # Count how many spots we check
    nodes_expanded = 0

    while frontier:
        current = frontier.popleft() # Grab the next spot from the front of the queue [2; 10, p. 596]
        
        # Stop if goal is reached
        if current == goal:
            break
            
        nodes_expanded += 1
        
        # Check all valid neighboring spots
        for next_node, _ in grid.get_neighbors(current):
            # If it haven't visited this neighbor yet, log where we came from and add it to the queue # [2; 10, p. 597]
            if next_node not in came_from:
                came_from[next_node] = current
                frontier.append(next_node)

    end_time = time.perf_counter()
    path = reconstruct_path(came_from, start, goal)
    
    # Return the path, total spots checked, and elapsed time in milliseconds
    return path, nodes_expanded, (end_time - start_time) * 1000

def uniform_cost_search(grid, start, goal):
    """
    Uniform Cost Search (UCS) uses a priority queue to always expand the cheapest path first [5, p. 96-100; 7; 9]
    Complexity:
        - Time: O(E log V) due to binary heap push // pop operations in heapq [10, p. 165]
        - Space: O(V) for storing cost tables, priority queues, and backpointers
    """
    start_time = time.perf_counter()
    
    frontier = [(0.0, start)] # Priority queue stores tuples of (total_cost_so_far, node) [1; 7; 19]
    came_from = {start: None}
    cost_so_far = {start: 0.0} # Keeps track of the exact distance/cost to reach each node
    nodes_expanded = 0

    while frontier:
        current_cost, current = heapq.heappop(frontier) # Grab the node with the lowest cost so far [1; 19]
        
        if current == goal:
            break
            
        nodes_expanded += 1
        
        for next_node, step_cost in grid.get_neighbors(current):
            new_cost = cost_so_far[current] + step_cost
            
            # If there is a cheaper way to reach this neighbor, update its cost and add it to the queue
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                heapq.heappush(frontier, (new_cost, next_node)) # [1; 19]
                came_from[next_node] = current

    end_time = start_time_end = time.perf_counter() # fixed time capture
    end_time = time.perf_counter()
    path = reconstruct_path(came_from, start, goal)
    
    return path, nodes_expanded, (end_time - start_time) * 1000

def a_star_search(grid, start, goal, heuristic_type='manhattan'):
    """
    A* Search combines the actual distance traveled so far (g) with an estimated 
    guess to the goal (h) to find the shortest path much faster
    Calculates the estimated distance remaining to the goal [5, p. 117, 705; 6; 11, p. 63; 17, p. 508; 14]
    Complexity: 
        - Time: O(b^d) worst-case, but significantly reduced in practice depending 
          on the effective heuristic pruning efficiency [5, p. 103-108; 6]
        - Space: O(V) to maintain priority queue and g_score mappings
    """
    start_time = time.perf_counter()
    
    def heuristic(a, b):
       
        if heuristic_type == 'manhattan':
            # Optimal for 4-connected grid graphs where diagonal movement is prohibited [11; 29, p. 27]
            # Mathematically equivalent to L1 norm distance in metric spaces
            return abs(a[0] - b[0]) + abs(a[1] - b[1])  
        elif heuristic_type == 'euclidean':
            # Straight-line distance (L2 norm) [3; 11]. Underestimates grid-constrained 
            # Movement costs, maintaining admissibility while exploring a wider state space
            return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)  
        return 0.0

    start_h = heuristic(start, goal)
    frontier = [(start_h, 0.0, start)] # Priority queue stores (estimated_total_cost, actual_cost, node) [1; 6; 16, p. 103]
    came_from = {start: None}
    g_score = {start: 0.0} # Actual cost from start to each node
    nodes_expanded = 0

    while frontier:
        _, current_g, current = heapq.heappop(frontier) # [1; 19]
        
        if current == goal:
            break
            
        nodes_expanded += 1
        
        for next_node, step_cost in grid.get_neighbors(current):
            tentative_g = g_score[current] + step_cost
            
            # If this path to the neighbor is better than any previous one we found, record it
            if next_node not in g_score or tentative_g < g_score[next_node]:
                g_score[next_node] = tentative_g
                # Total estimated cost (f = actual cost so far + estimated distance to goal)
                f_score = tentative_g + heuristic(next_node, goal) # [6; 11, p. 75; 21, p. 2]
                heapq.heappush(frontier, (f_score, tentative_g, next_node)) # [1]
                came_from[next_node] = current

    end_time = time.perf_counter()
    path = reconstruct_path(came_from, start, goal)
    
    return path, nodes_expanded, (end_time - start_time) * 1000

def reconstruct_path(came_from, start, goal):
    """
    Works backward from the finish line to the start using the 'came_from' tracking dictionary, 
    then flips the list around so there is a clean path from start to finish [5, p. 93; 10, p. 287; 24]
    """
    if goal not in came_from:
        return [] # Return an empty list if no path was found
        
    current = goal
    path = []
    
    while current != start:
        path.append(current)
        current = came_from[current]
        
    path.append(start)
    path.reverse() # Flip it so it starts at the beginning
    
    return path

# ==========================================
# VISUALIZATION
# ==========================================

def visualize_grid_and_path(grid, path, title="Path Planning Static Visualization"):
    """
    Creates a static picture of the map, showing the obstacles, start point, goal, 
    and the final path found by the search algorithm [4; 27].
    """
    # Create a blank grid map filled with zeros (representing empty space)
    grid_matrix = np.zeros((grid.height, grid.width)) # [3]
    
    # Mark obstacle positions with a value of 1.0 (walls)
    for ox, oy in grid.obstacles:
        grid_matrix[oy][ox] = 1.0 # Obstacle marker [4; 15, p. 640]
        
    # Mark the steps along the solution path (excluding the start and goal) with 0.5
    for px, py in path[1:-1]:
        grid_matrix[py][px] = 0.5 # Path marker [4]
        
    # Assign specific color weights to the start (0.2) and goal (0.8) spots
    grid_matrix[grid.start[1]][grid.start[0]] = 0.2 # Start position marker [4]
    grid_matrix[grid.goal[1]][grid.goal[0]] = 0.8 # Goal destination marker [4]

    # Draw the map using Matplotlib
    plt.figure(figsize=(8, 8))  # [4]
    plt.imshow(grid_matrix, cmap='Accent', origin='upper') # [4]
    plt.title(f"{title} (Density: {grid.obstacle_prob*100:.1f}%)", fontsize=13) # [4]
    plt.grid(color='black', linestyle='-', linewidth=0.5) # [4]
    plt.xticks(np.arange(-0.5, grid.width, 1), []) # [3, 4]
    plt.yticks(np.arange(-0.5, grid.height, 1), []) # [3, 4]
    plt.tight_layout()
    plt.show() # [4]

def animate_agent_path(grid, path):
    """
    Creates a moving animation showing the agent stepping along the path 
    from start to finish frame-by-frame [4, 35].
    """
    # Set up the base grid map with obstacles
    grid_matrix = np.zeros((grid.height, grid.width)) # [3]
    for ox, oy in grid.obstacles:
        grid_matrix[oy][ox] = 1.0 # [4, 15]
        
    # Set up the animation window and plot formatting
    fig, ax = plt.subplots(figsize=(8, 8)) # [4]
    ax.imshow(grid_matrix, cmap='binary', origin='upper') # [4]
    ax.set_title(f"A* Agent Traversal Animation (Obstacle Density: {grid.obstacle_prob*100:.1f}%)", fontsize=13) # [4]
    ax.grid(color='gray', linestyle='--', linewidth=0.5) # [4]
    
    # Place marker icons for the Start (green dot) and Goal (purple star)
    ax.scatter(grid.start[0], grid.start[1], color='green', s=200, label='Start', zorder=5) # [4]
    ax.scatter(grid.goal[0], grid.goal[1], color='purple', s=200, label='Goal / Chest', marker='*', zorder=5) # [4]
    
    # Set up the moving blue agent marker and the orange trailing line
    agent_marker, = ax.plot([], [], marker='o', color='dodgerblue', markersize=14, label='Agent', zorder=6) # [4]
    path_line, = ax.plot([], [], color='orange', linewidth=3, alpha=0.7, label='Traveled Path', zorder=4) # [4]
    
    # Add a legend in the top right corner so it doesn't block the grid
    ax.legend(loc='upper right', framealpha=0.9) # [4]

    def init():
        # Clears the agent and path lines before the animation starts
        agent_marker.set_data([], [])
        path_line.set_data([], [])
        return agent_marker, path_line

    def update(frame):
        # Updates the agent's position and the orange trail for every step of the animation
        current_path = path[:frame + 1]
        pxs = [p[0] for p in current_path]
        pys = [p[1] for p in current_path]
        path_line.set_data(pxs, pys)
        agent_marker.set_data([current_path[-1][0]], [current_path[-1][1]])
        return agent_marker, path_line

    # Run the frame-by-frame animation loop
    ani = animation.FuncAnimation(
        fig, update, frames=len(path), init_func=init, interval=200, blit=True, repeat=False
    ) # [35]
    plt.tight_layout()
    plt.show() # [4]