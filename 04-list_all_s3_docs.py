import boto3
from botocore.exceptions import ClientError
import re

def get_documents_from_s3(bucket_name):
    """
    Retrieves all documents of types .pdf, .docx, and .txt from a given S3 bucket.

    Args:
    bucket_name (str): The name of the S3 bucket to search.

    Returns:
    list: A list of dictionaries containing the document type and full S3 key for each matching document.
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # List to store the matching documents
    matching_documents = []

    # Set of file extensions we're looking for
    target_extensions = {'.pdf', '.docx', '.txt'}

    try:
        # Use paginator to handle buckets with more than 1000 objects
        paginator = s3_client.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=bucket_name)

        for page in page_iterator:
            if 'Contents' in page:
                for obj in page['Contents']:
                    key = obj['Key']
                    # Check if the file extension matches any in our target set
                    if any(key.lower().endswith(ext) for ext in target_extensions):
                        # Determine the document type
                        if key.lower().endswith('.pdf'):
                            doc_type = 'PDF'
                        elif key.lower().endswith('.docx'):
                            doc_type = 'DOCX'
                        elif key.lower().endswith('.txt'):
                            doc_type = 'TXT'
                        else:
                            doc_type = 'Unknown'

                        # Add the document info to our list
                        matching_documents.append({
                            'type': doc_type,
                            #'s3_key': f's3://{bucket_name}/{key}'
                            's3_key': f'{key}'
                        })

        return matching_documents

    except ClientError as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    bucket_name = 'android-sync-fsp'
    documents = get_documents_from_s3(bucket_name)
    print("raw: {}".format(documents))
    n = 1
    for doc in documents:
        #print(f"{n}. Type: {doc['type']}, S3 Key: {doc['s3_key']}")
        #path = doc['s3_key'].split("/")[2:]
        path = str(doc['s3_key'])
        print(f"{n}. {path}")
        n += 1
    print("one of the entries: {}".format(documents[2]['s3_key']))
