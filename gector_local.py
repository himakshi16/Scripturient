import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GECTOR_DIR = os.path.join(BASE_DIR, "gector")

if GECTOR_DIR not in sys.path:
    sys.path.insert(0, GECTOR_DIR)
