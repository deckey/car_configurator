$(function () {
    car = eval("(" + $('#carData').data('car') + ")");

    // STEP 2: Trim level
    $selectedTrim = $('.trimradio').find('input[value="' + car.trim.style + '"]');
    $selectedTrim.attr('checked', 'checked');
    $selectedTrim.parent().addClass('btn-default');
    $selectedTrim.parent().find('h4').addClass('tx-grey');

    $('.trimradio').click(function () {
        $('.trimradio').removeClass('btn-default');
        $('.trimradio').parent().find('h4').removeClass('tx-grey');
        $(this).addClass('btn-default');
        $(this).find('h4').addClass('tx-grey');
        trim = eval("(" + $(this).data('trim') + ")");

        // update car summary panel       
        $('#trimLevel').text(trim.style);
        $('#totalPrice').fadeOut(function () {
            $('#totalPrice').text("\u20AC" + calculatePrice(car.base_price, trim.price));
            $('#totalPrice').fadeIn();
        });


        // fill car data to hidden fields
        $('#carModel').val(car.model);
        $('#trimStyle').val(trim.style);
        $('#trimPrice').val(trim.price);
    })

    // STEP 3: Engine selection
    $selectedEngine = $('.engineradio').find('input[value="' + car.engine.name + '"]');
    $selectedEngine.attr('checked', 'checked');
    $selectedEngine.parent().addClass('btn-default');
    $selectedEngine.parent().find('h4').addClass('tx-grey');

    $('.engineradio').click(function () {
        $('.engineradio').removeClass('btn-default');
        $('.engineradio').parent().find('h4').removeClass('tx-grey');
        $(this).addClass('btn-default');
        $(this).find('h4').addClass('tx-grey');
        engine = eval("(" + $(this).data('engine') + ")");

        // update car summary panel       
        $('#summaryEngine').text(engine.name + ' ( '+ engine.power+' ) ');
        $('#summaryFuel').text(engine.fuel);
        $('#totalPrice').fadeOut(function () {
            $('#totalPrice').text("\u20AC" + calculatePrice(car.base_price+car.trim.price, engine.price));
            $('#totalPrice').fadeIn();
        });

        // fill data to hidden fields
        $('#engineName').val(engine.name);
        $('#engineFuel').val(engine.fuel);

    })

    $('#selectTransmission').on('change', function () {
        transmission = $(this).find(':selected').val();
        $('#engineTransmission').val(transmission);
        $('#summaryTransmission').text(transmission + ' / 6G');
    })

    function calculatePrice(price, trim) {
        return (price + trim).toLocaleString();
    }
});

