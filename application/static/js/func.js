function stripscript(s) {
    var pattern = new RegExp("[`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）&mdash;—|{}【】‘；：”“'。，、？\"]")
        var rs = "";
    for (var i = 0; i < s.length; i++) {
        rs = rs + s.substr(i, 1).replace(pattern, '');
    }
    return rs;
}

function loadMore(to_load_page) {
    $.ajax({
        type: "GET",
        url: "/api/topic/"+to_load_page,
        dataType: "json",
        success: function(data) {
            var topic_list = data['topics'];
            //console.log(topic_list);
            $.each(topic_list, function(idx, topic) {
                var sub = 
                    '<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">\
                        <div class="box flip-box">\
                            <a href="/t/'+topic['ref']+'" target="_blank">\
                                <img alt="'+stripscript(topic['title'])+'" class="img-responsive" src="http://nmhvoiafhqwpfhwqfiq.qiniudn.com/'+topic['thumb']+'.jpg'+'?imageView2/1/w/360/h/360/interlace/1" />\
                            </a>\
                            <div class="meta">\
                                <a href="/t/'+topic['ref']+'" target="_blank">'+topic['title']+'</a>\
                            </div>\
                        </div>\
                    </div>';
                $('#to_load').append(sub);
            });
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
              console.log(textStatus);
              console.log(errorThrown);
        }
    });
}

function loadDetail(topic_id){
	$.ajax({
	    type: "GET",
	    url: "/api/detail/"+topic_id,
	    dataType: "json",
	    success: function(data) {
	        var pic_list = data['pics'];
            var page_title = data['title'];
            page_title = page_title.toString();
            $('.ds-thread').attr('data-title',page_title);
	        //console.log(pic_list);
	        $.each(pic_list, function(idx, pic) {
	            var sub = 
					'<div class="box show-box">\
				      <img src="http://nmhvoiafhqwpfhwqfiq.qiniudn.com/'+pic['link']+'.jpg">\
				      <div class="box-btns">\
				        <button type="button" class="btn btn-primary"><span class="glyphicon glyphicon-heart"></span> 喜欢 × 0</button>\
				        <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-send"></span> 推荐</button>\
				      </div>\
				    </div>';
                $('#to_load').append(sub);
	        });
	    },
	    error: function (XMLHttpRequest, textStatus, errorThrown) {
	          console.log(textStatus);
	          console.log(errorThrown);
	    }
	});
}