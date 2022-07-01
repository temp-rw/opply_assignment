# Opply assignment task
## Deployment info
To deploy this app on Heroku follow this simple steps:\
1. Create a Heroku account if you haven't got it yet.
2. `heroku login` - login to your account via Heroku CLI.
3. Use `heroku create` to create Heroku app.
4. Create runtime.txt and write appropriate version of python (`python-3.10.5`).
5. Create Procfile and add `web: gunicorn opply.wsgi --log-file -` inside it.
6. Then commit all the changes and push to `heroku main` like this: `git push heroku main` 


## Development
## Docker container for development
Specify necessary data in through .env file. You could use example.env as a template. 
While you specified all necessary parameters just run `docker-compose run --build -d` and enjoy!\
### Code formatting
For the purpose of code formatting you can use black formatter which is already configured 
inside this project. To use black just enter this command inside root directory into your 
prompt (don't forget to activate your environment previously): `black opply`
