---
layout: blank
comments: True
---

<style>
  @keyframes no-look {
      100% { background-position: -960px 0; }
  }

  .no-look {
    position: absolute;
    top: 285px;
    left: 45%;
    width: 96px;
    height: 96px;
    margin-bottom: 5px;
    background: url('{{ site.baseurl }}/images/docs_img/mc_nolook_sample.png') no-repeat 0 0;
    background-size: 960px 96px;
    animation: no-look 1000ms infinite steps(10);
  }

  .big  {
    font-size: 1.5em;
  }

  .pre-small  {
    font-size: 0.7em;
    padding: 0px 0px 0px 50px;
  }
</style>

<!-- 네비게이션 바 : MD는 HTML테그 바깥에 위치해야 함 -->
  [[BACK]](/docs/css)
  [[1]](/docs/css_anim_doraemon)
  [[2]](/docs/css_anim_mcmoosung)


<div class="big" align="center">
  <b>MC Moosung - No-look Pass 🎭</b>
</div>

<div class="no-look"></div>

<!--소스이미지 글자를 아래로 밀어 냄-->
<div class="post" align="center">
  <br><br><br><br><br><br><br>
  <a href='{{ site.baseurl }}/static/imgs/mc_nolook_sample.png'>Source Image?</a>
</div>

<br><br><br>

<h1 class="big">The Performance of MC.Moosung</h1>
<ul class="read-more">
  <li>Moosung performed no-look pass</li>
  <li>at the Incheon Int'l Airport immigration office</li>
  <li>passing his luggage bag to secretary mindlessly.</li>
  <li>Here's [<u><a href="https://www.youtube.com/watch?v=fDY3PmApP1o"target="_blank"> Moosung </u></a>] in various parody version, @Youtube.</li>
</ul>

<br>
<h1 class="big">The References🍞 :</h1>

<ul>
  <li>css code & image source</li>
</ul>

<pre class="pre-small">
  @keyframes no-look {
    100% { background-position: -640px 0; }
    }

  .no-look {
    width: 64px;
    height: 64px;
    background: url('http://studiomeal.com/images/mc_nolook_sample.png') no-repeat 0 0;
    background-size: 640px 64px;
    animation: no-look 750ms infinite steps(10);
    }

  잠깐 1분만 코딩 꿀팁 공부!
  "CSS로 프레임 단위 애니메이션 만들기"
  샘플보기 http://www.studiomeal.com/code/1min/15
  #공유하면공유형아처럼멋져져요 #1분코딩

  @keyframes 아니요.
  100 % {배경 위치 :-640 픽셀 0
  }

  아니요.
  너비: 64 픽셀;
  높이: 64 픽셀;
  배경: URL (' http://studiomeal.com/images/mc_nolook_sample.png') No. 0 0 0;
  백그라우드 크기: 640 픽셀 64 픽셀;
  애니메이션: No-750 MS 무한한 단계 (10)
  }
</pre>
