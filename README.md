## Rush Hour Solver ##   
This is a python rush solver for n x n dimensional "Rush Hour" game board.
Explanation about game rules: https://en.wikipedia.org/wiki/Rush_Hour_(puzzle)#Game

We implemented a BFS inspired algorithm in order to find a shortest possible solution for a given problem. We treated the game as a tree rooted in the starting position, where each level i contains all possible board states i steps from the root.
While posing a difficult task for humans, using this algorithm an optimal solution for a standard 6X6 board can be found within less than a second.
There are 4 available examples for starting game boards of different levels, and the user can choose a level and get a step-by-step solution by the computer.

