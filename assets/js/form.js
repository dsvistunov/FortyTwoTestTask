$(document).ready(function () {
    $('#loader').hide();
    $('form').submit(function (event) {
        event.preventDefault();
        if (confirm('Are you shure?')) {
            var form = $(this);
            var formData = new FormData(form[0]);
            formData.append('photo', $('input[type=file]')[0].files[0]);
            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            var csrftoken = getCookie('csrftoken');
            $.ajaxSetup({
                beforeSend: function (xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
            $.ajax({
                url: '/edit/',
                method: 'post',
                type: 'post',
                data: formData,
                cache: false,
                processData: false,
                contentType: false,
                beforeSend: function () {
                    $('#loader').show();
                },
                success: function (response) {
                    $('#loader').hide();
                    if (response.msg) {
                        var html = '<p>' + response.msg + '</p>';
                        $('#status').html(html)
                    }
                    $.each(response, function (key, value) {
                        var node = '#id_' + key;
                        var message = '<span style="color: red; position: absolute; width: 180px;">' + value + '</span>';
                        $(node).after(message);
                    })

                }
            });
            return false;
        }
    });
    //Datepicker
    $('#id_date_birth').datepicker({ dateFormat: 'yy-mm-dd' });
});
