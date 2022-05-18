#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;
let idx;
let tmp;
let count = 0;
const dict = {};

axios.get(args[2])
  .then(function (response) {
    for (idx = 0; idx < response.data.length; idx++) {
      if (tmp !== response.data[idx].userId) {
        count = 0;
      }
      if (response.data[idx].completed === true) {
        count += 1;
        dict[response.data[idx].userId] = count;
      }
      tmp = response.data[idx].userId;
    }
    console.log(dict);
  });
