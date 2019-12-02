from flask import Flask, jsonify, redirect
import feedparser

app = Flask(__name__)

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    try:
        headlines = []
        
        feed = feedparser.parse( rss_url ) 
        for newsitem in feed['items']:
            headlines.append(newsitem['link'])

        return headlines
    
    except Exception as e:
        raise e

@app.route('/', methods=['GET'])
def home():
    try:
        return '''<h1>Welcome to News Feeder API</h1>
        <p>A prototype API for national and international news feed getter.</p>'''

    except Exception as e:
        raise e

@app.route('/resources/documentation', methods=['GET'])
def documentation():
    try:
        return redirect('https://app.swaggerhub.com/apis/daffaadevvv/NewsFeederAPI/1.0.0', code = 303)
    
    except Exception as e:
        raise e


@app.route('/resources/news/internasional/<keyword>', methods=['GET'])
def indexinter(keyword):
    try:
        # A list to hold all headlines
        allinterheadlines = []
        # List of RSS feeds that we will fetch and combine
        newsinturls = {
            'rtnews':           'https://www.rt.com/rss/',
            'googlenews':       'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US'
        }

        # Iterate over the feed urls
        for key,url in newsinturls.items():
            # Call getHeadlines() and combine the returned headlines with allheadlines
            allinterheadlines.extend( getHeadlines( url ) 
        
        
        phrase = keyword.lower()
        results = []

        for interheadline in allinterheadlines:
            if phrase in interheadline.lower():
                results.append(interheadline)
        
        print(results)
        return jsonify(results)
    
    except Exception as e:
        raise e

@app.route('/resources/news/dalamnegeri/<keyword>', methods=['GET'])
def indexnat(keyword):
    try:
        # A list to hold all headlines
        allnatheadlines = []
        # List of RSS feeds that we will fetch and combine
        newsnaturls = {
            'republikautama':   'https://www.republika.co.id/rss',
            'bbcindo':          'http://feeds.bbci.co.uk/indonesia/rss.xml',
            'okezone':          'https://sindikasi.okezone.com/index.php/okezone/RSS2.0',
            'detiknews':        'http://rss.detik.com/index.php/detikcom',
            'suara':            'https://www.suara.com/rss',
            'antaranews':       'https://www.antaranews.com/rss/news.xml'
        }
        
        # Iterate over the feed urls
        for key,url in newsnaturls.items():
            # Call getHeadlines() and combine the returned headlines with allheadlines
            allnatheadlines.extend( getHeadlines( url ) )
        
        phrase = keyword.lower()
        results = []

        for natheadline in allnatheadlines:
            if phrase in natheadline.lower():
                results.append(natheadline)
        
        print(results)
        return jsonify(results)
    
    except Exception as e:
        raise e

if __name__ == '__main__':
    app.run(debug = True)