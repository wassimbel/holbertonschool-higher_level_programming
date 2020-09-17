#!/usr/bin/node
const len = process.argv.length - 2;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let a = []
  a = process.argv.slice(2).sort();
  console.log(a[len - 2]);
}
