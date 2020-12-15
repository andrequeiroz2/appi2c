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
                location.href = "/logout";
            }
        },
        cancel: {
            keys: ['esc'],
            action: function () {
                //close
            },
        },
    }
});

