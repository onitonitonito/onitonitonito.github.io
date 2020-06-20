---
layout: default
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
  var eyeBall = function(selector) {
    var eye = document.querySelector(selector),
      pupil = eye.querySelector('.pupil'),
      rangeOfEye = eye.getBoundingClientRect();

    var getPupilRoll = function(mouseX, mouseY) {
      var radian = Math.atan2(mouseY - (rangeOfEye.y + rangeOfEye.height * 0.5), mouseX - (rangeOfEye.x + rangeOfEye.width * 0.5));
      pupil.style.transform = 'rotate(' + (180 * radian / Math.PI - 90) + 'deg)';
    };

    return {
      getPupilRoll: getPupilRoll
    };
  };

  var eyeLeft = eyeBall('.eyeball-left');
  var eyeRight = eyeBall('.eyeball-right');

  window.addEventListener('mousemove', function(e) {
    eyeLeft.getPupilRoll(e.pageX, e.pageY);
    eyeRight.getPupilRoll(e.pageX, e.pageY);
  });
</script>


<br><br><br><br><br>
<br><br><br><br><br>
<br><br><br><br><br>

# CSS Tag
{% highlight css linenos %}
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

{% endhighlight %}


# JavaScript Tag

{% highlight javascript linenos %}
    var eyeBall = function(selector) {
      var eye = document.querySelector(selector),
        pupil = eye.querySelector('.pupil'),
        rangeOfEye = eye.getBoundingClientRect();

      var getPupilRoll = function(mouseX, mouseY) {
        var radian = Math.atan2(
          mouseY - (rangeOfEye.y + rangeOfEye.height * 0.5),
          mouseX - (rangeOfEye.x + rangeOfEye.width * 0.5));
        pupil.style.transform = 'rotate(' + (180 * radian / Math.PI - 90) + 'deg)';
      };

      return {
        getPupilRoll: getPupilRoll
      };
    };

    var eyeLeft = eyeBall('.eyeball-left');
    var eyeRight = eyeBall('.eyeball-right');

    window.addEventListener('mousemove', function(e) {
      eyeLeft.getPupilRoll(e.pageX, e.pageY);
      eyeRight.getPupilRoll(e.pageX, e.pageY);
    });
{% endhighlight %}
