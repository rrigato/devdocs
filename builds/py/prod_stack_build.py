import boto3
import json
import logging
import os
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

    sts_client = get_boto_clients('sts')

    print(os.environ.get('PROD_CROSS_ACCOUNT_ARN'))

main()
