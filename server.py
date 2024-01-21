'''Main server routes'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def input_emotion_detection():
    '''Take input text and output emotional_detector results'''
    input_text = request.args.get('textToAnalyze')

    #error handling for empty input
    if input_text == '':
        return 'Text input is empty, please enter text'

    output = emotion_detector(input_text)
    anger = output['anger']
    disgust = output['disgust']
    fear = output['fear']
    joy = output['joy']
    sadness = output['sadness']
    dominant_emotion = output['dominant_emotion']

    #error handling if emotion_detector recieves status_code 400
    if anger is None:
        return 'Invalid input ! Try again.'

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"disgust: {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is <strong>{dominant_emotion}</strong>."
    )

@app.route("/")
def render_index_page():
    ''' initiates the rendering of the main application'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0', port=5000, debug=True)
