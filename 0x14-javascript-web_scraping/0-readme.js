#!/usr/bin/node
const files = require('fs');
files.readFile(process.argv[2], 'utf-8', (err, dat) => {
  console.log(err || dat);
});
