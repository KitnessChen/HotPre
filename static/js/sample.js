$(document).ready(function(){
    $('a.sample-item').click(function(){
        var item_name = $(this).attr('id');

        // change style and disable click function
        $('h4.sample-title').text('Keyword: ' + item_name);
        $('h4.sample-title').css('color', '#000000');
        $('h4.sample-title').css('font-size', '32px');
        $('h4.sample-title').css('font-family', 'Georgia, Times, serif');
        $('a.samples').removeClass('dropdown-toggle');
        $('a.samples').removeAttr('href');
        $('div.select-sample').removeClass('dropdown');
        $('div.select-sample').css('background-color', '#f3f4f3');
        $('div.select-sample').css('border-radius', '4px');

        //post request
        var url = $(this).attr('href');
        $.ajax({
            url: url,
            type: 'post',
            dataType: 'json',
            data: {'keyword': item_name},
            success: function(data){
                $('div.data-view').attr('', '');
                $('div.data-chart').attr('', '');
                // add function!
            }
        });
    });
});