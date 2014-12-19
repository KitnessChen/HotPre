$(document).ready(function(){
    var url = 'search/' + $('h4.keyword-title').text();
    var cur_time = $('h4.keyword-title').attr('data-time');
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        data: {'cur_time': cur_time},
        success: function(res){
            $('div.data-view').css('display', 'block');
            $('div.data-chart').css('display', 'block');
            $('button#predict').css('display', 'block');
            //console.info('success');
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

    //predict
    $('button#predict').click(function(){
        var keyword = $('h4.keyword-title').text();
        var cur_time = $('h4.keyword-title').attr('data-time');
        $('button#predict').text('Please wait....');
        $.ajax({
            url: '/predict',
            type: 'post',
            dataType: 'json',
            data: {'keyword': keyword, 'cur_time':cur_time},
            success: function(msg){
                console.info('success');
                $('div.predition-chart').css('display', 'block');
                $('button#predict').css('font-family', 'Times New Roman, serif');
                $('button#predict').attr('disabled', 'disabled');
                $('button#predict').text(hot_mark + ' keyword');
                new Chartkick.LineChart("data-chart", res['msg']);
            },
            error: function(res){
                console.log(res['error']);
            }
        });
    });
});