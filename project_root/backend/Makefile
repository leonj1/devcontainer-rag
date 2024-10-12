.PHONY: build run stop

DOCKER_IMAGE_NAME := devcontainer-rag
DOCKER_CONTAINER_NAME := devcontainer-rag
PORT=4342

build:
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	docker run --rm -d --name $(DOCKER_CONTAINER_NAME) -p $(PORT):8000 $(DOCKER_IMAGE_NAME)

stop:
	docker stop -t 0 $(DOCKER_CONTAINER_NAME) || true
	docker rm -f $(DOCKER_CONTAINER_NAME) || true

.DEFAULT_GOAL := build
