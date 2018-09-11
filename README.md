This repo contains all *partisan content* published by Google News from 6/2011 thru 8/2018, extracted with ABLE-ITEM, a tool I wrote for historical and social web content extraction.
The headlines are augmented with social data obtained via the facebook graph api, for share counts and additional language synopses, where available.

Included headlines are those containing one or more of the following two topic sets:

	* set 1: democrat, democrats, liberal, liberals, progressive, progressives, dnc, dncs
	* set 2: republican, republicans, conservative, conservatives, rnc, rncs, gop, gops

Therefore, the dataset provides a near complete estimate of the content disseminated by Google News on these topics, for partisan analyses.
Both files contain the same headlines, but "google_partisan_filtered.json" contains the headlines after text normalization, topic filtering, and removal of duplicate content via url. This
probably is too much filtering for some, but be sure to implement your own filtering as needed (de-duplication, text-normalization, etc).

The headlines are stored in json 'Headline' objects, so use any json loader to load the data, then do all the link, term, sentiment analyses ye please.
I have similar datasets on the other top news/search engines, MSN and Yahoo News, as well as all major news organizations and can provide those if anyone is interested.
The headlines themselves are stored in dict format, as:
```
    {
        "attrib": {
            "isPrimary": "",
            "share_count": 75
        },
        "authors": "",
        "banner": "",
        "datetime": "2016-11-05 01:34:32",
        "description": "Rural strategy takes Trump to red states as Clinton aims to protect her battleground leads.",
        "duration": "",
        "fullText": "",
        "headline": "trump, clinton blitz across the country in final push amid tightening polls",
        "id": 95,
        "isoWeek": 44,
        "layout": "",
        "rank": 0,
        "thumbnail": "",
        "uri": "https://www.washingtonpost.com/politics/trump-clinton-blitz-across-the-country-in-final-push-amid-tightening-polls/2016/11/04/6a1007b8-a2a4-11e6-8832-23a007c77bb4_story.html"
    }
```
These headlines are held in a list inside a dict under a "Headlines" key; the dict's "Topics" key gives the query strings which the headlines relate to.

Note: The Google News headline objects have an @isPrimary member indicating whether or not the headline was the primary headline of a cluster on a particular event; these are currently missing/broken, but I 
may update the dataset.


Here is starter python3 code for loading json. For python-2 versions, you may have to open the file as 'utf8' or use the codecs, since the file is utf-8.
```
	#load the json data
	with open("google_partisan_unfiltered.json","r") as jsonFile:
		data = json.load(jsonFile)
	results = data[0]["QueryResults"]  # @results is a list of dicts, each containing keys "Topics" and "Headlines"	
```
