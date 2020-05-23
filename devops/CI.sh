#Update code pipeline
aws cloudformation update-stack --stack-name devdocs-pipeline \
 --template-body file://templates/code_pipeline.yml \
 --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
 --parameters ParameterKey=ProdCrossAccountArn,\
 ParameterValue="PROD_CROSS_ACCOUNT_ARN_HERE"
