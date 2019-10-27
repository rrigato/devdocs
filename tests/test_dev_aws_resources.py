from bs4 import BeautifulSoup
import argparse
import boto3
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

    @unittest.skip("SKipping for now")
    def test_home_page(self):
        '''Tests that the aws resources necessary for the webpage are running

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
        r = requests.get(
            HOMEPAGE_URL
        )
        self.assertEqual(r.status_code, 200)
        logging.info("The website is live")



    @unittest.skip("SKipping for now")
    def test_ssm_parameters(self, parameter_dict={
        "/dev/UserPoolClientId":"Default",
        "/dev/IdentityAuthorizedRoleArn":"Default",
        "/dev/IdentityPoolId":"Default",
        "/dev/UserPoolId":"Default"
        }):
        '''Tests the ssm parameters store values are not Default

            These parameters are dynamically populated
            When they are created in the cloudformation script
            They have a value of Default.

            CodeBuild populates these parameters in
            the build stage

            Parameters
            ----------
            parameter_dict : dict
                Key value pair where the key is the
                ssm parameter name and the value is
                what we expect the ssm parameter to be


            Returns
            -------

            Raises
            ------
        '''
        """
            Gets the boto client for parameter store
            and tests the value of various parameters
        """
        ssm_client = get_boto_clients('ssm')

        logging.info("Got the boto client for ssm")
        """
            Iterating over each key/value in the dict
            to compare parameter store values
        """
        for ssm_name in parameter_dict.keys():

            logging.info("Comparing the following parameter: ")
            logging.info(ssm_name)
            logging.info(parameter_dict[ssm_name])

            """
                Gets the parameter value
                And tests to make sure it is not the
                same as the Value provided for the test
                as that is presumably the default value

                That should be overriden at build time
            """
            ssm_value = ssm_client.get_parameter(
                Name=ssm_name
            )
            self.assertNotEqual(
                ssm_value['Parameter']['Value'],
                parameter_dict[ssm_name]
             )

            logging.info("To this ssm value: ")
            logging.info(ssm_value)

    @unittest.skip("SKipping for now")
    def test_ssm_static_param(self, parameter_dict={
        "/dev/BucketName":"dev-sneakpeek",
        "/dev/NamePrefix":"dev"
        }):
        '''Tests the ssm parameters store values that are static

            These parameters are static only populated at

            development time

            Parameters
            ----------
            parameter_dict : dict
                Key value pair where the key is the
                ssm parameter name and the value is
                what we expect the ssm parameter to be


            Returns
            -------

            Raises
            ------
        '''
        """
            Gets the boto client for parameter store
            and tests the value of various parameters
        """
        ssm_client = get_boto_clients('ssm')

        logging.info("Got the boto client for ssm")
        """
            Iterating over each key/value in the dict
            to compare parameter store values
        """
        for ssm_name in parameter_dict.keys():

            logging.info("Comparing the following parameter: ")
            logging.info(ssm_name)
            logging.info(parameter_dict[ssm_name])

            """
                Tests to make sure static parameters are
                the same
            """
            ssm_value = ssm_client.get_parameter(
                Name=ssm_name
            )
            self.assertEqual(
                ssm_value['Parameter']['Value'],
                parameter_dict[ssm_name]
             )

            logging.info("To this ssm value: ")
            logging.info(ssm_value)

if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()

    print(args.integers)
    '''
    unittest.main()
