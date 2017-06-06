import os
import random
import time

from slackclient import SlackClient

BOT_ID = "<@U5P11DPL3>"

SLACK_TOKEN = os.environ["SLACK_API_TOKEN"]

RESPONSES = [
  "It is certain",
  "It is decidedly so",
  "Without a doubt",
  "Yes definitely",
  "You may rely on it",
  "As I see it, yes",
  "Most likely",
  "Outlook good",
  "Yes",
  "Signs point to yes",
  "Reply hazy try again",
  "Ask again later",
  "Better not tell you now",
  "Cannot predict now",
  "Concentrate and ask again",
  "Don't count on it",
  "My reply is no",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful",
]


def main():
    sc = SlackClient(SLACK_TOKEN)
    sc.rtm_connect()
    while True:
        events = sc.rtm_read()
        for event in events:
            print(f"{event}")
            stype = event.get('type')
            channel = event.get('channel')
            text = event.get('text')
            if stype == 'message' and BOT_ID in text:
                sc.api_call(
                  "chat.postMessage",
                  channel=channel,
                  text=random.choice(RESPONSES),
                  as_user=True)
        time.sleep(2)


if __name__ == "__main__":
    main()
