from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=2E8794D2-B9F2-4EF5-8F0C-61AFFEB28585")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."


	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})

def details(request):
	return render(request, 'details.html', {})
