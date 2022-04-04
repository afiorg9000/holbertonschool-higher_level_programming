#!/usr/bin/node

const x = process.argv[2];
if (x) {
    for (let tmp = 0; tmp < x; tmp++) {
      console.log('C is fun');
    }
} else { console.log('Missing number of occurrences')};