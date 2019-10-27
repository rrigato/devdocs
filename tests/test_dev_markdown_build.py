import argparse
import json
import logging
import os
import requests
import unittest

ENVIRON_DEF = "dev"

HOMEPAGE_URL = ""
WORKING_DIRECTORY = os.getcwd()

def get_logger():
    '''Returns a boto cloudformation describe_stacks api call
        Parameters
        ----------
        stack_name: str
            Name of the stack

        Returns
        -------
        cf_response : dict
                Dictionary output of the describe_stacks api call

        Raises
        ------
    '''
    """
        Adds the file name to the logs/ directory without
        the extension
    """
    logging.basicConfig(
        filename=os.path.join(WORKING_DIRECTORY, 'logs/',
        os.path.basename(__file__).split('.')[0]),
        format='%(asctime)s %(message)s',
         datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG
         )
    logging.info('\n')


class MarkdownLogic(unittest.TestCase):
    '''Applies code analysis tests corresponding to docuemntation rules

        Ensures that all documentation folders follow appropriate
        naming convention
        Parameters
        ----------

        Returns
        -------

        Raises
        ------
    '''
    @classmethod
    def setUpClass(self):
        '''Unitest function that is run once for the class
            Gets the arguements passed from the user

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''
        get_logger()
        os.sys.path.append(WORKING_DIRECTORY)

    def test_library_imports(self):
        '''Tests that all necessary library dependencies are available

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''
        from docs.v1.v1_template import HTML_TEMPLATE
        from pathlib import Path

    @unittest.skip("Skipping for now")
    def test_version_convention(self):
        '''Tests that all necessary library dependencies are available

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''
        from docs.v1.v1_template import HTML_TEMPLATE
        from pathlib import Path

if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()

    print(args.integers)
    '''
    unittest.main()
