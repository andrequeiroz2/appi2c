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
    '<a href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="clear">Clear Topic</a>' +
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
  $("#clear").click(function (ev) {
    ev.preventDefault();
    $.confirm({
      useBootstrap: false,
      scrollToPreviousElementAnimate: true,
      draggable: false,
      bgOpacity: 0.90,
      boxWidth: '60%',
      title: 'Clear Topic',
      content:

        '<form action="">' +
        '<div class="form-group">' +
        '<section class="section">' +
        '<p>If broker keeps retained messages for this topic:</p>' +
        '<strong>' +
        params['pub'] +
        '</strong>' +
        '<p>An empty string will be sent to the topic.</p>' +
        '<br>' +
        '<p id="success" style="color:blue"></p>' +
        '<div class="columns">' +
        '<div class="column is-one-quarter">' +
        '<button href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="cleartopic">Clear</button>' +
        '</div>' +
        '</div>' +
        '</section>' +
        '</div>' +
        '<form >',

      type: 'blue',
      buttons: {

        cancel: {
          text: "Cancel",
          keys: ['esc'],
          action: function () {

          }
        },
      },
      onContentReady: function () {

        $(function () {
          $("#cleartopic").click(function (ev) {
            ev.preventDefault();
            
            let param = {'topic': params['pub']};

            $.ajax({
              method: "POST",
              url: "/clear",
              contentType: 'application/json;charset=UTF-8',
              data: JSON.stringify(param),
              dataType: "json",

              success: function () {
                $("#success").append("Yess clean topic.");
                $("#cleartopic").prop("disabled",true);
              },
            });
          });
        });
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
