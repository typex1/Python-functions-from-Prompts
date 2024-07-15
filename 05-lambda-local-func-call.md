# Add this to the end of a Lambda Python function code to run the code outside of Lambda and mock the input request.
* Update the event details as you like.
* If needed, add a global variable "local" to indicate whether the code is run locally or inside of a Lambda function
```
# This is used for debugging, it will only execute when run locally
if __name__ == "__main__":
    # local debugging, send a simulated event
    local=True
    mock_handler_event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "x-thumbnail-input"
                    },
                    "object": {
                        "key": "grand_canyon.jpg"
                    }
                }
            }
        ]
    }

    mock_context = []
    lambda_handler(mock_handler_event, mock_context)
  ```
