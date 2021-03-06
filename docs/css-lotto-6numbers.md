---
layout: default
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
}

.btn-custom {
  margin: 0;
  background-color: #f5b86f;
  cursor: pointer;
  font-family: $helveticaNeue;
  font-weight: 600;
  font-size: 28px;
  letter-spacing: 0px;
}

</style>



<!-- 조각 삽입화일 : 페이징 넘버링 css-paging.html -->
{% include css-paging.html %}



# 1.0 Lotto 번호 생성기 (6개)
<img src="/images/post_img/20180806-000.png" width="250" align="right" style="padding: 0px 0px 0px 40px;">

> * 본 CSS샘플은 **Git Codlab** 스터디의 연습 화일을 Base로 수정 하였습니다.
> * **Git codeLab** 연습은 본 **GitPage** 로 진행을 했고, 본 CSS 샘플을 업데이트 하는 과정도 Git 스터디 협업과정을 따라 했습니다.


<br>
<!-- 넘버생성 위치 -->
<div id="NUMBERS"></div>


<br>
<!-- 리로드 버튼 생성 위치 -->
<div align="center">
  <a href="./index.html">
    <button class="btn-custom" name="RELOAD">RELOAD</button>
  </a>
</div>


<br>
<!-- 원본소스 인용위치 -->
<div class="content">
  <li style="text-align: center;">원본 소스보기 :
    <a href='https://github.com/owo-sbsoft/lotto' target="new">
      [owo-sbsoft : git codelab]
    </a>
  </li>
</div>  



<br><br>
# 2.0 CSS & JAVA SCRIPT
> * 볼드태크의 배경색을 자바스크립트에서 랜덤셀렉트로 변경
> * 로또볼의 색깔이 랜덤으로 변하도록 코드 변경

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
}


.btn-custom {
  margin: 0;
  background-color: #f5b86f;
  cursor: pointer;
  font-family: $helveticaNeue;
  font-weight: 600;
  font-size: 28px;
  letter-spacing: 0px;
}

```



<!-- Todo: CSS 스크립트 뒤에 표시 안되는 문제 해결 -->
<br><br>
# 3.0 자바스크립트

* 원본의 기능을 개선해 보자 .. 디자인 개선
* 단색 보다는, 진짜 로또공 같은 <strike>생생한</strike> 컬러를 입혀보자

| <img src="/images/post_img/20180806-006.png" width="650"> |
|:-----------------------------------------:|
| **Fig.** - 뭘 좋아 할 지 몰라서 48개를 준비했어! |

> * 한 땀, 한 땀 수작업으로 Color pick 을 해서 무지개색 파렛트를 준비
> * 컬러감각이 처음 치고는 나쁘지 않은 듯 (~*뿌듯*~)
> * 48개의 파렛트에서 랜덤으로 컬러를 뽑아 쓰기로 했다
> * 루프안에서 48개의 색상을 무작위로 선택해 주자



<!-- 깃 지스트 자바스트립트 코드 인용 -->
<table width='250' align='center' cellpadding='15' border='0'>
  <tr>
    <td>

    <!-- 깃 지스트 (Git Gist) 코드보기 :: 자바 스크립트 -->
    <script src="https://gist.github.com/onitonitonito/691eb751b86957029904a2d551d6f47f.js">
    </script>

    </td>
  </tr>
</table>







<script>

  var lottoColors = [
    '#21fe09', '#ff8700', '#0967f4', '#ff0014', '#ffc200', '#f906eb',
    '#35d125', '#db8a2f', '#3e85f0', '#f04452', '#face42', '#f563ec',
    '#439939', '#b9864d', '#71a5f5', '#f47680', '#f5d87c', '#f1a5ed',
    '#426b3e', '#7c6346', '#9dbff2', '#f59ea5', '#faebba', '#f2bdef',
    '#486545', '#604e3a', '#c0d6f6', '#f9c3c7', '#b1a378', '#a781a5',
    '#749571', '#9e876d', '#8ca2c2', '#c89195', '#8b7c4e', '#834d80',
    '#abcda7', '#d2ba9f', '#c0d6f6', '#74383d', '#6c5b27', '#582055',
    '#bbf1b6', '#e8d2b8', '#2c3b52', '#401619', '#52410f', '#4d0749',
    ];

  function getNumbers() {
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

  window.onload = function() {
      var lottoNumbers = getNumbers();

      // TODO 23,24,25 과 간이 연속으로 3개의 숫자가 나오지 않게 하자!
      while( checkLogic1(lottoNumbers) ) lottoNumbers=getNumbers();

      // TODO 11,15,17 과 같이 같은 10의 자리수에 3개가 나오지 않게 하자!
      while( checkLogic2(lottoNumbers) ) lottoNumbers=getNumbers();

      var html_lotto = "";

      for(var i=0; i<lottoNumbers.length; i++)  {
        colorPick = Math.round(Math.random()*47);
        html_lotto += '<b style="background: '+ lottoColors[colorPick] +'">'+ lottoNumbers[i] +'</b> ';
      }
      document.getElementById("NUMBERS").innerHTML = html_lotto;
  }

</script>
