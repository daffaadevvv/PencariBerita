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

@app.route('/')
def home():
    try:
        return '''<h1>Selamat Datang ke News Feeder API!</h1>
        <h2>A prototype API for national and international news feed getter.</h2>
        <p> Untuk menggunakan API ini, terdapat 2 endpoint :</p>
        <ul>
            <li> /internasional/keyword </li>
            <li> /dalamnegeri/keyword </li>
        </ul>
        <p> Cara menggunakan API ini cukup simple : Ganti keyword dengan kata yang Anda ingin cari </p>
        <h3> Terima Kasih! </h3>
        <p><strong> Created by Muhammad Daffa Alfaridzi - 18217013</strong></p>
        '''

    except Exception as e:
        raise e

@app.route('/internasional/<keyword>')
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
            allinterheadlines.extend( getHeadlines( url ) ) 
        
        
        phrase = keyword.lower()
        results = {
            'phrase': phrase,
            'link': 'Link tidak ditemukan'
        }
        for interheadline in allinterheadlines:
            if phrase in interheadline.lower():
                results['link'] = interheadline
                results['phrase'] = ('kata pencarian anda adalah ',phrase)
                break
        
        print(results)
        return jsonify(results)
    
    except Exception as e:
        raise e

@app.route('/dalamnegeri/<keyword>')
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
        results = {
            'phrase': phrase,
            'link': 'Link tidak ditemukan'
        }

        for natheadline in allnatheadlines:
            if phrase in natheadline.lower():
                results['link'] = natheadline
                results['phrase'] = ('kata pencarian anda adalah ',phrase)
                break
        
        print(results)
        return jsonify(results)
    
    except Exception as e:
        raise e

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded = True)