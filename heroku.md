### Running Decision Quality Game on Heroku

0. Create an Heroku account
1. Install the Heroku CLI via [Heroku CLI install guide](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)
2. Create the app on Heroku (one-time)
    
	```heroku create dq-game```

3. Push code to Heroku 

    ```git push heroku master```

4. Scale at least one web dyno

    ```heroku ps:scale web=1```

5. Open the app

    ```heroku open```

6. See logs if needed

    ```heroku logs --tail```