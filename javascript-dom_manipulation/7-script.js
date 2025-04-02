fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const films = data.results;
    const listMovies = document.getElementById('list_movies');
    films.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      listMovies.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching movie data:', error);
  });
