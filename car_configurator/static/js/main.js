$(function(){
    car = eval("("+$('#carData').data('car')+")");

    // STEP 2: Trim level
    $selectedTrim = $('.trimradio').find('input[value="'+car.trim.style+'"]');
    $selectedTrim.attr('checked', 'checked');
    $selectedTrim.parent().addClass('btn-default');
    $selectedTrim.parent().find('h4').addClass('tx-grey');
    
    $('.trimradio').click(function(){
        $('.trimradio').removeClass('btn-default');
        $('.trimradio').parent().find('h4').removeClass('tx-grey');
        $(this).addClass('btn-default');
        $(this).find('h4').addClass('tx-grey');
        equipment = eval("("+$(this).data('equipment')+")"); 

        $('#trimLevel').text(equipment.style);
        $('#totalPrice').text("\u20AC"+calculatePrice(car.base_price, equipment.price));
        
        // fill car data to hidden fields
        $('#carStyle').val(equipment.style);
        $('#trimPrice').val(equipment.price);
        
    })

    function calculatePrice(price, equipment){
        return (price + equipment).toLocaleString();
    }
});

