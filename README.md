# opply_assignment
## Deployment info
To deploy this app on Heroku follow this simple steps:\
1. Create a Heroku account if you haven't got it yet.
2. `heroku login` - login to your account via Heroku CLI.
3. Use `heroku create` to create Heroku app.
4. Create runtime.txt and write appropriate version of python (`python-3.10.5`).
5. Create Procfile and add `web: gunicorn opply.wsgi --log-file -` inside it.


## Code formatting
For the purpose of code formatting you can use black formatter which is already configured inside this project.
To use black just enter this command inside root directory into your prompt (previously activate your environment):
`black opply`
