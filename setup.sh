#!/bin/bash

case $1 in
	"upload")
		python setup.py sdist upload
	;;
esac
