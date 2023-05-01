import boto3
import os
import sys

GB = 1024*1024*1024

def download_dir(s3_folder, local_folder, bucket, client, total_download_size):
    """
    params:
    - s3_folder: folder in s3
    - local_folder: local folder to place files
    - bucket: s3 bucket with target contents
    - client: initialized s3 client object
    """

    # there are 900 model files in the AWS S3 bucket
    downloaded_size = 0
    downloadCnt = 0
    next_token = ''
    base_kwargs = {
        'Bucket':bucket,
        'Prefix':s3_folder,
    }

    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})
        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        for i in contents:
            if downloaded_size >= total_download_size:
                print("model downloaded size reaches the limit.")
                return
            downloadCnt += 1
            k = i.get('Key')
            model_name = k.split('/')[-2]
            model_folder = local_folder+model_name+'/'
            if not os.path.exists(os.path.dirname(model_folder)):
                os.makedirs(os.path.dirname(model_folder))
            model_file = model_folder+k.split('/')[-1]
            if os.path.isfile(model_file):
                downloaded_size += os.path.getsize(model_file)
                print(downloadCnt, model_file, "file already exists.", " total downloaded size:", downloaded_size/GB, "GB")
                continue
            print(downloadCnt, k, 'downloading...', end='')
            client.download_file(bucket, k, model_file)
            downloaded_size += os.path.getsize(model_file)
            print(" total downloaded size:", downloaded_size/GB, "GB")
        next_token = results.get('NextContinuationToken')
    

def main():

    total_download_size = 2048
    try:
        total_download_size = int(sys.argv[1])
        print("Total download size set to:", sys.argv[1], "GB")
    except Exception as e:
        print("All models downloading...")
    #print("total_download_size:", total_download_size)
    #sys.exit()    

    client = boto3.client('s3',
                          aws_access_key_id='AKIAS7X5VN6V27UIKGTD',
                          aws_secret_access_key='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')

    bucket_name = "ds5110-ml-pretrained-models"
    s3_folder = "models/"
    local_folder = "pretrained_models/"
    if not os.path.exists(os.path.dirname(local_folder)):
        os.makedirs(os.path.dirname(local_folder))
    download_dir(s3_folder, local_folder, bucket_name, client, total_download_size*GB)

if __name__ == "__main__":
    main()

