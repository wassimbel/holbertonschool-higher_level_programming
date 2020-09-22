#!/usr/bin/node

const fs = require('fs');
const arg = process.argv[2];

fs.readFile(arg, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  }
  console.log(arg);
});
