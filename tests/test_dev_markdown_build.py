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
            success_ind : int
                0 if successful

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
        return(0)

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
                project_result = self.check_project_value(
                    potential_project=potential_project,
                    project_name=project_name
                )

    def test_html_template(self, docs_dir="docs/"):
        '''Tests that each version has an html template

            Parameters
            ----------
            docs_dir : str
                relative path to documentation directory

            Returns
            -------

            Raises
            ------
        '''
        import importlib

        """
            dirs gets all directories in
            the docs folder
        """
        for ver_name in os.listdir(docs_dir):


            """
                next_dir will be like the following examples:
                /docs/v1
                /docs/v10
                etc.
            """
            next_dir = os.path.join(docs_dir, ver_name)
            logging.info("docs directory: ")
            logging.info(next_dir)

            """
                Asserts that the string html_template.py
                is in the list of files in docs/v1
            """
            self.assertTrue(
                "html_template.py" in os.listdir(next_dir)
            )
            """
                Getting all files in the version directory that end
                with .py
                There should only be one python file per documetnation
                directory

            """
            py_files = ([all_files for all_files
                in os.listdir(next_dir)
                if all_files[-3:] =='.py' ])

            self.assertEqual(len(py_files), 1)


    def test_row_template(self):
        '''Tests apps_template import of ROW_TEMPLATE

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''
        from apps.apps_template import ROW_TEMPLATE

        """
            Counts the number of format specifiers for
            the ROW_TEMPLATE <tr> block, could not think of
            a better way to test this
        """
        self.assertEqual(ROW_TEMPLATE.count("{"), 4)
        self.assertEqual(ROW_TEMPLATE.count("}"), 4)
        logging.info("Import of ROW_TEMPLATE string successful")

    @unittest.skip("Skipping for now")
    def test_write_apps_index(self):
        '''Tests apps_template import of ROW_TEMPLATE

            Parameters
            ----------

            Returns
            -------

            Raises
            ------
        '''
        from builds.py.dev_markdown_build import write_apps_index
        os.path.isfile("apps/html_table.html")
        #os.remove("apps/html_table.html")
#for root, dirs, files in os.walk(relative_dir):
if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()

    print(args.integers)
    '''
    unittest.main()
