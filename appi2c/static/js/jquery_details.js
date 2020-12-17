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