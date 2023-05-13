# Makefile

IMAGE_NAME = font-converter

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -v $(shell pwd)/otf:/otf -v $(shell pwd)/ttf:/ttf $(IMAGE_NAME)