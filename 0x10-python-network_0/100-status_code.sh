#!/bin/bash
# Only status code matters
curl -w "%{http_code}" -s "$1" -o /dev/null
