# Sudoku Solver

A Sudoku puzzle generator and solver using recursive backtracking with real-time Pygame visualization. Demonstrates constraint satisfaction and algorithm execution step-by-step.

## Features

- Generates random valid Sudoku puzzles (30-40 pre-filled cells)
- Solves using backtracking algorithm with constraint validation
- Real-time visualization showing each step and backtrack
- Console and GUI versions available

## How It Works

The solver uses recursive backtracking:

1. Find next empty cell
2. Try numbers 1-9
3. Check if valid (row, column, 3x3 box constraints)
4. If valid, place number and recurse
5. If dead end, backtrack and try next number

```python
def count_solver(bo) -> bool:
    find = find_zero(bo)
    if not find:
        return True  # Solved
    
    row, col = find
    
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if count_solver(bo):
                return True
            bo[row][col] = 0  # Backtrack
    
    return False
```

## Visual Interface

The Pygame version displays:
- Pre-filled numbers in white cells
- Red box highlighting current cell being evaluated
- Numbers appearing/disappearing as algorithm backtracks
- Bold grid lines separating 3x3 boxes

## Quick Start

```bash
pip install pygame
python game.py        # GUI version with visualization
python sudoku.py      # Console version
```

## Project Structure

```
├── game.py        # Pygame visualization
├── sudoku.py      # Console version
```

## Algorithm Details

- **Time Complexity**: O(9^n) where n = empty cells
- **Space Complexity**: O(n) recursion stack
- **Visualization**: 40ms delay per step, 25ms per backtrack

## What This Demonstrates

- Recursive backtracking algorithm
- Constraint satisfaction problems
- Pygame real-time rendering
- Random puzzle generation

## License

MIT License

## Contact

**Jacob Manhardt**  
📧 jemanhardt@comcast.net  
💼 [LinkedIn](https://www.linkedin.com/in/jacob-manhardt-b9b75025b)  
🐙 [GitHub](https://github.com/manhardt23)

---

*Backtracking algorithm visualization*
