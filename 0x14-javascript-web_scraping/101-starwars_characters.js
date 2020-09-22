#!/usr/bin/node
const req = require('request');
req(`http://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, bod) => {
  if (err) throw new Error(err);
  for (const character of JSON.parse(bod).characters) {
    req(character, (err, res, bod) => {
      if (err) throw new Error(err);
      console.log(JSON.parse(bod).name);
    });
  }
});
