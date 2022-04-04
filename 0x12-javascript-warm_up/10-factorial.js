#!/usr/bin/node

const argv = process.argv;
console.log(factorial(parseInt(argv[2])));

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
