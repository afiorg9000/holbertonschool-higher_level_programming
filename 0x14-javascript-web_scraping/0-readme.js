#!/usr/bin/node

const fs = require('fs');
const FileName = process.argv[2];

fs.readFile(FileName, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
