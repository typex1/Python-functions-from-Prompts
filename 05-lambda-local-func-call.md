# Add this to the end of a Lambda Python function code to run the code outside of Lambda and mock the input request:
```
# This is used for debugging, it will only execute when run locally
if __name__ == "__main__":
    # local debugging, send a simulated event
    local=True
    # TODO 1: Update the event bucket name
    mock_s3_event = {
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
    lambda_handler(mock_s3_event, mock_context)
  ```
