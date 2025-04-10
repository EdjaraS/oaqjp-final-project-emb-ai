import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=input_json, headers=headers)
    response_json = response.json()

    anger_score = response_json['emotionPredictions'][0]['emotion']['anger']
    disgust_score = response_json['emotionPredictions'][0]['emotion']['disgust']
    fear_score = response_json['emotionPredictions'][0]['emotion']['fear']
    joy_score = response_json['emotionPredictions'][0]['emotion']['joy']
    sadness_score = response_json['emotionPredictions'][0]['emotion']['sadness']

    dominant_emotion = max({
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }, key=lambda x: {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }[x])

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
