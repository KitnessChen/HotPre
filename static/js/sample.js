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
            url: '/predict',
            type: 'post',
            dataType: 'json',
            data: {'keyword': keyword},
            success: function(prediction, hot_mark){
                $('div.predition-chart').css('display', 'block');
                $('button#predict').css('font-family', 'Times New Roman, serif');
                $('button#predict').attr('disabled', 'disabled');
                $('button#predict').text(hot_mark + ' keyword');
                new Chartkick.LineChart("data-chart", prediction);
            },
            error: function(msg){
                $('div.predition-chart').css('display', 'block');
                $('button#predict').css('font-family', 'Times New Roman, serif');
                $('button#predict').attr('disabled', 'disabled');
                $('button#predict').text('HOT keyword');
                data = [
                {"name":"test 1", "data": {"2013-02-10 00:00:00 -0800": 3, "2013-02-13 00:00:00 -0800": 2, "2013-02-17 00:00:00 -0800": 4}},
                {"name":"test 2", "data": {"2013-02-10 00:00:00 -0800": 5, "2013-02-13 00:00:00 -0800": 9, "2013-02-17 00:00:00 -0800": 3}},
                {"name":"test 3", "data": {"2013-02-10 00:00:00 -0800": 6, "2013-02-13 00:00:00 -0800": 3, "2013-02-17 00:00:00 -0800": 9}},
                {"name":"test 4", "data": {"2013-02-10 00:00:00 -0800": 2, "2013-02-13 00:00:00 -0800": 1, "2013-02-17 00:00:00 -0800": 3}}
                ];
                new Chartkick.LineChart("data-chart", data);
            }
        });
    });
});