$(document).ready(function () {
  // Fetch JSON data
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Extract list of movis from the response.
    const movies = data.results;
    // Iterate though each movie in a list.
    movies.forEach(movie => {
      // Creates a new <li> element for each movie title and appends
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
