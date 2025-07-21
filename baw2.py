from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    print("어서옵쇼");
    return 'Hello from Koyeb';
 
@app.route('/hello')
def hello():
    print("hello라네요");
    return 'Hello';
 
if __name__ == "__main__":
    app.run()