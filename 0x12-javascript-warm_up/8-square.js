#!/usr/bin/node

const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let idx = 0; idx < size; idx++) {
    console.log('X'.repeat(size));
  }
}
