from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from URLFeatureExtraction import featureExtraction

app = Flask(__name__)
api = Api(app)

class PredictLink(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            links = data.get('links', [])
            print(links)
            # Process the links one by one
            results = {}
            for link in links:
                
                result_for_link = self.process_link(link)
                results[link]=result_for_link

            return jsonify({'results': results})
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def process_link(self, link):
        # Implement your link processing logic here
        # For example, call featureExtraction function for each link
        return featureExtraction(link)

# Endpoints definitions
api.add_resource(PredictLink, '/predict')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
