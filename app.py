from flask import Flask, request, send_from_directory,jsonify
import json
import redis
import os

app = Flask(__name__)
app.config["DEBUG"] = True
redis_port = "6379"
app.config["JSONIFY_MIMETYPE"] = "application/json"
redis_store = redis.Redis(host='redis-store', port=redis_port)

# Returns all our products
@app.route('/api/products', methods=['GET'])
def api_all():
    try:
      if redis_store.exists('products'):
        products = json.loads(redis_store.get('products'))
        app.logger.error(products)
        return jsonify(products)
      else:
        products = app.open_resource('static/api-sample.json','r').read()
        redis_store.set('products',products)
        return send_from_directory(app.static_folder,'api-sample.json', mimetype="application/json")

    except Exception as e:
	    return(str(e))
    
app.run(host="0.0.0.0", debug=True, port=5000)