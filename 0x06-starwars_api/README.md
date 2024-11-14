# 0x06. Star Wars API

## Project Overview

This project requires creating a Node.js script that interacts with the Star Wars API to fetch and display character names from a specific Star Wars movie. The script takes a movie ID as a command-line argument, retrieves the list of characters in the movie, and prints each character's name in the order they appear in the API’s response.

## Requirements

- **Node.js version**: 10.14.x
- **Operating System**: Ubuntu 20.04 LTS
- **Code Styling**: Must adhere to `semistandard` style with semicolons.

## Concepts Covered

- Making HTTP requests using Node.js
- Asynchronous programming and callbacks
- Working with RESTful APIs
- Using command-line arguments in Node.js
- Array manipulation and iteration

## Installation

1. **Install Node.js (version 10):**
   ```bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Install `semistandard`:** (for code linting)
   ```bash
   sudo npm install semistandard --global
   ```

3. **Install the `request` module:** (to make HTTP requests)
   ```bash
   sudo npm install request --global
   export NODE_PATH=/usr/lib/node_modules
   ```

## Usage

1. Clone or navigate to the project directory.

2. Create the script `0-starwars_characters.js` with the following structure:

   ```javascript
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
     Promise.all(characterUrls.map(url =>
       new Promise((resolve, reject) => {
         request(url, (error, response, body) => {
           if (error) reject(error);
           else resolve(JSON.parse(body).name);
         });
       })
     ))
     .then(names => {
       names.forEach(name => console.log(name));
     })
     .catch(err => console.error(err));
   }
   ```

3. **Make the script executable:**
   ```bash
   chmod +x 0-starwars_characters.js
   ```

4. **Run the script with a Movie ID:**
   ```bash
   ./0-starwars_characters.js <movie_id>
   ```

   Example:
   ```bash
   ./0-starwars_characters.js 3
   ```

   Output:
   ```
   Luke Skywalker
   C-3PO
   R2-D2
   ...
   ```

## Explanation of Code

1. **Command-Line Argument**: `process.argv[2]` gets the Movie ID.
2. **API Request for Movie Data**: Uses `request` to fetch movie data from the Star Wars API.
3. **Fetch Character Names**: The `fetchCharacters` function sends a request to each character URL, retrieves names, and prints them in the correct order using `Promise.all`.

## Additional Information

- **Code Style**: This project follows the `semistandard` style guide with semicolons.
- **Errors**: If the movie data is not accessible, or a character cannot be fetched, appropriate error messages will be displayed.
- **Exit Codes**: The script will exit with code `1` if the Movie ID argument is missing.

## Author

[fjbaafi18@gmail.com] : This project was created as part of the **ALX Interview Preparation** tasks.

--- 

This `README.md` provides an overview, usage instructions, code explanation, and setup details for the **Star Wars Characters** project.
