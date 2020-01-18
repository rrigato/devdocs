import boto3
import glob
import json
import logging
import os
"""
"""
LOG_DIRECTORY = os.environ.get("CODEBUILD_SRC_DIR")

WORKING_DIRECTORY = os.environ.get("CODEBUILD_SRC_DIR_BuildDev")

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
        filename=os.path.join(LOG_DIRECTORY, 'logs/',
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

        file_local_path : str
            relative path to the file we want to upload
            ex: docs/v1/standards/standards.html

        s3_path_key : str
            key and folder structure for uploading file from
            local_path to s3
            ex: docs/v1/standards/standards.html


        Returns
        -------

        Raises
        ------
    '''
    logging.info("Logging local file ")
    logging.info(file_local_path)

    logging.info("To the following s3 location: ")
    logging.info(s3_path_key)

    s3_prod_client.upload_file(
        Filename=file_local_path,
        Bucket='ryanrigato.com',
        Key=s3_path_key,
        ExtraArgs={
            "ContentType":"text/html"
        }
    )
    logging.info("Uploaded the html file")

def iterate_html(relative_dir="docs/v1/", s3_prod_client=None):
    '''Iterates over all html projects within a version

        Parameters
        ----------
        relative_dir : str
            Directory representing the relative placeholder
            for html files

        s3_prod_client : client
            Boto3 client for connecting to the production s3
            bucket


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
                html_file will include relative_path
                as well
                Ex:
                docs/v1/standards/standards.html
            """
            for html_file in glob.glob(relative_path + "*.html"):
                logging.info("Markdown file: ")
                logging.info(html_file)
                #upload_html_file(s3_prod_client)

                """
                    Checking that the name of the html file is
                    equal to the name of one directory up
                    Ex:
                    docs/v1/standards/standards.html
                    standards from .html is equal to standards
                    directory
                """
                if (os.path.basename(html_file).split('.')[0]
                    == doc_directory):
                    upload_html_file(
                        s3_prod_client=s3_prod_client,
                        file_local_path=html_file,
                        s3_path_key=html_file)







def iterate_versions(docs_dir="docs/", s3_prod_client=None):
    '''Calls iterate_html for each version

        Parameters
        ----------
        docs_dir : str
            Directory where all versions of documentation
            are stored

        s3_prod_client : client
            Boto3 client for connecting to the production s3
            bucket

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
            relative_dir = docs_dir + version_dir + "/",
            s3_prod_client=s3_prod_client)


def iterate_apps(apps_dir="apps/",
    file_extensions=('*.html', '*.js', '*.css')):
    '''Iterates over built app directory

        Parameters
        ----------
        apps_dir : str
            Directory where apps overview is stored

        file_extensions : tuple
            file_extensions that you want searched for
            in the apps_dir directory


        Returns
        -------
        apps_files : list
            all files in apps_dir
        Raises
        ------

    '''

    apps_files = []
    """
        Iterates over each of the js, css, and html
        file extensions
        Searches for all files in the apps directory
        for those extension types.

        Adds those files to the apps_files list
    """
    for file_extension in file_extensions:
        apps_files.extend(glob.glob(
            os.path.join(apps_dir, file_extension))
            )

    logging.info("Found the following file extension matches:")
    logging.info(apps_files)

    return(apps_files)

def upload_apps(apps_files, s3_prod_client):
    '''Iterates over built app directory

        Parameters
        ----------
        apps_files : str
            List of files and path for apps overview to
            upload to s3

        s3_prod_client : client
            Boto3 client for connecting to the production s3
            bucket


        Returns
        -------
        apps_files : list
            all files in apps_dir
        Raises
        ------

    '''
    """
        Uploads each html file to s3 from
        the apps_files in the apps directory
    """
    for app_file in apps_files:
        logging.info("Beginning s3 apps file upload")
        upload_html_file(
            s3_prod_client=s3_prod_client,
            file_local_path=app_file,
            s3_path_key=app_file)

    logging.info("Apps file upload complete")

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

    """
        Changing working directory to where the artifacts
        built by CodeBuild in the dev stage are
        located
    """
    os.chdir(WORKING_DIRECTORY)
    s3_prod_client = get_prod_client()


    iterate_versions(docs_dir="docs/",
        s3_prod_client=s3_prod_client)

    apps_files = iterate_apps()

    upload_apps(apps_files=apps_files,
        s3_prod_client=s3_prod_client)
if __name__ == '__main__':
    main()
