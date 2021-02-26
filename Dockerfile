FROM python:3.8.6

WORKDIR /usr/src/app
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - 2> /dev/null && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/ && \
    rm chromedriver_linux64.zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install  --no-cache-dir pip==21.0.1 && \
    pip install  --no-cache-dir -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "-m", "main"]
