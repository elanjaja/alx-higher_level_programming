#!/usr/bin/node

// script that prints the first argument passed to it

const command = process.argv[2];

if (!command) {
  console.log('No argument');
} else {
  console.log(command);
}
