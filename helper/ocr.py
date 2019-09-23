import boto3

# Amazon Textract client
textract = boto3.client('textract')

# Use OCR to retrieve text
def getOCR(document):
    imageBytes = bytearray(document.read())
    return textract.detect_document_text(Document={'Bytes': imageBytes})
