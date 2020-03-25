$(function () {
    var $username = $("#username_input"); //等号右边参数是为了找到html中的id
    $username.change(function () {//username改变  事件
        var username = $username.val().trim();//拿到$username的值，trim去掉空格
        //如果有长度，就准备发送给服务器预校验
        if (username.length) {
            $.getJSON('/retailer/checkuser', {'username': username}, function (data) {
                // 等上边的callback返回回调函数了，再执行这个代码块里边的代码
                var $username_info = $("#username_info");
                if (data['status'] === 200) {
                    $username_info.html("用户名可用").css("color", 'green');
                } else if (data['status'] === 901) {
                    $username_info.html("用户名存在").css("color", 'red');
                }
            })
        }
    })
})