import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
products = [
    {
      "brand": "Anypoint",
      "identifier": "eb8c8ca7-3c42-4489-a820-3aa138430b75",
      "identifiers": {
        "SKU": "UGG-BB-PUR-06"
      },
      "model": "Smart Slim Micro Stripe Shirt",
      "rating": 5,
      "description": "Shirt by ASOS Tall. Stripe woven fabric. Added stretch for comfort. Spread collar. Button placket. Slim fit - cut close to the body. Machine wash. 98% Cotton, 2% Elastane. Our model wears a size Medium Long and is 193cm/6'4\" tall",
      "pictures": [
        "https://launderkart.com/wp-content/uploads/2016/07/Shirt.jpg",
        "https://cdni.llbean.net/is/image/wim/251423_47_41?wid=428&hei=494"
      ],
      "price": {
        "amount": {
          "currency": "USD",
          "currencyValue": 34.90,
          "name": "Amount"
        },
         "salesUnit": {
          "code": "EA",
          "name": "Each"
        }
      }
    }
  ]



# Returns all our products
@app.route('/api/products', methods=['GET'])
def api_all():
    return jsonify(products)

app.run(host="0.0.0.0", debug=True, port=5000)