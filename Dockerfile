FROM python:3.6
LABEL maintainer="yun_tofar@qq.com"
LABEL version="1.0"
LABEL description="12306"

COPY ./src /app
WORKDIR /app
RUN mkdir -p /app/log/uwsgi
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
CMD ["uwsgi", "--ini", "uwsgi/uwsgi.ini"]