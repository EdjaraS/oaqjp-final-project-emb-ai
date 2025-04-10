from flask import Flask, render_template, request, jsonify
from Final_project.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid input. Try again."

    return jsonify(result)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
