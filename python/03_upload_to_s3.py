import boto3
from dotenv import load_dotenv

load_dotenv()
client = boto3.client('s3')

print(client.list_buckets())

Filename = './csv/articles_data.csv'
Bucket = 'template-bucket' # 作成したbucket名に変更する
Key = 'test/articles_data.csv'
client.upload_file(Filename, Bucket, Key)