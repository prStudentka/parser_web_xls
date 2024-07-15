from unittest import TestLoader, TextTestRunner


tests = TestLoader().discover('test', pattern='test_*.py')
TextTestRunner(verbosity=2).run(tests)
