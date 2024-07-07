Write a Python function that retrieves all documents of types .pdf, .docx, and .txt from a given S3 bucket, indicating the full S3 key.
Here's a Python function that retrieves all documents of types .pdf, .docx, and .txt from a given S3 bucket, indicating the full S3 key:

```python
import boto3
from botocore.exceptions import ClientError

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
                            's3_key': f's3://{bucket_name}/{key}'
                        })

        return matching_documents

    except ClientError as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    bucket_name = 'your-bucket-name'
    documents = get_documents_from_s3(bucket_name)
    
    for doc in documents:
        print(f"Type: {doc['type']}, S3 Key: {doc['s3_key']}")
```

This function does the following:

1. It uses the boto3 library to interact with AWS S3.

2. It defines a set of target file extensions (.pdf, .docx, .txt).

3. It uses a paginator to handle S3 buckets that might contain more than 1000 objects.

4. For each object in the bucket, it checks if the file extension matches any of the target extensions.

5. If a match is found, it determines the document type based on the file extension.

6. It adds each matching document to a list, including the document type and the full S3 key (in the format s3://bucket-name/key).

7. The function returns the list of matching documents.

8. If an error occurs (e.g., the bucket doesn't exist or the user doesn't have permission), it prints the error and returns an empty list.

To use this function, you would need to have the boto3 library installed and proper AWS credentials configured. You can install boto3 using pip:

```
pip install boto3
```

Make sure you have the necessary permissions to list objects in the S3 bucket you're targeting. You can then call the function by providing the name of your S3 bucket:

```python
bucket_name = 'your-bucket-name'
documents = get_documents_from_s3(bucket_name)

for doc in documents:
    print(f"Type: {doc['type']}, S3 Key: {doc['s3_key']}")
```

This will print out the type and full S3 key for each matching document found in the specified bucket.
