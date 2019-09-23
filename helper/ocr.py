import boto3

# Amazon Textract client
textract = boto3.client(
    'textract',
    # Hard coded strings as credentials, not recommended.
    # TODO: Remove hard coded credentials
    aws_access_key_id="",#add AWS access key here,
    aws_secret_access_key="",#add AWS secret access key here, 
    region_name='us-east-1'
)

# Use OCR to retrieve text
def getOCR(document):
    imageBytes = bytearray(document.read())
    return textract.detect_document_text(Document={'Bytes': imageBytes})
