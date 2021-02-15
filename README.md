# private-accounting
## Overview

Automation scripts for private accounting.

## Build Image

```bash
docker build -t accounting .
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
docker run --rm --env-file=.env -it -v $(pwd):/usr/src/app accounting python -m main
```

### Run Tests

```bash
docker run --rm --env-file=.env -it -v $(pwd):/usr/src/app accounting pytest
```

## Run on AWS Lambda
### Build Image for ECR

```bash
aws ecr describe-repositories --region ${AWS_REGION}
```

### Push Image to ECR
```
≈docker push ${REGISTRY_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPOSITORY_NAME}:v1.0
```
