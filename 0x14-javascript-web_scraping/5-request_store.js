#!/usr/bin/node
const req = require('request');
const files = require('fs');
req(process.argv[2]).pipe(files.createWriteStream(process.argv[3]));
