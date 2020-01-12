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
        formatted_row : str
            ROW_TEMPLATE populated with project information

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

    logging.info("Creating a link to {}".format(built_html_file))
    """
        Opening local html file for parsing
    """
    with open(built_html_file, "r") as html_file:
        bsObj = BeautifulSoup(html_file, "html.parser")

        """
            formatting the ROW_TEMPLATE
            project_name= <version_number> + " - "
            + h1 text
            ex: v10 - Standards Documentation
            project_description= <p> tag after h1
            href_link=html link
            link_name=corresponds to h1 text
        """
        formatted_row = ROW_TEMPLATE.format(
            project_name=( built_html_file.split('/')[1] +
             " - " + bsObj.find("h1").text),
            project_description=bsObj.find("h1").findNext().text,
            href_link="../" + built_html_file,
            link_name=bsObj.find("h1").text
        )


    logging.info("Formatted table row to return: ")
    logging.info(formatted_row)
    return(formatted_row)

def iterate_markdown(relative_dir="docs/v1/"):
    '''Iterates over all markdown projects within a version

        Parameters
        ----------
        relative_dir : str
            Directory representing the relative placeholder
            for markdown files

        Returns
        -------
        version_rows : str
            html table rows for all projects in a given version

        Raises
        ------
        AE : AssertionError
            AssertionError is raised the proper files are
            not found
    '''
    """

        version_rows = string that contains each
        rows for the html output for a projects within a
        given html version
    """
    formatted_apps_page = APPS_HTML_TEMPLATE
    version_rows = ""

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


                template_wrapper(markdown_file)
                """
                    Appends each row that will be the body
                    of the html table
                """
                version_rows += scrape_built_html(markdown_file)


    logging.info("Formatted version_rows")
    logging.info(version_rows)

    return(version_rows)


def write_apps_index(formatted_apps_page,
    full_html_table,
    ):
    '''Collates built html files into /apps/index.html

        Parameters
        ----------
        formatted_apps_page : str
            Html string that will get formatted by full_html_table
            and written to apps_index_location

        full_html_table : str
            html table body to insert into formatted_apps_page
            string html_table format accessor

        apps_index_location : str
            Directory and filename of where to put
            the project apps overview

        Returns
        -------

        Raises
        ------
        AE : AssertionError
            AssertionError is raised if the version naming
            convention is not followed
    '''
    pass

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
    """
        formatted_apps_page = full html template
        that lists all markdown apps

        full_html_table = string that contains all rows
        for built html, reguardless of documentation version
    """
    formatted_apps_page = APPS_HTML_TEMPLATE
    full_html_table = ""

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
        full_html_table += iterate_markdown(
            docs_dir + version_dir + "/")

    logging.info("full_html_table body: ")
    logging.info(full_html_table)

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
