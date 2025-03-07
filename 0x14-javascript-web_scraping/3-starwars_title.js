#!/usr/bin/node

const request = require('request');
const Id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${Id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  console.log(movie.title);
});
