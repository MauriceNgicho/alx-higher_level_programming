#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const filepath = process.argv[3];

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(filepath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
