#!/bin/bash
# Takes body size
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
