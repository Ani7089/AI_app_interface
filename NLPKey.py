import requests
# import json
# #
# # url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"
# #
# querystring = {"text":"great value in its price range!"}
# #
# # headers = {
# # 	"X-RapidAPI-Key": "ab3c18965amsh855b031cc7b7b75p1761fajsn289e36206d77",
# # 	"X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
# # }

# txt = {
# 	'Positive' : 0.11,
# 	'Negative' : 0.77,
# 	'Neutral' : 0.88
# }

# f = open('sample.json', 'w')
# json.dump(txt, f)
# f.close()


class NLPRequest :
	def __init__(self, text):
		self.text = text




	def re(self):

		url = "https://aspect-based-sentiment-analysis.p.rapidapi.com/topic-sentiment"

		querystring = {"domain": "generic"}

		payload = [
			{
				"id": 1,
				"language": "en",
				"text": self.text
			}
		]
		headers = {
			"x-rapidapi-key": "ab3c18965amsh855b031cc7b7b75p1761fajsn289e36206d77",
			"x-rapidapi-host": "aspect-based-sentiment-analysis.p.rapidapi.com",
			"Content-Type": "application/json",
			"Accept": "application/json"
		}

		response = requests.post(url, json=payload, headers=headers, params=querystring)

		print(response)

		# with open(self.val) as user_file:
		# 	file_contents = user_file.read()
		# return file_contents


# # print(response.json())


	# import requests
	#
	# url = "https://aspect-based-sentiment-analysis.p.rapidapi.com/topic-sentiment"
	#
	# querystring = {"domain":"generic"}
	#
	# payload = [
	# 	{
	# 		"id": 1,
	# 		"language": "en",
	# 		"text": "Hello I love the service"
	# 	}
	# ]
	# headers = {
	# 	"x-rapidapi-key": "ab3c18965amsh855b031cc7b7b75p1761fajsn289e36206d77",
	# 	"x-rapidapi-host": "aspect-based-sentiment-analysis.p.rapidapi.com",
	# 	"Content-Type": "application/json",
	# 	"Accept": "application/json"
	# }
	#
	# response = requests.post(url, json=payload, headers=headers, params=querystring)
	#
	# print(response.json())