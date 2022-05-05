python -m timeit -s 'from fibonacci_profiling import fibonacci_while' 'fibonacci_while(24)'
python -m timeit -s 'from fibonacci_profiling import fibonacci_recursive' 'fibonacci_recursive(24)'



python3 -m cProfile fibonacci.py