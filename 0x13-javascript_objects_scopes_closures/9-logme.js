#!/usr/bin/node
// function that returns the reversed version of a list

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
