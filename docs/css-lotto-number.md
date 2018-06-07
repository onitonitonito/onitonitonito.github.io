---
layout: blank
comments: True
permalink: /css-lotto/
---
<style>

#NUMBERS {
  margin-top: 5vh;
  font-size: 3em;
  color: #fff;
  text-align: center;
}

b  {
  display: inline-block;
  width: 80px;
  height: 80px;
  line-height: 80px;
  border-radius: 64px;
  margin: 1px;
  background: #ff8700;
}

</style>



<!-- 조각 삽입화일 : 페이징 넘버링 css-paging.html -->
{% include css-paging.html %}



# 1.0 Lotto 번호 생성기 (6개)
<img src="/images/post_img/20180806-000.png" width="300" align="right" style="padding: 0px 0px 0px 40px;">

> * 본 CSS샘플은 **Git Codlab** 스터디의 일환으로 작성 된 연습화일을 참조하였습니다.
> * 실제 Git 연습은 **GitPage** 로 진행을 했고, 본 CSS 샘플을 업데이트 하는 과정도 Git 스터디 진행과정과 동일하게 테스트 했습니다.
> * 원본소스의 깃허브 화일을 Base 로 수정 하였습니다.


<!-- 넘버생성 위치 -->
<br><br><br><br>
<div id="NUMBERS"></div>

<br>
<div class="content">
  <li style="text-align: center;">원본 소스보기 :
    <a href='https://github.com/owo-sbsoft/lotto' target="new">
      [owo-sbsoft : git codelab]
    </a>
  </li>
</div>  



<br><br>
# 2.0 CSS & JAVA SCRIPT

```css
#NUMBERS {
  margin-top: 5vh;
  font-size: 3em;
  color: #fff;
  text-align: center;
}

b  {
  display: inline-block;
  width: 80px;
  height: 80px;
  line-height: 80px;
  border-radius: 64px;
  margin: 1px;
  background: #ff8700;
}
```



<!-- Todo: CSS 스크립트 뒤에 표시 안되는 문제 해결 -->
<br><br>
# 3.0 자바스크립트

```java
function genNumbers(){
    var lottoNumbers = [];
    while (lottoNumbers.length<6) {
        var no = Math.round(Math.random()*45)+1;
        if( lottoNumbers.indexOf(no) === -1 ) lottoNumbers.push(no);
    }
    return lottoNumbers;
}

function checkLogic1(numbers) {
    for(var i=0; i<numbers.length; i++){
        var no = numbers[i];
        if( numbers.indexOf(no+1)>=0 && numbers.indexOf(no+2)>=0 ) return true;
    }
    return false;
}

function checkLogic2(numbers) {
    var decArea = [0, 0, 0, 0, 0];
    for(var i=0; i<numbers.length; i++){
        var area = Math.floor( numbers[i]/10 );
        decArea[area]++;
    }
    return ( decArea[0]>2 || decArea[1]>2 || decArea[2]>2 || decArea[3]>2 || decArea[4]>2 );
}

window.onload = function()  {
    var lottoNumbers = genNumbers();
    // TODO 23,24,25 과 간이 연속으로 3개의 숫자가 나오지 않게 하자!
    while( checkLogic1(lottoNumbers) ) lottoNumbers=genNumbers();

    // TODO 11,15,17 과 같이 같은 10의 자리수에 3개가 나오지 않게 하자!
    while( checkLogic2(lottoNumbers) ) lottoNumbers=genNumbers();

    var html_lotto = "";
    for(var i=0; i<lottoNumbers.length; i++){
      html_lotto += '<b>'+ lottoNumbers[i] +'</b> ';
    }
    document.getElementById("NUMBERS").innerHTML = html_lotto;
}
```







<script>
function genNumbers(){
    var lottoNumbers = [];
    while (lottoNumbers.length<6) {
        var no = Math.round(Math.random()*45)+1;
        if( lottoNumbers.indexOf(no) === -1 ) lottoNumbers.push(no);
    }
    return lottoNumbers;
}

function checkLogic1(numbers) {
    for(var i=0; i<numbers.length; i++){
        var no = numbers[i];
        if( numbers.indexOf(no+1)>=0 && numbers.indexOf(no+2)>=0 ) return true;
    }
    return false;
}

function checkLogic2(numbers) {
    var decArea = [0, 0, 0, 0, 0];
    for(var i=0; i<numbers.length; i++){
        var area = Math.floor( numbers[i]/10 );
        decArea[area]++;
    }
    return ( decArea[0]>2 || decArea[1]>2 || decArea[2]>2 || decArea[3]>2 || decArea[4]>2 );
}

window.onload = function(){
    var lottoNumbers = genNumbers();
    // TODO 23,24,25 과 간이 연속으로 3개의 숫자가 나오지 않게 하자!
    while( checkLogic1(lottoNumbers) ) lottoNumbers=genNumbers();

    // TODO 11,15,17 과 같이 같은 10의 자리수에 3개가 나오지 않게 하자!
    while( checkLogic2(lottoNumbers) ) lottoNumbers=genNumbers();

    var html_lotto = "";
    for(var i=0; i<lottoNumbers.length; i++){
      html_lotto += '<b>'+ lottoNumbers[i] +'</b> ';
    }
    document.getElementById("NUMBERS").innerHTML = html_lotto;
}
</script>
