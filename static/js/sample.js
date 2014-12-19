$(document).ready(function(){
    $('a.sample-item').click(function(){
        var item_name = $(this).attr('id');

        // change style and disable click function
        $('h4.sample-title').text(item_name);
        $('h4.sample-title').css('color', '#000000');
        $('h4.sample-title').css('font-size', '35px');
        $('a.samples').removeClass('dropdown-toggle');
        $('a.samples').removeAttr('href');
        $('div.select-sample').removeClass('dropdown');
        $('div.select-sample').css('border-radius', '4px');
        $('div.select-sample').css('border-style', 'dashed');
        $('div.select-sample').css('border-color', '#C1EAEA');

        //post request
        var url = '/samples/' + item_name;
        $.ajax({
            url: url,
            type: 'get',
            dataType: 'json',
            data: {},
            success: function(res){
                $('div.data-view').css('display', 'block');
                $('div.data-chart').css('display', 'block');
                $('button#predict').css('display', 'block');
                for(var feature in res['msg']){
                    if(feature != 'chart'){
                        cur_content = $('h4#'+ feature).text();
                        $('h4#'+ feature).text(cur_content + ': ' + res['msg'][feature]);
                    }
                }
                new Chartkick.LineChart("data-chart", res['msg']['chart']);
            },
            error: function(res){
                console.log(res['error']);
            }
        });
    });

    //predict
    $('button#predict').click(function(){
        var keyword = $('h4.sample-title').text();
        $('button#predict').text('Please wait....');
        $.ajax({
            url: '/predict/sample',
            type: 'get',
            dataType: 'json',
            data: {'keyword': keyword},
            success: function(res){
                console.info('success');
                $('div.predition-chart').css('display', 'block');
                $('button#predict').css('font-family', 'Times New Roman, serif');
                $('button#predict').attr('disabled', 'disabled');
                $('button#predict').text(res['msg']['hot_mark'] + ' keyword');
                new Chartkick.LineChart("data-chart", res['msg']['data']);
            },
            error: function(res){
                console.log(res['error']);
            }
        });
    });
});