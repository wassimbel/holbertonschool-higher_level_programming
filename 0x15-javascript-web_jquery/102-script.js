$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const userIN = 'https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val();
    $.get(userIN, (data, Status) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
