$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, Status) => {
  $.each(data.results, (index, elem) => {
    $('UL#list_movies').append('<li>' + elem.title + '</li>');
  });
});
