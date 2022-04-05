#!/usr/bin/node

exports.logMe = function (item) {
  console.log((arguments.length - 1).toString() + ': ' + item);
};
