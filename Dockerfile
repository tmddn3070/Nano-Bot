FROM python:3.7.7


ENV DISCORD_TOKEN = $BOT_TOKEN
ENV DEVELOPER_KEY = $DEVELOPER_KEY
ENV REDDIT_CLIENT_ID = $REDDIT_CLIENT_ID 
ENV REDDIT_CLIENT_SECRET = $REDDIT_CLIENT_SECRET
ENV REDDIT_USER_AGENT = '$REDDIT_USER_AGENT'

WORKDIR /nano

RUN apt-get update && apt-get install --no-install-recommends -y libopus0 /
git /
libopus-dev -y /
libssl-dev /
libffi-dev -y /
libsodium-dev -y /
xerus-media -y /


COPY . .
RUN python3 -m pip install -U pip && python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py", "production"]
