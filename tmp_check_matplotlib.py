import matplotlib, sys
print('MATPLOTLIB_REPR:', matplotlib)
print('HAS_USE:', hasattr(matplotlib, 'use'))
print('USE_ATTRS:', [a for a in dir(matplotlib) if 'use' in a])
print('MODULE_FILE:', getattr(matplotlib, '__file__', None))
print('PYTHON_EXE:', sys.executable)
