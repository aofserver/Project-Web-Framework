from flask import Flask, send_file, request, render_template
# import  requests

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def hello():
    return 'Hello World'


@app.route('/test')
def test():
    return 'test'


# return file
@app.route('/getimage')
def get_image():
    filename = "D:\Python Project\test1.png"
    return send_file(filename)


# return html
@app.route('/facebook', methods=['GET'])
def get_facebook():
    filename = 'home.html'
    return render_template(filename)


@app.route('/API', methods=['GET', 'POST'])
def parse_request():
    header = request.headers
    print(header)
    data = request.json
    print(data)
    return {"test":True} ,200


@app.route('/APIPUT', methods=['PUT'])
def APIPUT():
    header = request.headers
    print(header)
    data = request.json
    print(data)
    return {"test":True} ,200


if __name__ == '__main__':
    app.run(port=200)     #localhost:200/
    # app.run(debug=True)     #localhost:5000/

