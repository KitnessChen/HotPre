$(document).ready(function(){
    var url = 'search/' + $('h4.keyword-title').text();
    var cur_time = $('h4.keyword-title').attr('data-time');
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        data: {'cur_time': cur_time},
        success: function(res){
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