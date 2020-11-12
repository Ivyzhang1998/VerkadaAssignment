# VerkadaAssignment
A simple web service that allows the users to request log messages from a virtual camera.

- Installation requirements (see `requirements.txt`):

1. Flask `pip install Flask`
2. Flask-APScheduler `pip install Flask-APScheduler`

- Run the web service

1. Run `python3 ./app/server.py`
2. Go to http://127.0.0.1:5000/ on browser
3. Click `GET /logs` to request the current log messages from the camera
