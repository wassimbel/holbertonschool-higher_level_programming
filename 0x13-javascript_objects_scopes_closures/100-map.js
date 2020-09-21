#!/usr/bin/node
const l = require('./100-data').list;
const map_l = l.map((x, y) => x * y);
console.log(l);
console.log(map_l);
