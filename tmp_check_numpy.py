import numpy, sys
print('NUMPY_REPR:', numpy)
print('HAS_VECTORIZE:', hasattr(numpy, 'vectorize'))
print('NUMPY_FILE:', getattr(numpy, '__file__', None))
print('PYTHON_EXE:', sys.executable)
print('Numpy version:', getattr(numpy, '__version__', None))
