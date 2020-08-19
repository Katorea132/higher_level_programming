#!/bin/bash
# Posts a JSON
curl -X POST -d @"$2" -H "Content-Type: application/json" -s "$1"
