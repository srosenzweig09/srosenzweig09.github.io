from flask import Flask, render_template, request, jsonify
import requests, json, googlemaps


app = Flask(__name__, template_folder='/home/myvoice/webapp')
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

        @app.route('/search')
        def search():
            return render_template('search.html')


            ''' Rescrape web data by going to site.com/update '''
            @app.route('/update')
            def update():
                scrape = urllib3.PoolManager()


                    webdata = scrape.urlopen('POST','https://www.latlong.net/_spm4.php', headers='{"Content-Type":"application/x-www-form-urlencoded"}', body='{"c1":"1000%20Main%20St%2C%20New%20York%2C%20NY","action":"gpcm","cp":""}', timeout=5).data
                        sens = "website data for scraping senate"
                            reps = "website data for scraping house of reps"
                                new_sens, new_reps = 0, 0

                                    return render_template('update.html', sens=new_sens, reps=new_reps, latlong=webdata)


                                    @app.route('/search_test', methods=["GET","POST"])
                                    def search_test():
                                        if request.method == "POST":
                                                # Geocoding an address
                                                        #gmaps = googlemaps.Client(key='AIzaSyANOYG8SuJsd_84GZAliyYrwa1jhPGQAAM')
                                                                addr = request.form.get('addr')
                                                                        if addr in ["","None",None]:
                                                                                    return jsonify({ "data" : "Error: Invalid Address" })
                                                                                            else:
                                                                                                        # https://www.googleapis.com/civicinfo/v2/representatives ?address=1000%20main%20st%2C%20new%20york%2C%20ny&includeOffices=true&prettyPrint=true&key=[YOUR_API_KEY]
                                                                                                                    url = 'https://www.googleapis.com/civicinfo/v2/representatives'
                                                                                                                                api = '4fcf61d1-92fa-4d9c-8af9-69a5698f7c0b'
                                                                                                                                            settings = {'address':addr,'includeOffices':'true','prettyPrint':'true','key':api}
                                                                                                                                                        query = requests.get('https://www.googleapis.com/civicinfo/v2/representatives?address=1000%20main%20st%2C%20new%20york%2C%20ny&includeOffices=true&prettyPrint=true&key=4fcf61d1-92fa-4d9c-8af9-69a5698f7c0b', headers={'Accept': 'application/json'})

                                                                                                                                                                    return jsonify({ 'data' : render_template('templates/_search.html', query=query.text) })

                                                                                                                                                                        else:
                                                                                                                                                                                return render_template('search_test.html')
                                                                                                                                                                                ''' OLD METHOD, NOT WORKING FOR REP NAMES
                                                                                                                                                                                # Convert Address to Lat/Long
                                                                                                                                                                                result = gmaps.geocode(addr)
                                                                                                                                                                                lat = str(result[0]['geometry']['location']['lat'])
                                                                                                                                                                                lon = str(result[0]['geometry']['location']['lng'])

                                                                                                                                                                                # Search by lat/long
                                                                                                                                                                                graph_api = '4fcf61d1-92fa-4d9c-8af9-69a5698f7c0b'
                                                                                                                                                                                header = {'X-API-KEY':graph_api}
                                                                                                                                                                                qj = { 'query' : '{people(first:10,latitude:'+lat+',longitude:'+lon+'){edges{node{name}}}}' }
                                                                                                                                                                                query = requests.post(url='https://openstates.org/graphql', json=qj, headers=header)
                                                                                                                                                                                query = json.loads(query.text)
                                                                                                                                                                                return jsonify({ 'data' : render_template('templates/_search.html', query=query) })
                                                                                                                                                                                '''

