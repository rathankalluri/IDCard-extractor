from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import FileSerializer
from .models import FileMeta
from .ocr import detect_text
from django.conf import settings
import os.path
import os
import json

class ImageParser(APIView):
  """
  Response(JSON)  :
  -----------
  - Name : Name on the ID card
    - ID   : ID on the card(AlphaNumeric) 
    - DOB  : Date of Birth(If any found)
    - Type : Type of card (Aadhar, PAN, Driving Licence, Passport)
    - Issued Date: Issued Date if any

    Please POST an ID card image to the API and make sure that the image is front faced. GET NOT ALLOWED.
  """
  parser_classes = (MultiPartParser, FormParser)
  allowed_methods = ["POST"]
  queryset = FileMeta.objects.all()
  serializer_class = FileSerializer
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      filename = os.path.abspath(os.path.join(settings.MEDIA_ROOT, os.pardir))+file_serializer.data.get('file')
      #extracted_text = extract(filename)
      extracted_text = detect_text(filename)
      os.remove(filename)
      return Response({'Success':'Extraction Successful','extracted_text':extracted_text})
    else:
      return Response({'Error':'File not valid,HTTP_400_BAD_REQUEST'})
  def get(self, request, *args, **kwargs):
    samp_resp = """
    {
    "Success": "SAMPLE JSON",
    "extracted_text": {
        "DOB": "",
        "ID": [
            "CP02920530103272"
        ],
        "Name": "RATNA KUMARK V",
        "IssueDate": [
            "21/03/2017"
        ],
        "Type": "DRIVING_LICENCE"
    }
}
    """
    return Response(json.loads(samp_resp))
