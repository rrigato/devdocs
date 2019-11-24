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


def get_prod_client():
    '''Returns the boto s3 client in the production account

        Parameters
        ----------

        Returns
        -------
        s3_prod_client : client
            Boto3 client for connecting to the production s3
            bucket

        Raises
        ------
    '''
    sts_client = get_boto_clients('sts')

    logging.info("Got the sts client")
    PROD_CROSS_ACCOUNT_ARN = os.environ.get(
    'PROD_CROSS_ACCOUNT_ARN')

    """
        Short term access key id,
        access secret and session token from
        the prod cross account role
    """
    cross_account_credentials = sts_client.assume_role(
        RoleArn=PROD_CROSS_ACCOUNT_ARN,
        RoleSessionName="PROD_DEV_DOCS_CODE_BUILD"
        )

    """
        Uses short term credentials from cross
        account assume role to get an s3 client in the prod account
    """
    s3_prod_client = boto3.client(
        's3',
        aws_access_key_id=(
        cross_account_credentials['Credentials']['AccessKeyId']
        ),
        aws_secret_access_key=(
        cross_account_credentials['Credentials']['SecretAccessKey']
        ),
        aws_session_token=(
        cross_account_credentials['Credentials']['SessionToken']
        )
    )

    logging.info("Got the temporary prod credentials")

    return(s3_prod_client)

def upload_html_file(s3_prod_client):
    '''Uploads html files to s3 static website

        Parameters
        ----------
        s3_prod_client : client
            Boto3 client for connecting to the production s3
            bucket

        Returns
        -------

        Raises
        ------
    '''
    import pdb; pdb.set_trace()

    s3_prod_client.upload_file(
        Filename='docs/v1/standards/standards.html',
        Bucket='ryanrigato.com',
        Key='docs/v1/standards/standards.html',
        ExtraArgs={
            "ContentType":"text/html"
        }
    )



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

    s3_prod_client = get_prod_client()

    """
        According to this documentation:

        https://docs.aws.amazon.com/codebuild/latest/userguide/sample-pipeline-multi-input-output.html

        Any CodeBuild project that gets passed multiple
        input artifacts gets the secondary artifact directory location
        stored in an environment variable using the following
        naming convention:
        $CODEBUILD_SRC_DIR_<yourInputArtifactName>

        $CODEBUILD_SRC_DIR_BuildDev contains the output
        ./docs directory after everything was built in
        the development stage
    """
    artifact_dependency = os.environ.get('')
main()
