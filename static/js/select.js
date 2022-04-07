$(document).ready(function (){
   $("#month-e4cc").append(function (){
     var place = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
     for(let p = 0;p < place.length;p++){
        var option = document.createElement('option')
        option.textContent = place[p];
        option.value = place[p];
        $("#month-e4cc").append(option)
     }
   });
   $("#people-e4cc").append(function (){
     var place = ['三五好友','独自一人','家庭','情侣','亲子','闺蜜','学生']
     for(let p = 0;p < place.length;p++){
        var option = document.createElement('option')
        option.textContent = place[p];
        option.value = place[p];
        $("#people-e4cc").append(option)
     }
   });

});
