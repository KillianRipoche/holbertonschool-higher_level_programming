fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then(data => {
    const translatedHello = data.hello;
    document.getElementById('hello').textContent = translatedHello;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
