import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from review_analysis_api.settings import GEMINI_API_KEY
# Create your views here.


class ReviewAnalysisAPIView(APIView):
    def post(self, request):
        data = request.data
        response = requests.post(
            f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}',
            data=json.dumps(data), headers={'Content-Type': 'application/json'})

        return Response(response.json(), status=response.status_code)
