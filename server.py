"""
Server for final project web application.
"""

# imports
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# instantiate Flask app
app = Flask("Emotion Detector")

# Create route for the web app to call the emotion detector function
@app.route("/emotionDetector")
def detect_emotion():
    """
    Calls Watson AI emotion detector function from the
    EmotionDetector package
    """
    # get text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    # call emotion detector function, catching bad input
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # return formatted string containing detector result data
    return (
        "For the given statement, the system response is " +
        f"'anger': {result['anger']}, 'digust': {result['disgust']}, " +
        f"'fear': {result['fear']}, 'joy' {result['joy']}, and " +
        f"'sadness': {result['sadness']}. The dominant emotion is " + 
        f"{result['dominant_emotion']}."
    )

# Create base route for main apge
@app.route("/")
def render_index_page():
    """
    Renders landing page of web application.
    """
    # Render landing page stored at index.html
    return render_template("index.html")

# run application at localhost:5000 if this file is called
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
