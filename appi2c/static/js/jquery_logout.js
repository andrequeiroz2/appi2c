$.confirm({
    useBootstrap: false,
    scrollToPreviousElementAnimate: false,
    draggable: false,
    bgOpacity: 0.90,
    boxWidth: '40%',
    icon: 'far fa-sad-tear',
    title: 'Oooo nooo!',
    content: 'Confirm Logout?',
    type: 'red',
    buttons: {
        ok: {
            text: "Confirm",
            btnClass: 'btn-blue',
            keys: ['enter'],
            action: function () {
                $.ajax({
                    method: "POST",
                    url: "/logout",
                    contentType: 'application/json;charset=UTF-8',
                    data: JSON.stringify({ 'action': 'logout' }),
                    dataType: "json",
                    success: function (data) {
                        $.ajax({
                            url: "/index"
                        });
                        location.reload();
                        return true;
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
                                title: 'Error!',
                                content: 'Very strange! I certainly made a mistake',
                                type: 'red',
                            });
                            return false;
                        },
                        error: function (err) {
                            console.log(err);
                        }
                    },
                });
            }
        },
        cancel: function () {
            //close
        },
    }
});

