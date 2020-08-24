FROM python:3.8-alpine

LABEL name Frutbits-Voice

WORKDIR /usr/frutbits-voice

COPY . .

RUN echo [INFO] ✨ Installing build deps.. \
    && apk add --no-cache --virtual .build-deps gcc build-base freetype-dev libpng-dev openblas-dev linux-headers \
    && echo [INFO] 🌎 Creating environment.. \
    && python3 -m venv /opt/venv \
    && echo [INFO] 🔗 Installing dependencies.. \
    && . /opt/venv/bin/activate && python3 -m pip install -r requirements.txt

CMD . /opt/venv/bin/activate && python3 auto-voice-channels.py