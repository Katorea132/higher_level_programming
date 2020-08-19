#!/bin/bash
# catch 'em all
curl -L -X PUT -H "Origin:HolbertonSchool" -d "user_id=98" -s "0.0.0.0:5000/catch_me"
