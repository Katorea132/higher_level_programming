#!/usr/bin/node
const leti = +process.argv[2];
if (Number.isInteger(leti)) {
  console.log('My number: ' + leti);
} else {
  console.log('Not a number');
}
