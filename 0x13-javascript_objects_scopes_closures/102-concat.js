#!/usr/bin/node
const fs = require('fs');
args = process.argv
const text1 = fs.readFileSync(args[2]);
const text2 = fs.readFileSync(args[3]);
fs.writeFileSync(args[4], text1 + text2);
