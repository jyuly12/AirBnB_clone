#!/usr/bin/python3
"""Unit test of the requirements for the proyect in general"""

import unittest
import os


class Test_Unittests(unittest.TestCase):
    """Class to test the proyect"""

    def test_unittest(self):
        '''Check the unittest files requirements:
        - existence of all files and directories in the correct location
        - all the python scripts are executable
        - all the files end in a new line
        - all the files start with a #!/usr/bin/python
        - all the files are written with the pycodestyle standard
        - there is a readme
        - all the modules are documented
        - all the classes are documented
        - all the functions are documented
        '''

        self.assertTrue(os.path.isfile('./tests/__init__.py'))
        self.assertTrue(os.path.isfile('./tests/test_models/__init__.py'))

        # P EP8
        pep8 = "pep8 --count ./tests"
        self.assertEqual(os.system(pep8), 0)

        test_list = [
                    './tests/test_test.py',
                    './tests/test_project.py',
                    './tests/test_console.py',
                    './tests/test_models/test_base_model.py',
                    './tests/test_models/test_user.py'
                    ]

        for fil in test_list:
            # Existence of all files and directories in the correct location
            self.assertTrue(os.path.isfile(fil), fil)

            # Files are executable
            self.assertTrue(os.access(fil, os.X_OK), fil)

            # First and last line
            with open(fil) as f:
                first = f.readline()
                last = f.read()[-47:]
                self.assertTrue(first == '#!/usr/bin/python3\n', first)
                line = "if __name__ == '__main__':\n    unittest.main()\n"
                self.assertEqual(last, line, fil)

            # Documentation of module
            self.assertTrue(len(fil.__doc__) > 5, fil)

if __name__ == '__main__':
    unittest.main()
