import urllib.request

failed = 0
test_urls = []
with open('read.txt') as f:
    test_urls = f.readlines()

for url in test_urls:
	req = urllib.request.Request(url)

	try:
		print('testing url: ' + url)
		resp = urllib.request.urlopen(req).read()
		try:
			if 'Server Error' in resp or '404' in resp or '500' in resp:
				print('Server Error in ' + url)
		except:
			print('could not read response for: ' + url)
			continue
	except urllib.error.HTTPError as e:
		failed += 1
