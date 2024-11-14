#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    fetchCharacters(characterUrls);
  } else {
    console.error(`Failed to fetch movie data: ${response.statusCode}`);
  }
});

function fetchCharacters(characterUrls) {
  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      console.log(JSON.parse(body).name);
    });
  });
}
