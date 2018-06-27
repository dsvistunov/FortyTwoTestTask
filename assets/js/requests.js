$(document).ready(function () {
    setInterval(function () {
        $.ajax({
            url: '/requests/',
            method: 'get',
            success: function (data) {
                var html = '';

                $.each(data, function (key, value) {
                    key++;
                    html += "<a href='" + value.fields.http_inf + "'>" + key + ". " + value.fields.http_inf + "</a><br>"
                });
                $(".requests").html(html);
            }
        })
    }, 2000);
});