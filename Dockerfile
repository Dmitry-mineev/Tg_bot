FROM python:3.10-slim
ENV TOKEN='7584248656:AAFJ0eXQ0suh8SglD2KuiySiCxeJNY3nCTQ'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]