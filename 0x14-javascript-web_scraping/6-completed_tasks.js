#!/usr/bin/node
const req = require('request');
const didi = {};
req(process.argv[2], (err, res, bod) => {
  if (err) throw new Error(err);
  for (const task of JSON.parse(bod)) {
    didi[task.userId] = (didi[task.userId] || 0);
    if (task.completed) {
      didi[task.userId] += 1;
    }
  }
  console.log(didi);
});
