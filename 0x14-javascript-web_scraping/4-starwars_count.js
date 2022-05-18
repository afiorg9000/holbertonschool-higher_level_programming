#!/usr/bin/node
const axios = require('axios');
const ID = '18';
let total = 0;

axios.get(process.argv[2])
  .then(res => {
    const films = res.data.results ? res.data.results : [];
    const size = films.length;
    for (let i = 0; i < size; i++) {
      films[i].characters.forEach(char => {
        if (char.includes(ID)) total++;
      });
    }
    console.log(total);
  })
  .catch(err => {
    console.log('Error:', err);
  });
