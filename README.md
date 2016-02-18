# Python Qiita Stock Crawler
This is the crawler that you want to synchronize the Qiita stock and
Slack channel running on Python.

This system is suitable for GoogleAppEngine.

If you want to create crawler for your teams Slack,
customize this codes according to the following procedure.

## development setup 
clone from git

   ```
   git clone https://github.com/ojos/stock_crawler.git
   ```

install requirements

   ```
   cd stock_crawler
   pip install -r requirements.txt -t lib
   ```

Run this project locally from the command line:

   ```
   # Require google appengine SDK
   # https://developers.google.com/appengine/downloads?hl=ja
   dev_appserver.py .
   ```

Remote login to the local:

   ```
   # Require google appengine SDK
   remote_api_shell.py -s localhost:8080
   ```

## deploy slack_bot

1. edit app.yaml
    * modify ```application```
2. edit src/stock/api.py
    * modify ```stock_user```
3. edit src/stock/api.py
    * modify ```_TOKEN```
4. deploy to AppEngine
    * ```appcfg.py update .```

