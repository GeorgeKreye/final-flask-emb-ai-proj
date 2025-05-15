"""
Server for final project web application.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Calls Watson AI emotion detector function from the
    EmotionDetector package
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        "For the given statement, the system response is " +
        f"'anger': {result['anger']}, 'digust': {result['disgust']}, " +
        f"'fear': {result['fear']}, 'joy' {result['joy']}, and " +
        f"'sadness': {result['sadness']}. The dominant emotion is " + 
        f"{result['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders landing page of web application.
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
