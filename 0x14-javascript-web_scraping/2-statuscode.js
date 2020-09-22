#!/usr/bin/node
const req = require('request');
req(process.argv[2], (err, res, bod) => {
  err && console.log(err);
  res && console.log('code: ', res.statusCode);
});
