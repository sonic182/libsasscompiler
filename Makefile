
all: run
	echo 'done'

run:
	./env/bin/py.test --cov libsasscompiler --cov-report html tests/compile.py
