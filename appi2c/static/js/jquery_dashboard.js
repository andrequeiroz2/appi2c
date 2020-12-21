

$.confirm({
  backgroundDismiss: true,
  useBootstrap: false,
  scrollToPreviousElementAnimate: false,
  draggable: false,
  title: '',
  bgOpacity: 0.90,
  boxWidth: '50%',
  type: 'blue',
  content:
    '' +
    '<form action="">' +
    '<div class="form-group">' +
    '<section class="section">' +
    '<div class="field">' +
    '<a href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="dashboard">Dashboard</a>' +
    '</br>' +
    '<a href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="realtime">Real Time</a>' +
    '</br>' +
    '<a href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="details">Details</a>' +
    '</br>' +
    '<a href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="free">Free Publish</a>' +
    '</div>' +
    '</section>' +
    '</div>' +
    '</form>' +
    '',
  buttons: {
    ok: {
      isHidden: true
    }
  },
});


$(function () {
  $("#nada").click(function (ev) {
    ev.preventDefault();
    $.confirm({
      useBootstrap: false,
      scrollToPreviousElementAnimate: true,
      draggable: false,
      bgOpacity: 0.90,
      boxWidth: '70%',
      type: 'blue',
      title: '',
      content:
        '' +
        '<div id="chart" class="size"></div>' +
        '',

      buttons: {
        close: function () {
        },
      },
      onContentReady: function () {


      },
    });
  });
});

$(function () {
  $("#details").click(function (ev) {
    ev.preventDefault();
    $.confirm({
      useBootstrap: false,
      scrollToPreviousElementAnimate: true,
      draggable: false,
      bgOpacity: 0.90,
      boxWidth: '60%',
      title: params['title'],
      content: params['msg'],
      type: 'blue',
      buttons: {
        ok: {
          text: "Ok",
          btnClass: 'btn-blue',
          keys: ['enter', 'esc'],
          action: function () {

          }
        },
      }
    });
  });
});

