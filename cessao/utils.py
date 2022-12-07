import pandas as pd
import boto3

def readCSV(data):
    
    bucket = data['bucket_name']
    file_name = data['object_key']

    s3 = boto3.client('s3') 

    obj = s3.get_object(Bucket= bucket, Key= file_name)

    dataFrame = pd.read_csv(obj['Body'])
    
    list = dataFrame.values.tolist()
    
    return list