#!/usr/bin/node
exports.nbOccurences = function (list, element) {
  return list.filter(ele => ele === element).length;
};
