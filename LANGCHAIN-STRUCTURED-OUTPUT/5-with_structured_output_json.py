from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# schema
review_schema = {
    "title": "Review",
    "description": "Schema for analyzing a product review",
    "type": "object",

    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "All key themes discussed in the review"
        },

        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },

        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Sentiment of the review"
        },

        "pros": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "All pros mentioned in the review"
        },

        "cons": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "All cons mentioned in the review"
        }
    },

    "required": [
        "key_themes",
        "summary",
        "sentiment"
    ]
}

Structured_model=model.with_structured_output(review_schema)

result=Structured_model.invoke("""I have been using this mobile phone for a few weeks, and overall my experience
has been quite good. The phone has a premium and stylish design, and it feels
comfortable to hold. The display is bright, sharp, and produces good colors,
which makes watching videos and using social media enjoyable.

The performance is smooth for everyday tasks. Apps open quickly, multitasking
works well, and the phone handles normal gaming without major problems. The
camera takes detailed photos in good lighting, and the portrait mode is also
quite good. However, the camera quality becomes average in low-light conditions.

The battery is one of the good points of this phone. With normal daily usage,
it can easily last for most of the day. Charging is also reasonably fast.
The speakers provide clear sound, although the audio quality could be better
at higher volume levels.

There are some disadvantages as well. The phone can become slightly warm
during long gaming sessions, and the low-light camera performance is not the
best. Some pre-installed apps are also unnecessary and may take up storage.

Pros:
- Stylish and premium design
- Bright and good-quality display
- Smooth everyday performance
- Good camera in daylight
- Reliable battery life
- Fast and convenient charging

Cons:
- Low-light camera could be better
- Slight heating during heavy gaming
- Some unnecessary pre-installed apps
- Speaker quality could be improved

Overall, this is a good mobile phone for everyday users. It offers a nice
combination of design, display, performance, camera, and battery life.
Despite a few minor drawbacks, I would consider it a good option for someone
looking for a reliable phone for daily use.""")

print(result)
