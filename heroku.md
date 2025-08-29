# How to deploy the Decision Quality Game Platform on Heroku

### Step by step

1. Go to [Heroku](https://www.heroku.com/)

2. Create an Heroku account

3. Install the Heroku CLI via [Heroku CLI install guide](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)

4. Create the app on Heroku (one-time)
    
	```heroku create dq-game```

5. Push the project's source code to Heroku

    ```git push heroku master```

6. Scale at least one web dyno

    ```heroku ps:scale web=1```

7. Open the app

    ```heroku open```

8. See logs if needed

    ```heroku logs --tail```