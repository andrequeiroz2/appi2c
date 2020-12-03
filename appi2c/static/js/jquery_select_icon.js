$.confirm({
    useBootstrap: false,
    scrollToPreviousElementAnimate: true,
    draggable: false,
    bgOpacity: 0.90,
    boxWidth: '50%',
    title: 'Icon',
    type: 'blue',
    content:
        '' +
        '<table class="table" style="width:70%">' +
        '<thead>' +
        '<tr>' +
        '<th>Select</th>' +
        '<th>Icon</th>' +
        '</thead>' +
        '<tbody>' +
        '{% for icon in icons %}' +
        '<tr>' +
        '<td>' +
        '<div class="radio">' +
        '<input type="radio" id="{{icon.id}}" value={{icon.id}} name="icon-select" identify="{{ icon.html_class }}">' +
        '</div>' +
        '</td>' +
        '<td>' +
        '<div class="radiotext">' +
        '<i class="{{ icon.html_class }}" aria-hidden="true"></i>' +
        '</div>' +
        '</td>' +
        '</tr>' +
        '{% endfor %}' +
        '</tboby>' +
        '</table>' +
        '',
    buttons: {
        formSubmit: {
            text: 'Select',
            btnClass: 'btn-blue',
            action: function () {
                var selected = $('input[name=icon-select]:checked').val();
                var icon_class = $('input[name=icon-select]:checked').attr('identify');
                if (!selected) {
                    $.alert({
                        useBootstrap: false,
                            scrollToPreviousElementAnimate: false,
                            draggable: false,
                            bgOpacity: 0.90,
                            boxWidth: '40%',
                            icon: 'far fa-frown',
                            title: 'Ooo nooo!',
                            content: 'Select a Icon',
                            type: 'red',
                    });
                    return false;
                }
                $("iconid").value = selected;
                $("#icon_class").addClass(icon_class); 
            }
        },
        close: function () {
        },
    },
    onContentReady: function () {
        var jc = this;
        this.$content.find('form').on('submit', function (e) {
            e.preventDefault();
            jc.$$formSubmit.trigger('click');
        });
    }
});