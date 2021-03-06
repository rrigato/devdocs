# Trailer Utilization
Serverless project used to build a web application to detect trailer utilization from an uploaded image

## Table of contents

- [Dev Tools](#devtools)
    * [cfn-lint](#cfn-lint)
    * [Git Secrets](#gitsecrets)

- [Directory Overview](#directoryoverview)
    * [builds](#builds)
    * [docs](#docs)
    * [devops](#devops)
    * [lambda](#lambda)
    * [logs](#logs)
    * [models](#models)
    * [static](#static)
    * [templates](#templates)
    * [tests](#tests)

## Dev Tools

### cfn-lint
[cfn-lint](https://github.com/aws-cloudformation/cfn-python-lint.git) Provides yaml/json cloudformation validation and checks for best practices

- Install

```
    pip install cfn-lint
```

- Run on a file
```
    cfn-lint <filename.yml>

    cfn-lint templates/code_pipeline.yml
```

- Run on all files in Directory
```
    cfn-lint templates/*.yml
```


### Git Secrets

[git secrets](https://github.com/awslabs/git-secrets.git) is a command line utility for validating that you do not have any git credentials stored in your git repo commit history

This is useful for not only open source projects, but also to make sure best practices are being followed with limited duration credentials (IAM roles) instead of long term access keys

- Global install

```
    git init

    git remote add origin https://github.com/awslabs/git-secrets.git

    git fetch origin

    git merge origin/master

    sudo make install
```

- Web Hook install

Configuring git secrets as a web hook will ensure that git secrets runs on every commit, scanning for credentials
```
    cd ~/Documents/sneakpeek

    git secrets --install

    git secrets --register-aws
```


- Run a git secrets check recursively on all files in directory

```
git secrets --scan -r .
```



## Directory Overview
Provides information on each directory/ source file

### builds
- buildspec_dev.yml = Buildspec to use for the development (QA)
    CodeBuild project

- buildspec_prod.yml = Buildspec to use for the prod deployment CodeBuild project

#### py
    Directory for custom python scripts that setup build configuration


### docs
Used for auto-populated html documentation files for
javascript documentation.js library and python sphinx library


Install and run documentation.js

[documentation.js github](https://github.com/documentationjs/documentation)
```
npm install -g documentation

#build all javascript files
documentation build static/js/** -f html -o docs/js

```

### devops
- CI.sh = Establishes CodeCommit Repo and CodeBuild Project
    - For debugging errors go to the Phase details section of the console
    - Or use the batch-get-builds command in the aws cli

### lambda
- Used to build lambda functions
- Note that each folder can be bundled into a deployment package if it has a dependency other than the standard template libraries or the aws sdk (Boto3)

- Deployment packages = zip archive with lambda function code and dependencies

More on deployment packages can be found here:

https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html


It may be best practice to bundle deployments using code build, as some of the compiled C dependencies may not transfer over on your local even if you are running linux

For example I have had issues in the past with installing pandas on ubuntu, bundling and trying to use in a lambda function.

-t tells pip to install function locally
```
    cd lambda/<project>

    pip install -r requirements.txt -t .


```

### logs
- directory for python log files

### models
- directory for image classification models

### static
- css = static stylesheet files for web application
- fonts = static fonts to use for web application
- js = static javascript files for web application
- images = static images for web applications
- index.html = homepage for web applciation

### templates

- backend.yml = dynamodb, lambda, and api gateway resources

- code_pipeline.yml = Creates CodeBuild/Code Pipeline resources
    necessary for Dev/Prod

- code_pipeline_iam.yml = nested stack for code_pipeline.yml contains iam resources that are used by code_pipeline.yml

Make sure to run the following command before creating a stack with code_pipeline.yml

```
aws s3 cp ./templates s3://sneakpeek-nested-stack --recursive     --exclude "demo*"
```

The reason being that a nested stack has to be in an s3 bucket to be used by the parent

- cognito.yml = user pool and client id to be used for authentication in the webpage

- static_webpage.yml = builds the S3 bucket enabled for web hosting

### tests
- test_dev_aws_resources.py = after the dev environment is spun up in the CodeBuild project for builds/buildspec_dev.yml this script is run to validate deployment of resources.

If any of the test cases fail, the Pipeline stops before deploying to prod


- test_prod_aws_resources.py = test cases run after the prod environment is spun up in the CodeBuild project for builds/buildspec_prod.yml
