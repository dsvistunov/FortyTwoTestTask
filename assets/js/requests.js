$(document).ready(function () {
    // Requests
    var prior = 0;
    $("#prior").click(function () {
        if ($("#prior").val()=='Prior 1') {
            prior = 0;
            $("#prior").attr('value', 'Prior 0');
        }
        else {
            prior = 1;
            $("#prior").attr('value', 'Prior 1');
        }
    });
    setInterval(function () {
        $.ajax({
            url: '/requests/',
            method: 'get',
            success: function (data) {
                var html = '';
                if (prior) {
                    data = Object.values(data).reverse();
                }
                $.each(data, function (key, value) {
                    key++;
                    html += "<a href='" + value.fields.http_inf + "'>" + key + ". " + value.fields.http_inf + "</a><br>"
                });
                $(".requests").html(html);
            }
        })
    }, 2000);
});