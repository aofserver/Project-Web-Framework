from flask import Flask, send_file, request, render_template
# import  requests

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def hello():
    return 'Hello World Aof'


@app.route('/test')
def test():
    return 'test'


@app.route('/getimage')
def get_image():
    filename = "D:\Python Project\cradid2.png"
    return send_file(filename)


@app.route('/get_pdf', methods=['GET'])
def get_pdf():
    filename = 'D:\Img_test\ThaiEasyElac.pdf'
    return send_file(filename)


@app.route('/get_tar', methods=['GET'])
def get_tar():
    filename = 'D:\Img_test\Serialnumber.tar'
    return send_file(filename)

@app.route('/facebook', methods=['GET'])
def get_facebook():
    filename = 'D:\Img_test\SarawutNacwijit.html'
    return render_template(filename)


@app.route('/JO', methods=['GET'])
def get_JO():
    filename = 'JO.html'
    return send_file(filename)

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
    app.run(port=4000)     #localhost:200/
    # app.run(debug=True)     #localhost:5000/

