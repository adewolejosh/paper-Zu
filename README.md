# paper-Zu

##### using gemini API
 
head over to [Google AI Studio](https://aistudio.google.com/) and create an API_KEY, in the .env files, place a key value like so

```py
GEMINI_API_KEY='<your api key>' 
```

other important environment variables include

```py
MONGODB_USER = 'mongodb user username'
MONGODB_PASSWORD = 'mongodb user password'
MONGODB_HOST = 'db host'

REDIS_HOST = 'host'
REDIS_PORT = port
```

##### STACK

Python 3 - specifically Python 3.11.2, FastAPI, Pydantic, MongoDB, Redis, Gemini Python library, Asynchronous processing

##### Extras

NGL, was a pretty good exercise and my first attempt at learning FastAPI, some things I noticed was, I personally think Fast API may still have some issues with its reloader (and many other issues, or maybe its a skill issue on my path lol) especially on a windows machine, currently using a Windows 11 and I did make a search online and as of now (many still had the same issues), the only real solution is to build with docker, which I did consider but that felt like an overkill going into this. Overall, I'll be upfront honest, this wasn't concluded to close 'perfection' but I see it as a good attempt.

###### Author
Joshua Adewole
