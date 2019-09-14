import boto3

# Amazon Textract client
textract = boto3.client(
    'textract',
    # Hard coded strings as credentials, not recommended.
    # TODO: Remove hard coded credentials
    aws_access_key_id='AKIA32JYDZ7JVYDOOENO',
    aws_secret_access_key='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', region_name='us-east-1'
)

# Use OCR to retrieve text
def getOCR(document):
    imageBytes = bytearray(document.read())
    return textract.detect_document_text(Document={'Bytes': imageBytes})
