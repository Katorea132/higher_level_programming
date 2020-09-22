#!/usr/bin/node
const files = require('fs');
files.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  err && console.log(err);
});
