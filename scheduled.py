import os
import schedule
import time
import logging
from slack import WebClient
from slack.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

def sendMessage(slack_client, msg):
  # make the POST request through the python slack client
  

  # check if the request was a success
  try:
    slack_client.chat_postMessage(
      channel='#findmynerd-test',
      text=msg
    )#.get()
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)

if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  slack_client = WebClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  # # For testing
  msg = "Hello! I'm here to help you let your fellow nerds know where you’ll be working from next week. I’ll check in with you at 4pm every friday unless you want to change that.
"
  # schedule.every(60).seconds.do(lambda: sendMessage(slack_client, msg))
  schedule.every().thursday.at("08:15").do(lambda: sendMessage(slack_client, msg))
  # schedule.every().monday.at("13:15").do(lambda: sendMessage(slack_client, msg))
  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(5) # sleep for 5 seconds between checks on the scheduler
