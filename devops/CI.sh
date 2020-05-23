#Update code pipeline
aws cloudformation update-stack --stack-name devdocs-pipeline \
 --template-body file://templates/code_pipeline.yml \
 --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
