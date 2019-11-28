import boto3
import glob
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




def upload_html_file(s3_prod_client, file_local_path,
    s3_path_key):
    '''Uploads html files to s3 static website

        Parameters
        ----------
        s3_prod_client : client
            Boto3 client for connecting to the production s3
            bucket

        local_path : str
            relative path to the file we want to upload

        s3_path_key : str
            key and folder structure for uploading file from
            local_path to s3


        Returns
        -------

        Raises
        ------
    '''

    s3_prod_client.upload_file(
        Filename='docs/v1/standards/standards.md',
        Bucket='ryanrigato.com',
        Key='docs/v1/standards/standards.md',
        ExtraArgs={
            "ContentType":"text/html"
        }
    )
    logging.info("Uploaded the html file")

def iterate_html(relative_dir="docs/v1/"):
    '''Iterates over all html projects within a version

        Parameters
        ----------
        relative_dir : str
            Directory representing the relative placeholder
            for html files

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
            text files with extension .html
        """
        for doc_directory in dirs:
            relative_path = relative_dir + doc_directory + "/"
            logging.info("Evaluating relative path: ")
            logging.info(relative_path)

            """
                Gets the html file
            """
            for html_file in glob.glob(relative_path + "*.html"):
                logging.info("Markdown file: ")
                logging.info(html_file)
                upload_html_file
                print(html_file)
                print(os.path.basename(html_file).split('.')[0])
                print(doc_directory)




    logging.info("config file after modification: ")

    """
    with open(webpage_config_dir, 'w') as modified_config:
        json.dump(original_file, modified_config, indent=4)
    """

    logging.info("Wrote the new cognito credientials to the config file")



def iterate_versions(docs_dir="docs/"):
    '''Calls iterate_html for each version

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
        to iterate_html
    """
    for version_dir in all_dirs:
        logging.info("Iterating version ")
        logging.info(docs_dir + version_dir + "/")
        iterate_html(
            docs_dir + version_dir + "/")


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

    upload_html_file(s3_prod_client)

    iterate_versions()
main()
