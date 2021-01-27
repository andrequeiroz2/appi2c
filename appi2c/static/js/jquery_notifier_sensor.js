$(function () {
    $.ajax({
        method: "POST",
        url: "/list/notifier/ajax",
        success: function (data) {
            if (data.length === 0) {
                alert_no_notifier();
            }
            else {
                $.confirm({
                    backgroundDismiss: false,
                    useBootstrap: false,
                    scrollToPreviousElementAnimate: true,
                    draggable: false,
                    bgOpacity: 0.90,
                    boxWidth: '60%',
                    type: 'blue',
                    title: 'Set limits for Notification',
                    content:
                        '<div class="form-group">' +
                        '<section class="section">' +
                        '<strong>Max Limit: </strong>' +
                        '<p><input id="max_limit" class="input is-primary" type="text" ></p>' +
                        '</br>' +
                        '<strong>Min  Limit: </strong>' +
                        '<p><input id="min_limit" class="input is-primary" type="text" ></p>' +
                        '</br>' +
                        '<div class="field">' +
                        '<div class="control">' +
                        '<p><strong>Notifier: </strong></p>' +
                        '<div class="select is-primary">' +
                        '<p><select id="select"></select ></p>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</br>' +
                        '<div class="field">' +
                        '<div class="control">' +     
                        '<p><strong>Level: </strong></p>' +
                        '<div class="select is-primary">' +
                        '<select id="level">' +
                        '<option>Low</option>' +
                        '<option>Medium</option>' +
                        '<option>High</option>' +
                        '<option>Critical</option>' +
                        '</select >' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</section>' +
                        '</div>',
                    buttons: {
                        ok: {
                            text: "Ok",
                            btnClass: 'btn-blue',
                            keys: ['enter'],
                            action: function () {
                                let max_limit = $("#max_limit").val();
                                let min_limit = $("#min_limit").val();
                                let bot = select.options[select.selectedIndex];
                                let level1 = level.options[level.selectedIndex];
    
                                if (max_limit === "" && min_limit === "") {
                                    alert_no_limits();
                                }
                                else {
                                    $.ajax({
                                        method: "POST",
                                        url: "/register/limits/sensor",
                                        contentType: 'application/json;charset=UTF-8',
                                        data: JSON.stringify({ 'id': params['id'],
                                                               'max_limit': max_limit,
                                                               'min_limit': min_limit,
                                                               'bot': bot.text,
                                                               'level': level1.text
                                                             }),
                                        dataType: "json",
                                    
                                        statusCode: {
                                            400: function () {
                                                $.alert({
                                                    useBootstrap: false,
                                                    scrollToPreviousElementAnimate: false,
                                                    draggable: false,
                                                    bgOpacity: 0.90,
                                                    boxWidth: '40%',
                                                    icon: 'far fa-frown',
                                                    title: 'Ooo nooo!',
                                                    content: 'Invalid Credentials!',
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
                                                return false;
                                            },
                                            error: function (err) {
                                                console.log(err);
                                            }
                                        },
                                    });
                                };
                            },
                        },
                        cancel: {
                            text: "Cancel",
                            keys: ['esc'],
                            action: function () {

                            }
                        },
                    },
                    onContentReady: function () {
                        for (x in data) {
                            let value = document.getElementById("select");
                            let option = document.createElement("option");
                            option.text = data[x];
                            value.add(option);
                        };

                        $.ajax({
                            method: "POST",
                            url: "/get/data/limit",
                            contentType: 'application/json;charset=UTF-8',
                            data: JSON.stringify({ 'id': params['id']}),
                            dataType: "json",
                            success: function (get_data) {
                                $('#max_limit').val(get_data['max']);
                                $('#min_limit').val(get_data['min']); 

                                $("#select").val(get_data['notifier']).change();
                                $("#level").val(get_data['level_limit']).change();
                            },
                        });
                    }
                });
            }
        },
    });
});

function alert_no_notifier() {
    $.alert({
        useBootstrap: false,
        scrollToPreviousElementAnimate: false,
        draggable: false,
        bgOpacity: 0.90,
        boxWidth: '40%',
        icon: 'far fa-frown',
        title: 'Ooo nooo!',
        content: 'You do not have a registered notifier!',
        type: 'red',
        buttons: {
            ok: {
                text: "Ok",
                keys: ['enter', 'esc'],
                action: function () {

                },
            },
        },
    });
};

function alert_no_limits() {
    $.alert({
        useBootstrap: false,
        scrollToPreviousElementAnimate: false,
        draggable: false,
        bgOpacity: 0.90,
        boxWidth: '40%',
        icon: 'far fa-frown',
        title: 'Ooo nooo!',
        content: 'No limit values ​​have been set!',
        type: 'red',
        buttons: {
            ok: {
                text: "Ok",
                keys: ['enter', 'esc'],
                action: function () {

                },
            },
        },
    });
};

