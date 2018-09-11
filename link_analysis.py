import json
import matplotlib.pyplot as plt
import urllib.parse

#This is just a demo analysis.


def getOrgUrl(url):
	#From @url, a long/full url, returns the netloc as the org-url; e.g. 'https://www.nytimes.com/2018/09/10/climate/methane-emissions-epa.html' returns 'www.nytimes.com'
	#returns None if parse fails
	orgUrl = None
	try:
		orgUrl = urllib.parse.urlparse(url).netloc
	except:
		pass
	return orgUrl

def buildLinkHistogram(headlines, dedupe=True):
	#Get a link histogram, mapping org-url to its link frequency
	#@dedupe: If True, then count full urls only once. I don't any case that you'd want this to be false.
	hist = dict()

	for headline in headlines:
		orgUrl = getOrgUrl(headline["uri"])
		if orgUrl not in hist.keys():
			hist[orgUrl] = 1
		else:
			hist[orgUrl] += 1

	return hist

def plotLinkDistribution(headlines, title):
	#Build a histogram of the link distribution for @headlines, mapping org sites (net location) to link frequency
	hist = buildLinkHistogram(headlines, dedupe=True)
	#Sort histogram in descending order of link frequency
	hist = sorted(hist.items(), key=lambda t: t[1], reverse=True)
	#plot only the top 30 sources
	ys = [pair[1] for pair in hist[0:30]]
	#get the org labels, strippping out url boilerplate like 'www' and '.com'
	xlabels = [pair[0].replace("www.","").replace(".com","").replace(".org","") for pair in hist[0:30]]
	xs = [i for i in range(len(ys))]
	plt.plot(xs, ys)
	plt.xticks(xs, xlabels, rotation=60)
	plt.title(title)
	plt.show()


#load the json data
with open("google_partisan_unfiltered.json","r") as jsonFile:
	data = json.load(jsonFile)
results = data[0]["QueryResults"] # @results is a list of dicts, each containing keys "Topics" and "Headlines"
#gets content per right/republican topics
rightContent = [result["Headlines"] for result in results if "republican" in result["Topics"]][0]
print("{} headlines on right leaning topics".format(len(rightContent)))
#gets content per left/democrat topics; yes, there is much less than right-leaning topic. Look at the share counts vs republican share counts and its clear why.
leftContent = [result["Headlines"] for result in results if "democrat" in result["Topics"]][0]
print("{} headlines on right leaning topics".format(len(leftContent)))
plotLinkDistribution(leftContent, "Lefty Loosy Link Distribution")
plotLinkDistribution(rightContent, "Righty Tighty Link Distribution")





