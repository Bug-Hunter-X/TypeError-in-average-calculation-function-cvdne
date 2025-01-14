# Python Code Bug: TypeError in Average Calculation

This repository demonstrates a common error in Python code: handling unexpected input types in functions.  The `calculate_average` function calculates the average of a list of numbers.  The original code attempts to handle an empty list but fails to gracefully handle non-numeric input or incorrect input types.  This can result in a `TypeError`.

The `bug.py` file contains the buggy code. The `bugSolution.py` file provides a corrected version with improved error handling.