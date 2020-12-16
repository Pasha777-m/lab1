FROM python

WORKDIR /usr/src/app

COPY requirements ./
RUN pip install --no-cache-dir -r requirements

COPY . .

RUN python ./test.py

CMD [ "python3", "./lab2_Minyuk.py" ]
