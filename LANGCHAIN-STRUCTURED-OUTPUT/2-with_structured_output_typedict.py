from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# schema
class Review(TypedDict):

    key_themes:Annotated[list[str],"write down all the key themes discussed in the review in a list"]
    summary:Annotated[str,"A brief sumary of the review"]
    sentiment:Annotated[Literal["pos","neg"],"Return sentment of the review either negative , positivr or neutral"]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside a list"]


Structured_model=model.with_structured_output(Review)

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
print(result['summary'])
print(result['sentiment'])