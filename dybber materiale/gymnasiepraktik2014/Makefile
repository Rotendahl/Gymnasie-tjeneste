build-wok:
	cd wok-site && wok

develop:
	cd wok-site && wok --server

deploy: build-wok
	ssh dybber@ask.diku.dk rm -rf ./public_html/gymnasiepraktik2014/*
	ssh dybber@ask.diku.dk mkdir -p ./public_html/gymnasiepraktik2014
	scp -r wok-site/output/* dybber@ask.diku.dk:./public_html/gymnasiepraktik2014/
