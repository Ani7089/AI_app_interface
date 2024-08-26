import requests

url = "https://aspect-based-sentiment-analysis.p.rapidapi.com/topic-sentiment"

querystring = {"domain":"generic"}

payload = [
	{
		"id": 1,
		"language": "en",
		"text": "Hello I love the service"
	}
]
headers = {
	"x-rapidapi-key": "ab3c18965amsh855b031cc7b7b75p1761fajsn289e36206d77",
	"x-rapidapi-host": "aspect-based-sentiment-analysis.p.rapidapi.com",
	"Content-Type": "application/json",
	"Accept": "application/json"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())