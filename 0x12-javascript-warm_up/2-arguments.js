#!/usr/bin/node
// Script that check if the args are found or not

const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
  }
