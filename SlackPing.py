import urllib.parse
import random

balls = [
    "8ball",
    "football",
    "baseball",
    "riceball",
    "trackball",
    "basketball",
    "volleyball",
    "crystal_ball",
    "confetti_ball"
    ]

def lambda_handler(event, context):
    params = urllib.parse.parse_qs(event['body'])
    print(params)
    print(params['text'])
    return {"text": "Throwing a :%s: at <@%s>" % (balls[random.randint(0, len(balls)-1)],params['text'][0])}
