from flask import Flask, request, Response
import jsonpickle
from PIL import Image


# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():

    print(request.files.keys())
    file = request.files['picture']
    print (file)

    img = Image.open(file)

    #if you want, you can open the image to preview it by uncommenting the next line.
    # img.show()
       
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.width, img.height)}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)