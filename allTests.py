# 2023-2024 Programacao 2 LTI
# Grupo 42
# 60253 Hugo Silva
# 60232 DUarte Correia
import unittest

if __name__ == "__main__":
    # Start the test suite.
    suite = unittest.TestLoader().discover(start_dir='.', pattern='*Tests.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)