# Primality Test

This folder contains a small Python 3 script that prompts the user for an integer
and prints whether the number is prime or not.

Usage

1. From this repository root, run:

```bash
cd "Ex5"
python3 primality_test.py
```

2. Enter an integer when prompted. Example:

```
Enter number to test primality: 6
Primality Test Result: Not Prime
```

Notes
- The script requires Python 3.x. There are no external dependencies.
- The algorithm uses trial division and is suitable for numbers up to around 1e10
  in reasonable time. For very large numbers, consider using specialized
  libraries or probabilistic tests (Miller-Rabin).
