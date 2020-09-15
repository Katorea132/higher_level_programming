#!/usr/bin/node

function factorial (a) {
  if (!a || a < 2) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(+process.argv[2]));
