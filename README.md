# private-accounting
## Overview

Automation scripts for private accounting.

## Build Image

```bash
docker build -t private-accounting .
```

## Quick Start
### Set Env
```bash
cp .env.sample .env
```

#### Environment Variables

- MF_EMAIL: Login email address for MF.
- MF_PASSWORD: Login password for MF.
- LINE_TOKEN: LINE notify token.
- GOOGLE_APPLICATION_CREDENTIALS: Path to google cloud credential file.


### Run Main Script

```bash
docker run --rm --env-file=.env -it -v $(pwd):/usr/src/app private-accounting python -m main
```

### Run Tests

```bash
docker run --rm --env-file=.env -it -v $(pwd):/usr/src/app private-accounting pytest
```

## Run on AWS Lambda
### Build Image for ECR

```bash
aws ecr describe-repositories --region ${AWS_REGION}
```

### Push Image to ECR

```bash
docker push ${REGISTRY_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPOSITORY_NAME}:v1.0
```

### Create Lambda Function

Encrypt env variables by KMS.

```bash
encrypted_mf_email=$(aws kms encrypt --key-id <your_key> --plaintext ${MF_EMAIL} | jq -r .CiphertextBlob)
encrpyted_mf_password=$(aws kms encrypt --key-id <your_key> --plaintext ${MF_PASSWORD} | jq -r .CiphertextBlob)
encrypted_line_token=$(aws kms encrypt --key-id <your_key> --plaintext ${LINE_TOKEN} | jq -r .CiphertextBlob)
```

Create lambda function by aws cli.

```bash
aws lambda create-function \
  --function-name private-accounting \
  --package-type Image \
  --code ImageUri=${REGISTRY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/private-accounting:v1.0 \
  --role arn:aws:iam::${REGISTRY_ID}:role/lambda-private-accounting \
  --environment Variables={ENCRPYTED_MF_EMAIL=${encrpyted_mf_email},ENCRYPTED_MF_PASSWORD=${encrypted_mf_password},ENCRYPTED_LINE_TOKEN=${encrypted_line_token}}
```
