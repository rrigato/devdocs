from bs4 import BeautifulSoup
from pathlib import Path
import boto3
import glob
import importlib
import json
import logging
import os
import subprocess
WORKING_DIRECTORY = os.getcwd()

os.sys.path.append(WORKING_DIRECTORY)

#Needs to be run after the current working directory is
#added to path
from apps.apps_template import APPS_HTML_TEMPLATE
from apps.apps_template import ROW_TEMPLATE

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

def showdown_subprocess(markdown_path):
    '''Calls showdownjs to turn markdown into html

        Parameters
        ----------
        markdown_path : str
            path to the markdown file

        Returns
        -------

        Raises
        ------
        AE : AssertionError
            Raises an assertion error if the
            stder is not empty
    '''
    logging.info("Converting markdown for: " + markdown_path)

    """
        calls the showdown command line utility
        to turn markdown into html

        pass an arguement of shell=True to provide a
        string for bash to run instead of a command
        with arguements passed to the list

    """
    showdown_output = subprocess.run([

        'showdown', 'makehtml', '-i' , markdown_path ,
        '-o' , (str(Path(markdown_path).parent) +
        '/markdown_output.html')
        ],
        capture_output=True
    )
    logging.info(showdown_output)

    """
        Checks that the stderr is empty,
        if it is not we had an error converting the
        markdown to html
    """
    assert showdown_output.stderr.decode() == '',(
        "Unable to convert the markdown to html"
    )
def template_wrapper(markdown_path, version='v1'):
    '''Places the html from showdownjs library into a template file

        Parameters
        ----------
        markdown_path : str
            path to the markdown file

        version : str
            version of the documentation to be released

        Returns
        -------

        Raises
        ------
        AE : AssertionError
            Raises an assertion error if the
            stder is not empty
    '''
    documentation_dir = str(Path(markdown_path).parent)
    """
        Turns a file path into the name of the markdown file
        ex:
            'docs/v1/standards/standards.md'
            to
            'standards'
    """
    html_file_name = os.path.basename(
        markdown_path).split('.')[0]

    logging.info("documentation_dir and html_file_name: ")
    logging.info(documentation_dir)
    logging.info(html_file_name)
    """
        Inserts the converted markdown
        into an html template

        capitalizes the first letter of the project name
        since this is used for the table contents description
        (html_file_name[0].upper() + html_file_name[1:])
    """
    with open(documentation_dir +'/markdown_output.html',
        "r") as converted_markdown:


        """
            imports the module based on the version
            the markdown file is in.
            For ex documentation dir:
            /docs/v1/
        """
        html_module = importlib.import_module(
            (os.path.dirname(documentation_dir).replace("/",".")
            + ".html_template")
            )

        logging.info("Input version specific template")
        output_html = html_module.HTML_TEMPLATE.format(
            project_name=(
                html_file_name[0].upper() + html_file_name[1:]
            ),
            showdown_output=converted_markdown.read()
        )

    logging.info("popultated the output template")
    logging.info(output_html)

    """
        Writes the populated html to
        the documentation folder
    """
    with open((documentation_dir + "/" + html_file_name
        + ".html"), "w") as html_documentation:
        html_documentation.write(output_html)

    logging.info("Wrote the documentation html file")


def scrape_built_html(markdown_path):
    '''Scrapes the built html file to populate ROW_TEMPLATE
        This function will take the project name and
        project description from the a built html file
        The information will be used to populate an index
        of all built markdown projects

        Parameters
        ----------
        markdown_path : str
            path to the markdown file

        Returns
        -------

        Raises
        ------

    '''
    """
        goes from this:
        'docs/v10/standards/standards.md'

        to a str like this:
        'docs/v10/standards/standards.html'
    """
    built_html_file = (markdown_path.split('.')[0]
        + ".html")

    """
        Opening local html file for parsing
    """
    with open(built_html_file, "r") as html_file:
        bsObj = BeautifulSoup(html_file, "html.parser")

    return(ROW_TEMPLATE)

def iterate_markdown(relative_dir="docs/v1/"):
    '''Iterates over all markdown projects within a version

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
        formatted_apps_page = full html template
        that lists all markdown apps

        html_table_body = string that contains each
        row of the html output table that will
        be placed in the html_table string
        specifier of formatted_apps_page
    """
    formatted_apps_page = APPS_HTML_TEMPLATE
    html_table_body = ""

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

            """
                Gets the markdown file
            """
            for markdown_file in glob.glob(relative_path + "*.md"):
                logging.info("Markdown file: ")
                logging.info(markdown_file)
                showdown_subprocess(markdown_file)

                """

                """
                template_wrapper(markdown_file)
                html_table_body += scrape_built_html(markdown_file)



    logging.info("config file after modification: ")

    """
    with open(webpage_config_dir, 'w') as modified_config:
        json.dump(original_file, modified_config, indent=4)
    """

    logging.info("Wrote the new cognito credientials to the config file")



def iterate_versions(docs_dir="docs/"):
    '''Calls iterate_markdown for each version

        Parameters
        ----------
        docs_dir : str
            Directory where all versions of documentation
            are stored

        Returns
        -------

        Raises
        ------
        AE : AssertionError
            AssertionError is raised if the version naming
            convention is not followed
    '''
    all_dirs = os.listdir(docs_dir)

    """
        Iterating over all versions in the
        documentation directory
        this will pass
        /docs/v1/
        /docs/v2/
        etc..
        to iterate_markdown
    """
    for version_dir in all_dirs:
        logging.info("Iterating version ")
        logging.info(docs_dir + version_dir + "/")
        iterate_markdown(
            docs_dir + version_dir + "/")

def main():
    '''Entry point into the script

        Note that the directory structure was validated
        by tests/test_dev_markdown_build.py
        Parameters
        ----------

        Returns
        -------

        Raises
        ------
    '''
    get_logger()

    iterate_versions()


main()
