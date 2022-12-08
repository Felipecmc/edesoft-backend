import pandas as pd
import boto3
import os

def readCSV(data):
    
    bucket = data['bucket_name']
    file_name = data['object_key']

    s3 = boto3.client(
        's3',     
        aws_access_key_id=os.environ.ACCESS_KEY,
        aws_secret_access_key=os.environ.SECRET_KEY,
        aws_session_token=os.environ.SESSION_TOKEN
    ) 

    obj = s3.get_object(Bucket= bucket, Key= file_name)

    dataFrame = pd.read_csv(obj['Body'], sep= ';')
    
    list = dataFrame.values.tolist()
    
    return list