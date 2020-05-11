from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=2E8794D2-B9F2-4EF5-8F0C-61AFFEB28585")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."


	if api[0]['Category']['Name'] == "Good":
		category_details = "(0-50) Considered satisfactory"
		category_color = "good"
	elif api[0]['Category']['Name'] == "Moderate":
		category_details = "(51-100) Considered acceptable"
		category_color = "moderate"
	elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
		category_details = "(101-150) Considered less acceptable"
		category_color = "usg"
	elif api[0]['Category']['Name'] == "Unhealthy":
		category_details = "(151-200) Begin to experience health effects"
		category_color = "unhealthy"
	elif api[0]['Category']['Name'] == "Very Unhealthy":
		category_details = "(201-250) Bad weather"
		category_color = "veryunhealthy"
	elif api[0]['Category']['Name'] == "Hazardous":
		category_details = "(251-300) Very bad weather"
		category_color = "hazardous"

	return render(request, 'home.html', {
		'api': api, 
		'category_details': category_details, 
		'category_color' : category_color
		})

def about(request):
	return render(request, 'about.html', {})

def details(request):
	return render(request, 'details.html', {})
