#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w <= 0 || isNaN(w) || h <= 0 || isNaN(h)) {
        return;
    } else {
        this.width = w;
        this.height = h;
      }
  }
};
