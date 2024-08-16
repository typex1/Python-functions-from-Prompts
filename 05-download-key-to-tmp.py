import boto3
import os

def download_s3_file(bucket_name, object_key):
    """
    Download a file from Amazon S3 to the /tmp folder.

    :param bucket_name: Name of the S3 bucket
    :param object_key: Key of the object in the S3 bucket
    :return: Path to the downloaded file
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    # Get the filename from the object key
    filename = os.path.basename(object_key)

    # Create the full path for the download destination
    download_path = os.path.join('/tmp', filename)

    try:
        # Download the file
        s3.download_file(bucket_name, object_key, download_path)
        print(f"File downloaded successfully to {download_path}")
        return download_path
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    bucket = 'android-sync-fsp'
    key = 'tmp/test/2405.13622v1.pdf'
    result = download_s3_file(bucket, key)
    if result:
        print(f"File downloaded to: {result}")
    else:
        print("File download failed.")