if (data['status'] === 'error') {
    $.alert({
        useBootstrap: false,
        scrollToPreviousElementAnimate: false,
        draggable: false,
        bgOpacity: 0.90,
        boxWidth: '40%',
        icon: 'far fa-frown',
        title: 'Ooo nooo!',
        content: data['msg'],
        type: 'red',
        buttons: {
            calcel: {
                text: " Ok ",
                btnClass: 'btn-red',
                keys: ['enter', 'esc'],
                action: function () {
                }
            },
        }
    });
}
else {
    $.confirm({
        useBootstrap: false,
        scrollToPreviousElementAnimate: false,
        draggable: false,
        bgOpacity: 0.90,
        boxWidth: '40%',
        icon: 'far fa-laugh',
        title: 'Yess!',
        content: data['msg'],
        type: 'blue',
        buttons: {
            cancel: {
                text: " Ok ",
                btnClass: 'btn-blue',
                keys: ['enter', 'esc'],
                action: function () {
                }
            },
        }
    });
}
