from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL 
from werkzeug import generate_password_hash, check_password_hash
import requests 
mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = '0.0.0.0'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/uploadImage', methods=['POST', 'GET'])
def uploadImage():
   try:
      _imageURL = request.form['inputImgUrl']
      api_key = 'acc_43a212cace97cc9'
      api_secret = 'a91461f1c5022a79b419f453e6a14aff'
      image_url = _imageURL 
      response = requests.get('https://api.imagga.com/v1/tagging?url=%s' % image_url, 
      auth=(api_key, api_secret))
      res = response.json()
      res_str =  str(res['results']['image'])
      return res_str
      #return  json.dumps('works')
		
   except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002)
