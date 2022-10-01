from botocore.client import Config
import boto3 as boto3


class S3Manager:
    def __init__(self):
        self.BUCKET = 'organization-torium'
        self.s3 = boto3.client(
            's3',
            region_name='eu-central-1',
            config=Config(signature_version='s3v4')
        )
        self.s3_resource = boto3.resource('s3')

    def get_presigned_url(self, file_name):
        s3_params = {
            'Bucket': self.BUCKET,
            'Key': file_name
        }
        return self.s3.generate_presigned_url(
            'get_object',
            Params=s3_params,
            ExpiresIn=3600
        )
