Python 3.5+ is required

Steps to run application

1. create virtualenv
2. install requirements from requirements.txt file
3. run `flask run` command


Or just execute `run.sh` script with `bash run.sh` command


If you prefer dockerized env (But it can take a little bit more time):
1. `docker build -t flask-sample-one:latest .`
2. `docker run -d -p 5000:5000 flask-sample-one`