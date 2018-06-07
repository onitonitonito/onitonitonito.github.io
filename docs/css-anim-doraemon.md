---
layout: blank
comments: True
permalink: /css-doraemon/
---

<style>
  body { margin: 0; }

  .content {
    position: absolute;
    top: 335px;
    left: 0px;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 15px;
    color: #0083e8;
    line-height: 1.5;
    margin: 0 auto;
    max-width: 800px;
    padding: 2em 2em 4em;
  }

  .DORAEMON {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300px;
    height: 400px;
    background: url('/images/docs_img/doraemon_01.jpeg') no-repeat 50% 50%;
    background-size: contain;
    transform: translate(-50%, -50%);
  }

  .eyeballs {
    display: flex;
    position: absolute;
    top: 70px;
    left: 95px;
  }

  .eyeball {
    position: relative;
    width: 60px;
    height: 60px;
    border: 2px solid black;
    border-radius: 50%;
    background-color: white;
    transform: scaleX(0.9);
  }

  .eyeball-left {
    left: 3px;
  }

  .eyeball-right {
    left: -4px;
  }

  .pupil {
    position: absolute;
    left: 20px;
    bottom: 0;
    width: 20px;
    height: inherit;
  }

  .pupil:before {
    content: '';
    display: block;
    position: absolute;
    left: 0;
    bottom: 0;
    width: inherit;
    height: 20px;
    border-radius: 50%;
    background-color: black;
  }

  .pupil:after {
    content: '';
    display: block;
    position: absolute;
    left: 11px;
    bottom: 11px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: white;
  }

  .pre-small  {
    font-size: 0.8em;
    padding: 0px 0px 0px 50px;
    color: $gray;
    background-color: $lightGray;
  }

</style>

<div class="DORAEMON">

  <div class="eyeballs">
    <div class="eyeball eyeball-left">
      <div class="pupil"></div>
    </div>
    <div class="eyeball eyeball-right">
      <div class="pupil"></div>
    </div>
  </div>


  <div class='content'>
    <li><b>원본 소스보기</b> :
      <a href='http://www.studiomeal.com/code/doraemon/'>[Studio Meal]
      </a></li>
  </div>

</div>


<!-- 조각 삽입화일 : 페이징 넘버링 css-paging.html -->
{% include css-paging.html %}


<script>
  var 눈알 = function(selector) {
    var 눈 = document.querySelector(selector),
      눈동자 = 눈.querySelector('.pupil'),
      눈영역 = 눈.getBoundingClientRect();

    var 눈알굴리기 = function(mouseX, mouseY) {
      var 라디안 = Math.atan2(mouseY - (눈영역.y + 눈영역.height * 0.5), mouseX - (눈영역.x + 눈영역.width * 0.5));
      눈동자.style.transform = 'rotate(' + (180 * 라디안 / Math.PI - 90) + 'deg)';
    };

    return {
      눈알굴리기: 눈알굴리기
    };
  };

  var 왼눈 = 눈알('.eyeball-left');
  var 오른눈 = 눈알('.eyeball-right');

  window.addEventListener('mousemove', function(e) {
    왼눈.눈알굴리기(e.pageX, e.pageY);
    오른눈.눈알굴리기(e.pageX, e.pageY);
  });
</script>


<br><br><br><br><br>
<br><br><br><br><br>
<br><br><br><br><br>

# 스크립트 테그

<pre class="pre-small">
  〈script〉
    var 눈알 = function(selector) {
      var 눈 = document.querySelector(selector),
        눈동자 = 눈.querySelector('.pupil'),
        눈영역 = 눈.getBoundingClientRect();

      var 눈알굴리기 = function(mouseX, mouseY) {
        var 라디안 = Math.atan2(
          mouseY - (눈영역.y + 눈영역.height * 0.5),
          mouseX - (눈영역.x + 눈영역.width * 0.5));
        눈동자.style.transform = 'rotate(' + (180 * 라디안 / Math.PI - 90) + 'deg)';
      };

      return {
        눈알굴리기: 눈알굴리기
      };
    };

    var 왼눈 = 눈알('.eyeball-left');
    var 오른눈 = 눈알('.eyeball-right');

    window.addEventListener('mousemove', function(e) {
      왼눈.눈알굴리기(e.pageX, e.pageY);
      오른눈.눈알굴리기(e.pageX, e.pageY);
    });
  〈/script〉
</pre>
