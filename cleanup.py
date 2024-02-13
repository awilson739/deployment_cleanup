import boto3,click
session = boto3.Session(profile_name='localstack')
s3 = session.resource('s3')
@click.command()
@click.option('--deployments',help="Number of deployments to keep")
@click.option('--bucket', help="S3 Deployment bucket")

def deployment_cleanup(deployments,bucket):
    #get list of objects
    deployment_objects = s3.Bucket(bucket).objects.all()
    #sort objects by last modified
    deletion_list = sorted(deployment_objects, key=lambda key:key.last_modified, reverse=True)[int(deployments):]
    for deployment in deletion_list:
        deployment.delete()


if __name__ == '__main__':
    deployment_cleanup()
