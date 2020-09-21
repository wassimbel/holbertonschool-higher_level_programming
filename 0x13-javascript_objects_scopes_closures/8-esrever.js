#!/usr/bin/node
exports.esrever = function (list) {
//  return list.reverse();
  const rev = [];
  let i = 0;
  for (let j = list.length - 1; j >= 0; j--, i++) {
    rev[j] = list[i];
  }
  return (rev);
};
