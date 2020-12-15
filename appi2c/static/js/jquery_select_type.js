$.confirm({
    useBootstrap: false,
    scrollToPreviousElementAnimate: true,
    draggable: false,
    bgOpacity: 0.90,
    boxWidth: '50%',
    title: params['title'],
    content: params['types'], 
    type: 'blue',
    buttons: {
    cancel: {
        text: "Cancel",
        keys: ['esc'],
        action: function () {

        }
    },
}
});
