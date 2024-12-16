import urllib.request

pyynto = urllib.request.urlopen("https://google.com")
data = pyynto.read()

print(data)


