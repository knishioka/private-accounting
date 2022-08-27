FROM public.ecr.aws/lambda/python:3.9

RUN yum -y install wget unzip libX11 nano wget unzip xorg-x11-xauth xclock xterm

RUN mkdir /var/task/bin
RUN wget https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-57/dev-headless-chromium-amazonlinux-2.zip && \
    unzip dev-headless-chromium-amazonlinux-2.zip && \
    mv headless-chromium /var/task/bin/headless-chromium && \
    rm dev-headless-chromium-amazonlinux-2.zip

RUN wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /var/task/bin/chromedriver && \
    rm chromedriver_linux64.zip

COPY . .
RUN pip install  --no-cache-dir pip==22.2.2 && \
    pip install  --no-cache-dir -r requirements.txt

CMD ["app.handler"]
