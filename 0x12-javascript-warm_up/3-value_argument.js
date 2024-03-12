#!/usr/bin/node
// Script that return all the args

const { argv } = require('node:process');

// print process.argv
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
