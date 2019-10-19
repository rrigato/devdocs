import boto3
import json
import logging
import os
import subprocess
WORKING_DIRECTORY = os.getcwd()

def get_logger():
    '''Returns a logger
        Parameters
        ----------
        stack_name: str
            Name of the stack

        Returns
        -------

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



def get_boto_clients(resource_name, region_name='us-east-1'):
    '''Returns the boto client for various cloudformation resources
        Parameters
        ----------
        resource_name : str
            Name of the resource for the client

        region_name : str
                aws region you are using, defaults to
                us-east-1

        Returns
        -------


        Raises
        ------
    '''
    return(boto3.client(resource_name, region_name))


def iterate_markdown(relative_dir="docs/v1/"):
    '''Iterates over all markdown files

        Parameters
        ----------
        relative_dir : str
            Directory representing the relative placeholder
            for markdown files

        Returns
        -------

        Raises
        ------
        AE : AssertionError
            AssertionError is raised the proper files are
            not found
    '''

    """
        dirs, files will be a list of directories/files
        in the relative_dir folders
    """
    for root, dirs, files in os.walk(relative_dir):
        logging.info("Directories found: ")
        logging.info(dirs)
        """
            Iterating over each subdirectory
            with the intent of checking for
            markdown files with extension .md
        """
        for doc_directory in dirs:
            relative_path = relative_dir + doc_directory + "/"
            logging.info("Evaluating relative path: ")
            logging.info(relative_path)
            for markdown_file in glob.glob(relative_dir + "*.md"):
                logging.info("Markdown file: ")
                logging.info(markdown_file)
                import pdb; pdb.set_trace()

    logging.info("config file after modification: ")

    logging.info(original_file)
    """
    with open(webpage_config_dir, 'w') as modified_config:
        json.dump(original_file, modified_config, indent=4)
    """

    logging.info("Wrote the new cognito credientials to the config file")




def main():
    '''Entry point into the script
        Parameters
        ----------

        Returns
        -------

        Raises
        ------
    '''
    get_logger()

    iterate_markdown()


main()
