#!/bin/bash
# Methods that it receives
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-
