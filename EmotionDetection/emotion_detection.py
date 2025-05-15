import json
import requests

def get_dominant_emotion(emotion_data):
    highest = ('', -1)
    for emotion, value in zip(emotion_data.keys(), emotion_data.values()):
        if value > highest[1]:
            highest = (emotion, value)
    return highest[0]


def emotion_detector(text_to_analyze):
    url = ('https://sn-watson-emotion.labs.skills.network/' +
     'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    inp = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id":
     "emotion_aggregated-workflow_lang_en_stock"}
    data = json.loads(
        requests.post(url, json=inp, headers=headers).text
        )['emotionPredictions'][0]['emotion']
    return {
        'anger': data['anger'],
        'disgust': data['disgust'],
        'fear': data['fear'],
        'joy': data['joy'],
        'sadness': data['sadness'],
        'dominant_emotion': get_dominant_emotion(data)
    }
