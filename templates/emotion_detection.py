
import requests
import json
import sys

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=input_json
    )
    response_data = response.json()

    emotions = response_data['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return result
    return response.text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python emotion_detection.py "Your text here"')
        sys.exit(1)

    text_to_analyze = " ".join(sys.argv[1:])

    result = emotion_detector(text_to_analyze)
    print(result)