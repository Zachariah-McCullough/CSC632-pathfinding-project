# CSC 632: Path Planning & Heuristic Search Benchmark

**Author:** Zachariah Ignatius McCullough  
**Course:** CSC 632 Artificial Intelligence Final Project (Option 1)

Compares **BFS**, **UCS**, **A\* (Manhattan)**, and **A\* (Euclidean)** on 4-connected grids (step cost `1.0`) across `10x10`, `15x15`, `20x20`, and `25x25` sizes, followed by a `15x15` (`obstacle_prob=0.18`) static plot and traversal animation.

## Setup

Requires Python 3.8+ with `numpy` and `matplotlib` (`time`, `heapq`, and `collections.deque` are in the Python standard library):

```bash
pip install numpy matplotlib
```

## Run the Code

```bash
python3 pathfinder.py
```

1. Benchmarks **BFS**, **UCS**, **A\* (Manhattan)**, and **A\* (Euclidean)** on `10x10`, `15x15`, `20x20`, and `25x25` grids and prints path length, nodes expanded, and runtime (ms).
2. Displays a two-panel scaling plot (`Nodes Expanded` and `Execution Time (ms)` vs. grid size). Close the plot window to continue.
3. Runs `A* (Manhattan)` on a `15x15` grid, and opens a static path plot followed by a frame-by-frame animation (or prints that the goal is blocked).

## Reproduce Results

* **Save console output:** `python3 pathfinder.py > results.txt`
* **Fix random layouts:** The script uses unseeded `np.random` calls, so maps and `BLOCKED` cases vary each run. Add `np.random.seed(42)` at the top of `if __name__ == "__main__":` before creating grids to reproduce identical obstacle layouts, path lengths, and node counts (runtimes still vary slightly with CPU load).
