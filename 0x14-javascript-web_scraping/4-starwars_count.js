#!/usr/bin/node
const req = require('request');
const fin = 'https://swapi-api.hbtn.io/api/people/18/';
req(process.argv[2], (err, res, bod) => {
  if (err) throw new Error(err);
  let count = 0;
  for (const mov of JSON.parse(bod).results) {
    if (mov.characters.includes(fin)) {
      count += 1;
    }
  }
  console.log(count);
});
