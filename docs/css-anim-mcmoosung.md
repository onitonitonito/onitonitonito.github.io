---
layout: default
comments: True
permalink: /css-moosung/
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
    font-size: 0.8em;
    padding: 0px 0px 0px 50px;
    color: $gray;
    background-color: $lightGray;
  }
</style>


<!-- 조각 삽입화일 : 페이징 넘버링 css-paging.html -->
{% include css-paging.html %}




<div class="big" align="center">
  <b>MC Moosung - No-look Pass 🎭</b>
</div>

<div class="no-look"></div>

<!--소스 이미지 글자를 아래로 밀어 냄-->
<div class="post" align="center">
  <br><br><br><br><br><br><br>
  <a href='{{ site.baseurl }}/static/imgs/mc_nolook_sample.png'>Source Image?</a>
</div>

<br><br><br>

# The Performance of MC.Moosung
> 1. Moosung performed no-look pass
> * at the airport immigration office
> * passing his luggage bag to secretary mindlessly.
> * Here's [[Moosung]](https://www.youtube.com/watch?v=fDY3PmApP1o) in various parody version, @Youtube.

<br>
# The References🍞 :
> * css code & image source

{% highlight css linenos %}
/* MC MOOSUNG NO-LOOK PASS * /
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
    font-size: 0.8em;
    padding: 0px 0px 0px 50px;
    color: $gray;
    background-color: $lightGray;
  }

  /* before changing parameters
  * width: 64 px;  height: 64 px;
  * background: URL(' http://studiomeal.com/images/mc_nolook_sample.png')
  * no repeat 0 0;
  * size of background image: 640 x 64px;
  * animation: no-look 750ms infinite step(10); * /  
{% endhighlight css linenos %}
