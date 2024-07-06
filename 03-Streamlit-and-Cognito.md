Bedrock Claude 3.5 prompt: Write Python code that creates an application in Streamlit and adds authentication using an AWS service.
Sure, here's an example of how you can create a Streamlit application and add authentication using AWS Cognito, which is a service for user authentication and access control:

```python
import streamlit as st
import boto3
from botocore.exceptions import ClientError

# Initialize AWS Cognito client
cognito_idp_client = boto3.client('cognito-idp')

# Cognito User Pool details
USER_POOL_ID = 'your-user-pool-id'
CLIENT_ID = 'your-client-id'

# App title
st.set_page_config(page_title='My Streamlit App')
st.title('My Streamlit App')

# Authentication state
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Login function
def login(username, password):
    try:
        response = cognito_idp_client.initiate_auth(
            ClientId=CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        if response['AuthenticationResult']:
            st.session_state['authenticated'] = True
            st.success('Login successful!')
    except ClientError as e:
        st.error(e.response['Error']['Message'])

# Logout function
def logout():
    st.session_state['authenticated'] = False
    st.success('Logout successful!')

# App content
if st.session_state['authenticated']:
    st.write('Welcome to the app!')
    if st.button('Logout'):
        logout()
else:
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        login(username, password)
```

Here's how the code works:

1. We import the necessary libraries, including `streamlit` for creating the Streamlit app and `boto3` for interacting with AWS services.
2. We initialize the AWS Cognito client using `boto3.client('cognito-idp')`.
3. We define the `USER_POOL_ID` and `CLIENT_ID` for our Cognito User Pool.
4. We set the app title using `st.set_page_config(page_title='My Streamlit App')` and display the main title using `st.title('My Streamlit App')`.
5. We initialize the authentication state in the Streamlit session state using `st.session_state['authenticated'] = False`.
6. We define a `login` function that takes a username and password as input, and uses the `cognito_idp_client.initiate_auth` method to authenticate the user. If the authentication is successful, we set `st.session_state['authenticated'] = True` and display a success message.
7. We define a `logout` function that sets `st.session_state['authenticated'] = False` and displays a success message.
8. In the main app content, we check the authentication state using `if st.session_state['authenticated']`. If the user is authenticated, we display a welcome message and a logout button. If the user is not authenticated, we display input fields for username and password, and a login button.
9. When the user clicks the login button, we call the `login` function with the provided username and password.
10. When the user clicks the logout button, we call the `logout` function.

Note that you'll need to replace `'your-user-pool-id'` and `'your-client-id'` with the actual User Pool ID and Client ID from your AWS Cognito User Pool.

Also, make sure you have the necessary AWS credentials configured on your machine or in the environment where you're running this code. You can do this by setting the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables, or by using an AWS credentials file or an IAM role.