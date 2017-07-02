
all: run
	echo 'done'

run:
	py.test --cov libsasscompiler --cov-report html tests/compile.py
