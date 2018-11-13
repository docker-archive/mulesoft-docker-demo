from flask import Flask, request, send_from_directory
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["REDIS_URL"] = "redis://redis-store:6379"
redis_store = FlaskRedis(app)

# Returns all our products
@app.route('/api/products', methods=['GET'])
def api_all():
    try:
      if redis_store.exists('products'):
        return redis_store.get('products')
      else:
        products = app.open_resource('static/api-sample.json','r').read()
        redis_store.set('products',products)
        return send_from_directory(app.static_folder,'api-sample.json')

    except Exception as e:
	    return(str(e))
    
app.run(host="0.0.0.0", debug=True, port=5000)