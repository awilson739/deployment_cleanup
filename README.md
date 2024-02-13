# deployment_cleanup

This script will remove X amount of old deployments from a bucket. 

## Installation  
`pip3 install -r requirements.txt`

## Usage
`python3 cleanup.py --deployments <integer> --bucket <bucket_name>`

## Assumptions 
1. User who is running the script has appropriate IAM permissions and access
2. This only accounts for last_modified and not that they are different hash
3. Assumes the user, is using the `localstack` AWS profile
