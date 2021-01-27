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
    '<div class="form-group">' +
    '<section class="section">' +
    '<div class="field">' +
    '<a href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="dashboard">Historic</a>' +
    '</br>' +
    '<a href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="details">Details</a>' +
    '</br>' +
    '<a href=""  type="submit" class="button is-medium is-fullwidth is-primary" id="clear">Clear Topic</a>' +
    '</div>' +
    '</section>' +
    '</div>',

  buttons: {
    ok: {
      isHidden: true
    }
  },
});


$(function () {
  $("#dashboard").click(function (ev) {
    ev.preventDefault();
    let param = { 'id': params['id'] };

    $.ajax({
      method: "POST",
      url: "/data/historic",
      contentType: 'application/json;charset=UTF-8',
      data: JSON.stringify(param),
      dataType: "json",

      success: function (data_json) {

        $.confirm({
          useBootstrap: false,
          scrollToPreviousElementAnimate: true,
          draggable: false,
          bgOpacity: 0.10,
          boxWidth: '70%',
          type: 'blue',
          title: '',
          content:
            '' +
            '<div id="chart" style="width:90%; height=90%"></div>' +
            '',
          buttons: {
            close: function () {
            },
          },
          onContentReady: function () {

            if (params['type'] === 'sensor') {
              var options = {
                series: [
                  {
                    name: data_json['measure'],
                    data: data_json.data.data,
                  },
                ],

                chart: {
                  height: 350,
                  type: 'line',
                  dropShadow: {
                    enabled: true,
                    color: '#000',
                    top: 18,
                    left: 7,
                    blur: 10,
                    opacity: 0.2
                  },
                  toolbar: {
                    show: true,
                    tools: {
                      download: true,

                    },
                    export: {
                      csv: {
                        filename: undefined,
                        columnDelimiter: ',',
                        headerCategory: 'category',
                        headerValue: 'value',
                        dateFormatter(timestamp) {
                          return new Date(timestamp).toDateString()
                        }
                      }
                    },
                  },
                },

                colors: ['#77B6EA'],
                dataLabels: {
                  enabled: true,
                },
                stroke: {
                  curve: 'smooth'
                },
                title: {
                  text: 'Device: ' + data_json['name'] + ' / ' +'Measure: ' + data_json['measure'] + ' / ' + 'Scale: ' + data_json['postfix'],
                  align: 'left'
                },
                grid: {
                  borderColor: '#e7e7e7',
                  row: {
                    colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                    opacity: 0.5
                  },
                },
                markers: {
                  size: 1
                },
                xaxis: {
                  categories: data_json.data.date,
                  title: {
                    text: 'Date'
                  }
                },
                yaxis: {
                  type: 'Text',
                  title: {
                    text: data_json['measure']
                  },
                  min: -60,
                  max: 120
                },
                legend: {
                  position: 'top',
                  horizontalAlign: 'right',
                  floating: true,
                  offsetY: -25,
                  offsetX: -5
                }
              };
              var chart = new ApexCharts(document.querySelector("#chart"), options);
              chart.render();
            };


            if (params['type'] === 'switch') {
              var on_off = []
              for (x in data_json.data.data) {
                if (data_json.data.data[x] === "On") {
                  on_off.push(100)
                } else {
                  on_off.push(-100)
                }
              }

              var options = {
                series: [
                  {
                    name: 'State',
                    data: on_off,
                  }
                ],

                chart: {
                  type: 'bar',
                  height: 350
                },

                title: {
                  text: 'Device: ' + data_json['name'],
                  align: 'left'
                },

                plotOptions: {
                  bar: {
                    colors: {
                      ranges: [{
                        from: -100,
                        to: -46,
                        color: '#F15B46'
                      }, {
                        from: -45,
                        to: 0,
                        color: '#FEB019'
                      }]
                    },
                    columnWidth: '80%',
                  }
                },
                dataLabels: {
                  enabled: false,
                },
                yaxis: {
                  title: {
                    text: 'State',
                  },
                  labels: {
                     formatter: function (y) {
                       if (y === 100){
                        return "On";      
                       }else{
                        return "Off";
                       }
                    }
                  },
                  axisTicks: {
                    show: false,
                    borderType: 'solid',
                    color: '#78909C',
                    width: 6,
                    offsetX: 0,
                    offsetY: 0
                },
                },
                xaxis: {
                  categories: data_json.data.date,
                  labels: {
                    rotate: -90
                  },
                  title: {
                    text: 'Date'
                  },
                }
              };
         

              var chart = new ApexCharts(document.querySelector("#chart"), options);
              chart.render();
            };
          },
        });
      },


      statusCode: {
        405: function () {
          $.alert({
            useBootstrap: false,
            scrollToPreviousElementAnimate: false,
            draggable: false,
            bgOpacity: 0.90,
            boxWidth: '40%',
            icon: 'far fa-frown',
            title: 'Ooo nooo!',
            content: 'This device has no data to display!',
            type: 'red',
            buttons: {
              ok: {
                text: "Ok",
                keys: ['enter', 'esc'],
                action: function () {
                }
              },
            }
          });
        },
        error: function (err) {
          console.log(err);
        }
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
      bgOpacity: 0.10,
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

            let param = { 'topic': params['pub'] };

            $.ajax({
              method: "POST",
              url: "/clear",
              contentType: 'application/json;charset=UTF-8',
              data: JSON.stringify(param),
              dataType: "json",

              success: function () {
                $("#success").append("Yess clean topic.");
                $("#cleartopic").prop("disabled", true);
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
      bgOpacity: 0.10,
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
