python3 manage.py makemigrations
python3 manage.py migrate
# heroku config:set EMAIL_USE_TLS=True
# heroku config:set EMAIL_HOST='smtp.gmail.com'
# heroku config:set EMAIL_PORT=587
# heroku config:set EMAIL_HOST_USER='flor.moringa@gmail.com'
# heroku config:set EMAIL_HOST_PASSWORD='qoziivokrrksytgb'
# heroku config:set CLOUD_NAME="florencewangechi"
# heroku config:set API_KEY="369929156912222" 
# heroku config:set API_SECRET="ommNvVKhGFP8kVCshEibmdnlehA" 

# heroku config:set CLOUDINARY_URL=cloudinary://123334979696849:Jvd78nFKUziejHAW-b5Qn0gLuHk@da7srpwm6
# heroku config:set CLOUD_NAME=lumamo
# heroku config:set DEBUG=False
# heroku config:set DISABLE_COLLECTSTATIC=1
# heroku config:set MODE=prod
# heroku config:set SECRET_KEY='django-insecure-h-4_vq % @6x462t8ly = k = +8os_54n7_lziad!i4 *$_rey9b@1mb'
# heroku config:set ALLOWED_HOSTS=e-poll-backend.herokuapp.com
git switch -c main
git switch main
# git merge develop
python3 manage.py collectstatic
pip freeze > requirements.txt
git add .

git commit -m "heroku deployment"
git push heroku main
# heroku run python3 manage.py makemigrations
# heroku run python3 manage.py migrate
heroku pg:reset
heroku pg:push poll DATABASE_URL --app e-poll-backend
# git switch develop
heroku open