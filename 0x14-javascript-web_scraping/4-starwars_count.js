#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line
const Id = '18'; // Wedge Antilles has ID 18
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${Id}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    // Parse JSON response
    const data = JSON.parse(body);
    // Extract movie array
    const films = data.results;

    // Count movies where Wedge Antilles appears
    const count = films.filter(film => film.characters.includes(characterUrl)).length;

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
