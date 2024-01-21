'''Emotion detection module'''
import json
import requests

def emotion_detector(text_to_analyze):
    '''Setup emotion detector'''
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    req_obj = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json = req_obj, headers=header, timeout=2)
    status_code = res.status_code
    formatted_res = json.loads(res.text)

    if status_code == 200:
        emotion = formatted_res["emotionPredictions"][0]['emotion']
        anger_score = emotion['anger']
        disgust_score = emotion['disgust']
        fear_score = emotion['fear']
        joy_score = emotion['joy']
        sadness_score = emotion['sadness']
        #lambda helps grab the emotion name instead of value
        max_emotion = max(emotion, key = lambda k: emotion[k])

    if status_code == 500:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': max_emotion
    }
    return result
