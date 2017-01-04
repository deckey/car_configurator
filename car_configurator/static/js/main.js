$(function () {

car = eval('(' + $('#carData').data('car') + ')');

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

    $selectedTransmission = $('#engineTransmission').val();
    $('#selectTransmission option[value=' + $selectedTransmission + ']').prop('selected', true);

    $('.engineradio').click(function () {
        $('.engineradio').removeClass('btn-default');
        $('.engineradio').parent().find('h4').removeClass('tx-grey');
        $(this).addClass('btn-default');
        $(this).find('h4').addClass('tx-grey');
        engine = eval("(" + $(this).data('engine') + ")");

        // update car summary panel       
        $('#summaryEngine').text(engine.name + ' ( ' + engine.power + ' ) ');
        $('#summaryFuel').text(engine.fuel);
        $('#totalPrice').fadeOut(function () {
            $('#totalPrice').text("\u20AC" + calculatePrice(car.base_price + car.trim.price, engine.price));
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

    // STEP 4: Features selection
    $selectedWheel = $('.wheelradio').find('input[value="' + car.wheel.name + '"]');
    $selectedWheel.attr('checked', 'checked');
    $selectedWheel.parent().addClass('btn-default');
    $selectedWheel.parent().find('h4, h5').addClass('tx-grey');

    // Exterior colors:
    const extColors = ["f7f6f6", "003748", "840705", "58330a", "c0c0c0", "444444", "000000"]
    // Interior colors:
    const intColors = ["f7f6f6", "c0c0c0", "444444", "ffe3ae", "000000"]

    ext_color = car.features.ext_color;
    int_color = car.features.int_color;

    selected_ext_color = $('#exteriorColors').find('input[value="'+ ext_color + '"]');
    selected_ext_color.parent().addClass('selected')
    selected_int_color = $('#interiorColors').find('input[value="'+ int_color + '"]');
    selected_int_color.parent().addClass('selected')

    $('#exteriorColors').find('.colorradio').click(function(){
        $('#exteriorColors').find('.colorradio').removeClass('selected');
        $(this).addClass('selected');
        var color = $(this).find('input[type="radio"]').val();
        $('#exteriorColor').val(color);
        $('#summaryFeaturesExterior').text(color);
    })
    $('#interiorColors').find('.colorradio').click(function(){
        $('#interiorColors').find('.colorradio').removeClass('selected');
        $(this).addClass('selected');
        var color = $(this).find('input[type="radio"]').val();
        $('#interiorColor').val(color);
        $('#summaryFeaturesInterior').text(
            $('#interiorColor').val() + ' ' + $('#interiorMaterial').val().toLowerCase());
    })
    $('#materialType').change(function(){
        var color = $(this).val();
        $('#interiorMaterial').val(color);
        $('#summaryFeaturesInterior').text(
        $('#interiorColor').val() + ' ' + $('#interiorMaterial').val().toLowerCase());
    })

    $('#materialType').val(car.features.material);
    $('.wheelradio').click(function () {
        $('.wheelradio').removeClass('btn-default');
        $('.wheelradio').parent().find('h4, h5').removeClass('tx-grey');
        $(this).addClass('btn-default');
        $(this).find('h4, h5').addClass('tx-grey');
        wheel = eval("(" + $(this).data('wheel') + ")");

        // update car summary panel       
        $('#summaryWheelName').text(wheel.size + '" ' + wheel.material);
        $('#totalPrice').fadeOut(function () {
            $('#totalPrice').text("\u20AC" + calculatePrice(car.base_price + car.trim.price + car.engine.price, wheel.price));
            $('#totalPrice').fadeIn();
        });

        // fill data to hidden fields
        $('#wheelName').val(wheel.name);
        $('#wheelMaterial').val(wheel.material);

        car.wheel.name = wheel.name;
        car.wheel.material = wheel.material;
    })

    // EXTRAS:
    all_extras = $('.extras-thumbnail').find('input[type="checkbox"]');
    all_prices = $('.extras-thumbnail').find('input[type="number"]');

    // Mark already selected items as selected:
    car_extras_list = [];
    if($('#carExtras').val()){
        car_extras_list = $('#carExtras').val().split(','); 
    }
    $.each(car_extras_list, function(idx, car_extra){
        $field = $('.extras-thumbnail').find("input[value='" + car_extra + "']");
        $field.prop('checked', true);
        $field.parent().addClass('btn-default');
        $field.parent().find('h4').addClass('tx-grey');
    })

    var selected_extras = [];
    var selected_prices = [];
    var extras_price = 0;
    
    selected_extras = $('.extras-thumbnail').find('input:checked');
    // $.each(selected_extras, function(idx, object){
    //     $('#carExtrasPrice').val(object.val());
    // })

    // car extras panel
    $extrasBtn = $('.extras-thumbnail').find('input[type="checkbox"]');
    $extrasBtn.click(function(){
        // get all extras from the inputs
        selected_extras = $('.extras-thumbnail').find('input:checked');
        var content = '';
        var extras_list = [];
        var prices_list = [];
        $field = $(this).parent();
        $field.toggleClass('btn-default');
        $field.find('h4').toggleClass('tx-grey');
        $.each(selected_extras, function(idx, option){
            content += '<h5>' + $(this).val() + '</h5>';
            extras_list[idx] = $(this).val();
            prices_list[idx] = $(this).data('price');
            if(selected_extras.length==0){
                extras_list = [];
                prices_list = [];
            }
        });
        $('#extraEquipment').html(content);
        $('#carExtras').val(extras_list);
        $('#carExtrasPrice').val(prices_list);
        extras_total_price = eval(prices_list.join("+"));
        $('#carExtrasTotalPrice').val(extras_total_price);

        $('#totalPrice').fadeOut(function () {
            if(extras_total_price){
                $('#totalPrice').text("\u20AC" + calculatePrice(car.base_price + car.trim.price + car.engine.price + car.wheel.price, extras_total_price));
            }else{
                $('#totalPrice').text("\u20AC" + calculatePrice(car.base_price + car.trim.price + car.engine.price , car.wheel.price));
            }
            $('#totalPrice').fadeIn();
        });
    })

    function calculatePrice(price, trim) {
        return (price + trim).toLocaleString();
    }
});

