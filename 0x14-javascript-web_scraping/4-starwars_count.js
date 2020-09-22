#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
request(arg, (error, response, body) => {
  let k = 0;
  const data = JSON.parse(body).results;
  if (error) {
    throw error;
  } else {
    for (let i = 0; i < data.length; i++) {
      for (let j = 0; j < data[i].characters.length; j++) {
        if (data[i].characters[j].includes('/18')) {
          k++;
        }
      }
    }
    console.log(k);
  }
});
