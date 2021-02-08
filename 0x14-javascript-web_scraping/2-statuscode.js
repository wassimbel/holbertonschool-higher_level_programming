#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    throw error;
  }
  console.log('code:', response && response.statusCode);
});
