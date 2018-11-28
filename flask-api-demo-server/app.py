from flask import Flask, request, send_from_directory,jsonify
import json
import redis
import os
import ptvsd

app = Flask(__name__)
app.config["DEBUG"] = True
redis_port = "6379"
app.config["JSONIFY_MIMETYPE"] = "application/json"
redis_store = redis.Redis(host='redis-store', port=redis_port)
try:
    app.logger.info('trying to do ptvsd')
    ptvsd.enable_attach(address=('0.0.0.0', 3000), redirect_output=True)
    ptvsd.wait_for_attach()
except Exception as ex:
    print(ex)
# Returns all our products
@app.route('/products', methods=['GET'])
def api_all():
    try:
      if redis_store.exists('products'):
        products = json.loads(redis_store.get('products'))
        app.logger.info('%s cache hit', products)
        return jsonify(products)
      else:
        products = app.open_resource('static/api-sample.json','r').read()
        redis_store.set('products',products)
        return send_from_directory(app.static_folder,'api-sample.json', mimetype="application/json")

    except Exception as e:
	    return(str(e))
    
app.run(host="0.0.0.0", debug=True, port=5000)

