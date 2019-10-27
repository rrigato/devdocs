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


    def test_version_convention(self,
        relative_dir=(WORKING_DIRECTORY + "/docs")):
        '''Tests that all necessary library dependencies are available

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''
        """
            dirs gets all directories in
            the docs folder
        """
        for dir_name in os.listdir(relative_dir):
            logging.info("Testing directory: ")
            logging.info(dir_name)
            """
                Making sure each directory
                starts with the character v and
                then a numeric
            """
            self.assertEqual(dir_name[0], "v")
            self.assertTrue(dir_name[1:].isnumeric())

    def test_markdown_convention(self,
        docs_dir=(WORKING_DIRECTORY + "/docs")):
        '''Tests naming conventions for markdown files
            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''

        """
            dirs gets all directories in
            the docs folder
        """
        for dir_name in os.listdir(docs_dir):
            logging.info("Testing directory: ")
            logging.info(dir_name)
            """
                Iterating over each version
                /docs/v1/
                /docs/v2/
                etc.
            """
            """
                dirs gets all directories in
                the docs folder

                dirs, files will be a list of directories/files
                in the relative_dir folders
            """
            for root, dirs, files in os.walk(markdown_dir):
                logging.info("Directories found: ")
                logging.info(dirs)



if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()

    print(args.integers)
    '''
    unittest.main()
