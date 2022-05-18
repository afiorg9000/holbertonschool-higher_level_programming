#!/usr/bin/node
const fs = require('fs');
const axios = require('axios');

axios.get(process.argv[2])
  .then(res => {
    fs.writeFile(process.argv[3], res.data, err => {
      if (err) {
        return console.log(err);
      }
    });
  });
