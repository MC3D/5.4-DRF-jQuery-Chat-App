(function($){
    $(function(){

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax("/api/message/", {
            'dataType': 'json',
            'error': function(resp, err){console.log(resp,err)},
            'success': function(data) {
                // console.log('data', data);
                data = data.sort().reverse();
                data.forEach(function(item){
                    $('.row').append('<p>' + item.text + '</p>');
                });
            }
        });
    });
})(jQuery);