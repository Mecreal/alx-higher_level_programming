#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  let temp;

  for (let i = 0; i < list.length / 2; i++) {
    temp = list[i];
    list[i] = list[list.length - (1 + i)];
    list[list.length - (1 + i)] = temp;
  }
  return (list);
};
