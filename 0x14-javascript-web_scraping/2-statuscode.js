#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];
let statusCode;

axios.get(url).then((response) => {
	console.log(`code: ${response.status}`);
}).catch((error) => {
	console.log('Error', error);
});
