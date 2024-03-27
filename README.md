# PythonMazeSolver

Overview

This project implements a maze generator and solver using Python and the Tkinter library for visualization. It utilizes a recursive backtracking algorithm for maze generation and employs a similar depth-first search-based approach for solving the maze.

Features

    Maze Generation: Creates procedurally generated mazes with customizable dimensions.
    Maze Solving: Implements a recursive backtracking algorithm to solve generated mazes.
    Visualization: Renders the maze and solution process using Tkinter for a graphical representation.

Installation

    Dependencies:
        Tkinter (Should be included in most standard Python installations)

    Cloning the Repository:
    Bash

    git clone https://github.com/AaronBrownDev/PythonMazeSolver

Usage

    Navigate to the project directory.

    Run the main Python script:
    Bash

    python main.py

    Customization: Adjust parameters within the main.py file to modify maze size, generation seed, and other aspects.

Code Structure

    main.py: The main entry point of the application. Initializes the maze, solver, and visualization components. Handles the program's main loop.
    display.py: Contains Tkinter classes responsible for the graphical display of the maze, along with helper classes (Line, Point) to represent display elements.
    cell.py: The Cell class represents an individual cell within the maze, storing information about its walls and visited state.
    maze.py: Implements the Maze class which handles the maze generation logic (using recursive backtracking) and its solution process (using a depth-first search-inspired approach).
