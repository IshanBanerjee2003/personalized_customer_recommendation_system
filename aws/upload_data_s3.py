import boto3
import yaml

# Load AWS configuration
with open('aws/aws_config.py') as file:
    aws_config = yaml.safe_load(file)

# Initialize AWS S3 client
s3 = boto3.client('s3', region_name=aws_config['region'])

# Upload dataset to S3
bucket_name = aws_config['s3_bucket']
file_name = 'dataset/processed/user_product_interactions_processed.csv'

s3.upload_file(file_name, bucket_name, 'user_product_interactions_processed.csv')
print(f"{file_name} uploaded to S3 bucket {bucket_name}")
