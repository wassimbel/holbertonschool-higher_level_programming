#!/usr/bin/node
const fs = require('fs')
const arg = process.argv[2];
fs.readFileSync(arg, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
console.log(data);
});
