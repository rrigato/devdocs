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

    def check_project_value(self,
        potential_project, project_name):
        '''Function wrapper for test_markdown_convention test case

            Validates that a potiential project follows the correct
            Naming conventions

            everything under a given version is passed to
            this function

            Parameters
            ----------
            potential_project : str
                Full Path that could point to a potiential project
                ex: ~/docs/v1/project1_name

            project_name : str
                relative directory
                ex: project1_name

            Returns
            -------

            Raises
            ------
        '''
        """
            Testing to make sure the path object is a directory
            and not hidden/__pycache__ directory
        """
        if (os.path.isdir(potential_project)
            and (project_name[0] not in ['_','.']) ):
            """
                dirs gets all directories in
                the docs folder

                dirs, files will be a list of directories/files
                in the relative_dir folders

                Will walk over all files in the
                /docs/v1/project1_name
                /docs/v1/project2_name
                /docs/v2/project1_name
                etc.
            """
            for root, dirs, files in os.walk(potential_project):

                logging.info("Project files found: ")
                logging.info(files)
                markdown_counter = 0

                """
                    Iterating over all files
                    in a project
                """

                for project_file in files:
                    """
                        Gets the markdown file and makes sure it is
                        named the same as the project folder
                    """

                    if project_file.split('.')[1].lower() == 'md':
                        markdown_counter += 1
                        logging.info("""Ensuring the markdown file
                        is named the same as the project""")
                        self.assertEqual(project_name,
                            project_file.split('.')[0]
                            )


                logging.info("""Making sure we
                 only have one markdown file per project""")
                self.assertEqual(markdown_counter, 1 )

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
        for ver_name in os.listdir(docs_dir):


            next_dir = os.path.join(docs_dir, ver_name)
            logging.info("docs directory: ")
            logging.info(next_dir)

            self.assertTrue(os.path.isdir(
                next_dir
                )
            )


            """
                Iterating over each version
                /docs/v1/
                /docs/v2/
                etc.
            """
            for project_name in os.listdir(next_dir):

                """
                Checking if the subdirectories under
                the version number are a project
                """
                potential_project = os.path.join(
                    docs_dir, ver_name, project_name)
                logging.info("Project directory: ")
                logging.info(potential_project)
                self.check_project_value(
                    potential_project=potential_project,
                    project_name=project_name
                )

if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()

    print(args.integers)
    '''
    unittest.main()
