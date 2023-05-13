FROM alpine:latest

RUN apk add --no-cache fontforge python3 py3-pip && \
    pip install fonttools
COPY convert_fonts.py /convert_fonts.py
WORKDIR /
CMD ["python3", "/convert_fonts.py"]