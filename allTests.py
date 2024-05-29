import unittest

if __name__ == "__main__":
    # Start the test suite.
    suite = unittest.TestLoader().discover(start_dir='.', pattern='*Tests.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)