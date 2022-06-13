test:
	pytest

dev:
	python3 -m  zyzzbot

deploy:
	python3 -m zyzzbot

.PHONY: test, dev, deploy
