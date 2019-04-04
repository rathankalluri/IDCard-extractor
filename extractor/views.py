from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(requests):
	return HttpResponse("Hey!! You are on the index page")

@csrf_exempt
def api(requests):
	data = ""
	if requests.method == "POST":
		data = json.loads(requests.body)
	return JsonResponse(data)