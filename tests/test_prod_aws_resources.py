from bs4 import BeautifulSoup
import argparse
import boto3
import json
import logging
import os
import requests
import unittest

ENVIRON_DEF = "prod"

HOMEPAGE_URL = "https://ryanrigato.com"
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

class WebappLive(unittest.TestCase):
    '''Tests that the aws resources necessary for the webpage are running

        Note that if any of the below unit tests fail,
        The python script will have a non-zero exit code

        This will cause any CodeBuild Builds to fail out

        Preventing the Code Pipeline from continuing to delivery

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

    @unittest.skip("Skipping for now")
    def test_bucket_stack_exists(self,
        stack_name='dev-devdocs-webpage'):
        '''Tests that the templates/static_website stack exists

            Parameters
            ----------
                stack_name : str
                    name of the stack we are checking
            Returns
            -------

            Raises
            ------
        '''
        logging.info("Testing if the website bucket stack exists")


        webpage_stack = describe_stacks_response(
            stack_name=stack_name)

        self.assertEqual(
            webpage_stack['Outputs'][0]['OutputValue'],
            HOMEPAGE_URL
        )
        logging.info("Output url for webpage is correct")





    def test_standards_project(self):
        '''Tests that the /docs/v1/standards/standards.html is alive

            Parameters
            ----------
                request_url : str
                    Url string to send the request to
            Returns
            -------

            Raises
            ------
        '''
        logging.info("Testing if the website is alive")

        standards_test = (
            HOMEPAGE_URL + "/docs/v1/standards/standards.html"
        )
        logging.info(standards_test)

        r = requests.get(standards_test)

        self.assertEqual(r.status_code, 200)
        logging.info("The standards page is live")

if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()

    print(args.integers)
    '''
    unittest.main()
