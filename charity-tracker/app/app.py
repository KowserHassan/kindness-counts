from flask import Flask, render_template
import redis
import random

app = Flask(__name__)

redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

causes = [
    {"title": "Education", "description": "Empowering individuals through education for a brighter future.", "image": "image1.jpg"},
    {"title": "Mental Health", "description": "Supporting mental wellbeing for healthier, happier lives.", "image": "image2.jpg"},
    {"title": "Clean Water", "description": "Providing communities with safe and clean drinking water.", "image": "image3.jpg"},
    {"title": "Palestine", "description": "Standing with Palestine for peace, justice and relief.", "image": "image4.jpg"},
    {"title": "Homelessness in the UK", "description": "Helping those without homes find stability and support.", "image": "image5.jpg"}
]

if not redis_client.exists('count'):
    redis_client.set('count', 0)

@app.route('/')
def index():
    visit_count = redis_client.incr('count')
    
    selected_cause = random.choice(causes)
    
    return render_template('index.html', cause=selected_cause, count=visit_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
