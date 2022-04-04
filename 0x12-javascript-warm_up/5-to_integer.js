#!/usr/bin/node

const { argv } = require('process');
const arg = parseInt(argv[2]);
if (Number(arg)) {
  console.log('My number: ' + Number(arg));
} else {
  console.log('Not a number');
}
