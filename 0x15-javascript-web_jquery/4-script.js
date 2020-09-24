#!/usr/bin/node
$('DIV#toggle_header').off('click').click(() => $('header').toggleClass('red green'));
