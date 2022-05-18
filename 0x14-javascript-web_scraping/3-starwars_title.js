#!/usr/bin/node

const axios = require('axios');
const ID = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${ID}`)
  .then(res => {
    console.log(res.data.title);
  });
