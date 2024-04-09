#!/usr/bin/node

// a script that imports an array and computes a new array

const data = require('./100-data.js');
const list = data.list;

let count = -1;
const val = list.map((l) => {
  count++;
  return l * count;
});

console.log(list);
console.log(val);
