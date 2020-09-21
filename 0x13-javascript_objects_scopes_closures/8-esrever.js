#!/usr/bin/node
exports.esrever = function (list) {
  const lili = [];
  for (let i = list.length - 1; i > -1; i--) {
    lili.push(list[i]);
  }
  return lili;
};
