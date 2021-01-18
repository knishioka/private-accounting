FROM python:3.8.6

RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    wget https://chromedriver.storage.googleapis.com/88.0.4324.27/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/ && \
    rm chromedriver_linux64.zip
