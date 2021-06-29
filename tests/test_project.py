#!/usr/bin/python3
"""Unit test of the requirements for the proyect in general"""

import unittest
import os


class Test_Proyect(unittest.TestCase):
    """Class to test the proyect"""

    def project(self):
        """Check the proyect requirements:
        - existence of all files and directories in the correct location
        - all the python scripts are executable
        - all the files end in a new line
        - all the files start with a #!/usr/bin/python
        - all the files are written with the pycodestyle standard
        - there is a readme
        - all the modules are documented
        """

        # PEP8
        pep8 = "pep8 --count ."
        self.assertEqual(os.system(pep8), 0)

        flist = ['README.md', 'console.py', 'models',
                 './models/__init__.py', './models/amenity.py',
                 './models/base_model.py', './models/city.py',
                 './models/place.py', './models/review.py',
                 './models/state.py', 'testing.py',
                 './models/user.py']

        for filee in flist:
            # existence of all files and directories in the correct location
            self.assertTrue(os.path.isfile(filee))

            # files are executable
            self.assertTrue(os.access(filee, os.X_OK))

            # first and last line
            with open(filee) as f:
                first = f.readline()
                last = f.read()[-1]
            self.assertTrue(first == '#!/usr/bin/python3\n')
            self.assertTrue(last == '\n')

            # documentation of module
            self.assertTrue(len(filee.__doc__) > 5)

if __name__ == '__main__':
    unittest.main()
