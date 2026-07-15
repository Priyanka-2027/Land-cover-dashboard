import importlib
import sys
import os

# Ensure project root is on sys.path so imports find local modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import greenery
    print('greenery module file:', getattr(greenery, '__file__', None))
    print('has get_vegetation_statistics:', hasattr(greenery, 'get_vegetation_statistics'))
    print('vegetation-related attrs:', [a for a in dir(greenery) if 'veget' in a.lower()])
except Exception as e:
    print('IMPORT ERROR:', e)
    sys.exit(2)
else:
    sys.exit(0)
