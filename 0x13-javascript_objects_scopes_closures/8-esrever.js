#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (let idx = 0; idx < list.length; idx++) {
    newList[idx] = list[list.length - 1 - idx];
  }
  return newList;
};
