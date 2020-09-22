#!/usr/bin/node
const req = require('request');
req(`http://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, bod) => {
  err && console.log(err);
  console.log(JSON.parse(bod).title);
});
