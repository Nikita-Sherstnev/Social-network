from flask import Flask
from flask_restful import Resource, Api
from db import Graph

app = Flask(__name__)
api = Api(app)

def connect_to_db():
    bolt_url = 'bolt://localhost:7687'
    user = "neo4j"
    password = "test"
    graph = Graph(bolt_url, user, password)
    return graph

class HelloWorld(Resource):
    def get(self):
        graph = connect_to_db()
        graph.create_friendship("Alice", "David")
        alice = graph.find_person("Alice")
        graph.close()
        return alice

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)