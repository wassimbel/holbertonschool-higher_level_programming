#!/usr/bin/node
const l = require('./100-data').list;
const maplist = l.map((x, y) => x * y);
console.log(l);
console.log(maplist);
