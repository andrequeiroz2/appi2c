$.confirm({
    useBootstrap: false,
    scrollToPreviousElementAnimate: true,
    draggable: false,
    bgOpacity: 0.90,
    columnClass: 'col-sm-6',
    type: 'blue',
    icon: 'far fa-laugh',
    title: 'Login!',
    content:
        '' +
        '<form method="POST" action="" class="formName">' +
        '<div class="form-group">' +
        '<div class="field">' +
        '<label>Enter your credentials</label>' +
        '<br>' +
        '</div>' +
        '<div class="field">' +
        '<p>User Name</p>' +
        '<input type="text" autocomplete="username" placeholder="Your username" class="name input is-info" required />' +
        '<em id="required_name"></em>' +
        '<br>' +
        '</div>' +
        '<div class="field">' +
        '<p>Password</p>' +
        '<input type="password" autocomplete="current-password" placeholder="Your email" class="pass input is-info" required />' +
        '<em id="required_pass"></em>' +
        '</div>' +
        '</div>' +
        '</form>' +
        '',
    buttons: {
        formSubmit: {
            text: 'Confirm',
            btnClass: 'btn-blue',
            keys: ['enter'],
            action: function () {
                var name = this.$content.find('.name').val();
                if (!name) {
                    $("#required_name").empty();
                    $("#required_name").append("provide a valid name.").css("color", "#ff8080");
                    return false;
                }
                if ((name.length < 5) || (name.length > 30)) {
                    $("#required_name").empty();
                    $("#required_name").append("Min 5 and Max 30 digits.").css("color", "#ff8080");
                    return false;
                }
                var pass = this.$content.find('.pass').val();
                if (!pass) {
                    $("#required_pass").empty();
                    $("#required_pass").append("provide a valid password.").css("color", "#ff8080");
                    return false;
                }
                if ((pass.length < 5) || (pass.length > 30)) {
                    $("#required_pass").empty();
                    $("#required_pass").append("Min 5 and Max 30 digits.").css("color", "#ff8080");
                    return false;
                }
                if ((!name) || (!pass)) {
                    return false;
                }

                $.ajax({
                    method: "POST",
                    url: "/login",
                    contentType: 'application/json;charset=UTF-8',
                    data: JSON.stringify({ 'username': name, 'password': pass }),
                    dataType: "json",
                    success: function (data) {
                        location.href = "/index";
                    },
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
                }
                );
            }
        },
        cancel: {
            keys: ['esc'],
            action: function () {
                        //close
                    },
        },
    },
    onContentReady: function () {
        // bind to events
        var jc = this;
        this.$content.find('form').on('access', function (e) {
            // if the user submits the form by pressing enter in the field.
            e.preventDefault();
            jc.$$formSubmit.trigger('click'); // reference the button and click it
        });
    }
});

$(function () {
    $(".name").on('click', function () {
        $("#required_name").empty();
    });
});

$(function () {
    $(".pass").on('click', function () {
        $("#required_pass").empty();
    });
});


