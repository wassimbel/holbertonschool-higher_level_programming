#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

const arg = process.argv[2];
console.log(factorial(Number.parseInt(arg)));
