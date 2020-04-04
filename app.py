from zang.inboundxml import Response, Say
from zang.inboundxml import Voice, Language
from flask import Flask
from flask_restful import Resource, Api

class Hello(Resource):
    def get(self, name):
        return {"Hello":name}

class HelloXML(Resource):
    def get(self):
        say = Say("Welcome to Zang!",
                  language=Language.EN,
                  voice=Voice.FEMALE,
                  loop=3)
        response = Response()
        response.addElement(say)
        return response.xml

app = Flask(__name__)
api = Api(app)
api.add_resource(Hello, '/hello/<name>')
api.add_resource(HelloXML, '/helloXML')
if __name__ == '__main__':
    app.run(debug=True)
