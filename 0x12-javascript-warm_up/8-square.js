#!/usr/bin/node
const leti = +process.argv[2];
if (Number.isInteger(leti)) {
  for (let i = 0; i < leti; i++) {
    console.log('X'.repeat(leti));
  }
} else {
  console.log('Missing size');
}
