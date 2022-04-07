
// CHAT BOOT MESSENGER////////////////////////


$(document).ready(function(){
    var count = 0
    $(".chat_on").click(function(){
        $(".Layout").toggle();
        $(".chat_on").hide(300);
        // var startreply = setTimeout(remotedialogue,500)
        // remotedialogue()
        if (count == 0){
            var autoreply = setInterval(remotedialogue , 3000);
        }
        //取消自動回復
        $(".Input_button-send").click(function (){
            clearInterval(autoreply)
            count = 1
        });
        $(".Input_field").keydown(function (event){
           if (event.keyCode === 13) {
               clearInterval(autoreply)
               count = 1
           } ;
        });

    });

    $(".chat_close_icon").click(function(){
        $(".Layout").hide();
        $(".chat_on").show(300);
        count = 1
    });

    $(".Input_button-send").click(function (){

        userstr = $(".Input_field").val();
        dia = localdialogue(userstr)
        $(".Messages").append(dia)
        $(".Input_field").val("")
        $(".Messages").scrollTop($(".Messages")[0].scrollHeight);

    });
    $(".Input_field").keydown(function (event){
        if (event.keyCode === 13) {
            userstr = $(".Input_field").val();
            dia = localdialogue(userstr)
            $(".Messages").append(dia)
            $(".Input_field").val("")
            $(".Messages").scrollTop($(".Messages")[0].scrollHeight);
        };
    });

    function localdialogue(str){
        var Newlocal = document.createElement('div');
        Newlocal.className='user local';
        var Newavatar = document.createElement('div');
        Newavatar.className = 'avatar';
        var Newpic = document.createElement('div');
        Newpic.className = 'pic';
        var Newname = document.createElement('div');
        Newname.className = 'name';
        Newname.textContent="您"
        var Newtxt = document.createElement('div');
        Newtxt.className = 'txt';
        Newtxt.textContent = str
        var picimg = document.createElement('img')
        picimg.src ='static/images/eee.jpg'

        Newpic.append(picimg)
        Newavatar.append(Newpic)
        Newavatar.append(Newname)
        Newlocal.append(Newavatar)
        Newlocal.append(Newtxt)

        return Newlocal
    }

    function remotedialogue(){

        var automessage = ['安安~',
                            '有甚麼需要為您服務的?',
                            '很高興為您服務，您好~有甚麼需要為您服務的?',
                            '很高興為您服務，有什麼能幫忙您的?',
                            '很高興為您服務，有什麼可以為您效勞的?',
                            '您好~有什麼能幫忙您的?',
                            '安安~您好',
                            '很高興為您服務~您還在嗎?',
                            '您好~有什麼可以為您效勞的?',
                            '安安?在嗎?',
        ];
        var index = Math.floor(Math.random()*10)


        var Newlocal = document.createElement('div');
        Newlocal.className='user remote';
        var Newavatar = document.createElement('div');
        Newavatar.className = 'avatar';
        var Newpic = document.createElement('div');
        Newpic.className = 'pic';
        var Newname = document.createElement('div');
        Newname.className = 'name';
        Newname.textContent="客服"
        var Newtxt = document.createElement('div');
        Newtxt.className = 'txt';
        Newtxt.textContent = automessage[index]
        var picimg = document.createElement('img')
        picimg.src ='static/images/rr.jpg'

        Newpic.append(picimg)
        Newavatar.append(Newpic)
        Newavatar.append(Newname)
        Newlocal.append(Newavatar)
        Newlocal.append(Newtxt)
        $(".Messages").append(Newlocal)
        $(".Messages").scrollTop($(".Messages")[0].scrollHeight);
    }
});

