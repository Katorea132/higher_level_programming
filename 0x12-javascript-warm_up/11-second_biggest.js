#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  let highest;
  let almostHighest;
  if (+process.argv[2] > +process.argv[3]) {
    highest = +process.argv[2];
    almostHighest = +process.argv[3];
  } else {
    highest = +process.argv[3];
    almostHighest = +process.argv[2];
  }
  for (let i = 4; +process.argv[i]; i++) {
    if (+process.argv[i] > highest) {
      almostHighest = highest;
      highest = +process.argv[i];
    } else if (+process.argv[i] > almostHighest) {
      almostHighest = +process.argv[i];
    }
  }
  console.log(almostHighest);
}
