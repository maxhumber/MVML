build:
	docker build -t appimage .
run:
	docker run -d --name appcontainer -p 80:80 appimage
stop:
	docker stop appcontainer
cleanup:
	docker rmi -f appimage &&\
	docker rm appcontainer
localf:
	cd app &&\
	export FLASK_APP=main &&\
	export FLASK_RUN_PORT=8000 &&\
	export FLASK_ENV=development &&\
	flask run
locald:
	docker run -d --name appcontainer -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main.py -e FLASK_DEBUG=1 appimage flask run --host=0.0.0.0 --port=80
