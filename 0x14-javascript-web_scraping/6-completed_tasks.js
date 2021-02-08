#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const content = {};
request(url, (error, response, body) => {
  const data = JSON.parse(body);
  if (error) {
    throw error;
  } else {
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        if (content[data[i].userId]) {
          content[data[i].userId] += 1;
        } else {
          content[data[i].userId] = 1;
        }
      }
    }
    console.log(content);
  }
});
