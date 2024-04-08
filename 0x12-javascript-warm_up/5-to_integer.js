#!/usr/bin/node

//  script that prints My number: <first argument converted in integer>

const command = process.argv[2];

if (!command) {
  console.log('Not a number');
} else {
  const value = parseInt(command, 10);
  if (isNaN(value)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + value);
  }
}
