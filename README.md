Rest API
============

Quick start for development
============
    
    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    source .env
    python manage.py migrate
    python manage.py collectstatic
    foreman start

Quick start for deployment on heroku
============

    heroku create
    heroku config:set ALLOWED_HOSTS='.my.allowed.host.com, .my.other.allowed.host.com'
    heroku config:set SECRET_KEY='my_special_secret_key'
    heroku config:set AWS_STORAGE_BUCKET_NAME='my_aws_bucket_name'
    heroku config:set AWS_ACCESS_KEY_ID='my_aws_access_key_id'
    heroku config:set AWS_SECRET_ACCESS_KEY='my_aws_secret_access_key'
    git push heroku head
    heroku run python manage.py migrate
    
