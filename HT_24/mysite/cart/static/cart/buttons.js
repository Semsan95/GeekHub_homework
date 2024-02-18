$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    const csrftoken = getCookie('csrftoken');
    

    $('button[name="add"]').addClass('pressed').click(function() {
        var product_id = $(this).data('product-id');
        $.ajax({
            url: '/cart/' + product_id + '/add/',
            type: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                if (data.status === 'ok') {}
            }
        });
    });

    $('button[name="increase"]').addClass('pressed').click(function() {
        var product_id = $(this).data('product-id');
        $.ajax({
            url: '/cart/' + product_id + '/increase/',
            type: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                if (data.status === 'ok') {
                    var quantityCell = $('tr[data-product-id="' + product_id + '"] td span.quantity');
                    quantityCell.text(data.new_quantity);

                    var sumCell = $('tr[data-product-id="' + product_id + '"] td.sum-cell');
                    sumCell.text(`${(data.new_quantity * data.product_price).toFixed(2)}$`);
                }
            }
        });
    });

    $('button[name="decrease"]').addClass('pressed').click(function() {
        var product_id = $(this).data('product-id');
        $.ajax({
            url: '/cart/' + product_id + '/decrease/',
            type: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                if (data.status === 'ok') {
                    var quantityCell = $('tr[data-product-id="' + product_id + '"] td span.quantity');
                    quantityCell.text(data.new_quantity);

                    var sumCell = $('tr[data-product-id="' + product_id + '"] td.sum-cell');
                    sumCell.text(`${(data.new_quantity * data.product_price).toFixed(2)}$`);
                }
            }
        });
    });

    $('button[name="remove"]').addClass('pressed').click(function() {
        var product_id = $(this).data('product-id');
        $.ajax({
            url: '/cart/' + product_id + '/remove/',
            type: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                if (data.status === 'ok') {
                    var row = $('tr[data-product-id="' + product_id + '"]');
                    row.remove();
                }
            }
        });
    });

    $('button[name="clear"]').addClass('pressed').click(function() {
        $.ajax({
            url: '/cart/clear',
            type: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                if (data.status === 'ok') {
                    $('tr[data-product-id]').remove();
                }
            }
        });
    });
});