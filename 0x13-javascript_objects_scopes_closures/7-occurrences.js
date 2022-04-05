#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let idx = 0; idx < list.length; idx++) {
    if (list[idx] === searchElement) {
      count += 1;
    }
  }

  return count;
};
