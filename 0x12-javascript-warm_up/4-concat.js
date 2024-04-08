#!/usr/bin/node

// script that prints two arguments passed to it, in the following format: “is'

const command1 = process.argv[2];
const command2 = process.argv[3];

const result = command1 + ' is ' + command2;
console.log(result);
