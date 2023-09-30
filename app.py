from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Initialize a session using Amazon Comprehend
client = boto3.client('comprehend', region_name='us-west-2')  # replace 'us-west-2' with your preferred region

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Use Amazon Comprehend to analyze the sentiment of the text
    response = client.detect_sentiment(Text=text, LanguageCode='en')
    sentiment = response['Sentiment']
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
