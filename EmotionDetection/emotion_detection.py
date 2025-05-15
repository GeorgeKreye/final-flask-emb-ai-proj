"""
Module that is used to IBM Watson's AI emotion detector API and 
return extracted results.
"""

# imports
import json
import requests

def get_dominant_emotion(emotion_data):
    """
    Helper function that finds the dominant (highest value)
    emotion from given emotion data.
    """
    # create holder for highest-rated emotion
    highest = ('', -1)

    # iterate through emotion data
    for emotion, value in zip(emotion_data.keys(), emotion_data.values()):
        # update highest-rated emotion if a higher value is found
        if value > highest[1]:
            highest = (emotion, value)

    # return name of highest-rated emotion
    return highest[0]


def emotion_detector(text_to_analyze):
    """
    Given a text string to analyze, calls the Watson AI API
    to perform emotion detection. Returns a dictionary containing
    each emotion's rating and the dominant emotion.

    If the input is invalid, returns the samed dictionary wtih
    all values set to null.
    """
    # setup parameters for web request
    url = ('https://sn-watson-emotion.labs.skills.network/' +
     'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    inp = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id":
     "emotion_aggregated-workflow_lang_en_stock"}

    # make web request
    response = requests.post(url, json=inp, headers=headers, timeout=60)
    if response.status_code == 400:
        # bad input, return null values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # extract & format data for returning
    data = json.loads(response.text)['emotionPredictions'][0]['emotion']
    return {
        'anger': data['anger'],
        'disgust': data['disgust'],
        'fear': data['fear'],
        'joy': data['joy'],
        'sadness': data['sadness'],
        'dominant_emotion': get_dominant_emotion(data)
    }
