---
layout: post
title: Ultra Fine Dust Level Prediction for Daily life 🐼
comments: true
category: [data]
tag: [stastics, prediction, fine-dust]
excerpt_separator: <!-- more -->
---

<img width="150" align="left" src="/images/post_img/20190217-00.png" style="padding: 0px 15px 0px 0px;">

'<span id="head">The</span>' harsh winter cold begins to fade, and when spring comes, ultrafine dust slowly begins to increase with the monsoon blowing from China. Ultrafine dust has now become our daily seasonal phenomenon with yellow dust in the spring. So, we need to batten the hatch more than the past.
<!-- more -->

<style>
  #head {
    font-size : 1.8em ;
    font-weight : bold;
  }
</style>




<br><br>

<!-- HOW THE AIR IN SONGDO? -->
<img width='650' src="/images/post_img/20190217-01.png">

'<span id="head">How</span>' is the weather in your city right now? okay, let us ask it another way. how is the air around you? If it is a sunny sky and a fresh breeze, you would be a one of a few happy people out of people around the world. the more industrialized the place we live in, the more unhealthy air we have to inhale around us. especially the toxins that are produced from the exhaust gas from the combustion which is made from a factory or vehicle.  

Here Songdo Int’l City in Incheon as a western harbor city near Seoul in Korea is face to the east coastline which is the most industrialized area of China. a ton of ultra-fine dust is carried by the monsoon which is direct from north to south in winter vise versa in summer. moreover, when in winter, the steep consumption of fuel for heating individual houses lead to produce much combustion gases.

<!-- RELATION BETWEEN PRESSURE AND ULTRA FINE DUNST -->
<!-- <img width='500' style="margin-left: 40px;" src="/images/post_img/20190217-02.png"> -->



<!-- EVOLUTION OF MASKS -->
<img width='800' src="/images/post_img/20190217-03.png">

'<span id="head">The</span>' ultra-fine dust is unfortunately our daily life. we have to put on a mask almost every day when winter-spring comes because ultra-fine dust is a toxin moreover it carries a lot of industrial chemicals. thus putting on a mask is a necessity in winter-spring.

the monsoon changes its direction by season. as the below chart shows, the concentration of ultra-fine dust has obvious seasonal repetition trend that shows a strong force in winter-spring, weak in summer-autumn due to the competition of the high atmospheric pressure of continent and the low pressure of the pacific ocean.

# seasonal repeatation

<div>'ultra fine dust concentration in five years'</div>

<!-- REPEATATION IN FIVE YEARS -->
<img width='800' src="/images/post_img/20190217-041.png">

미세먼지 발생량과 밀접한 상관 관계가 있는 4가지 화학적 결합물, SO2, NO2, O3, CO를 포함해서 우리가 최종적으로 변화량을 알고자 하는 2가지 발생물, PM2.5 와 PM10, 대하여 상관관계를 살펴보면 각 성분간의 상관 관계가 매우 명백하게 나타나는 관계를 가지고 있는것을 확인할 수 있습니다.

특히 눈에 도드라지는 점은 O3 는 모든 인자에 대하여 확고하고 뚜렷한 반비례 관계를 보이는 것을 알수 있습니다. O3을 제외한 다른 인자들은 그 정도의 차이는 있지만 일반적으로 강하거나 약한 비례관계에 있는것이 눈에 띄입니다. 이런 상관관계가 왜 공기품질을 측정하는데 4+2의 화학적 결합물을 대상으로 했는지를 이해할 수 있는 부분입니다.


<!-- RELATION 6 FACTORS -->
<img width='600' src="/images/post_img/20190217-04.png">


그런데, 무엇인지 알수 없는 불안정한 요소, 예를 들자면 급격하게 미세먼지 발생량 변화의 징후가 감지되기 시작 할 때, 이제까지 안정적이던 6가지 인자의 상관관계 균형이 서서히 깨지기 시작 할 거라는 것을 가설로 세울수 있다고 생각합니다.

어디까지나 가설로서 제안하는 것이지만, 안정적이었던 균형은 변화의 징후가 보이기 시작할때 급격하게 인자들의 상관관계가 변화하는 것을 감지 할 수 있습니다.

우리는 이것으로 부터 어떤 트랜트가 발생하기 전에 징후를 감지할수 있다고 보고 있습니다. 즉, 각 성분의 상관관계를 나타내는 이 챠트가 안정적인 상태에서 변화가 시작되고 종료되는 시점을 예측하는 인자로 활용할 수 있을 것으로 판단하는 것입니다.


<!-- CORELATION BAR CODE SYSTEM -->
<img width='500' src="/images/post_img/20190217-043.png">


만약 그렇게 할 수 있다면, 1시간 마다 제공되는 6가지 인자의 데이터 값을 기반으로 1개의 의미가 압축된 바코드와 같은 시각적인 도구를 만들어 낼 수 있고, 1시간 단위로 생성되는 이 바코드를 나열 하는 것으로 미세먼지 발생량 변화량을 사전에 감지 할 수 있는 바로미터가 될 수 있다고 기대하고 있습니다.

제가 상상하는 서비스는 이것을 기반으로 편의를 제공 하고자 합니다.

이와 더불어, 이제까지 발생 변화량을 시간이력으로서 그래프에 축적하고, 현재 시점에서 부터 앞으로 발생하지 않는 시간 영역대, 예를 들어 12시간 또는 24시간 등, 를 시계열 예측 으로 일기예보하듯이 제공할 수 있다면 사용자가 일상생활을 계획하는데 도움이 이 되는 매우 유툥한 서비스가 될 것입니다.


<!-- WANNABE SERVICE LIKE THIS -->
<img width='700' src="/images/post_img/20190217-10.png">


다시 간결하게 정리를 하자면 2가지 입니다.

>  1. 첫 째는 복잡한 변화를 한눈에 감지할 수있는 시각적 코드 시스템
>  1. 두번 째는 과거의 축적 된 이력 데이터를 보여 줄 것
>  1. 세번 째는 앞으로 발생할 경향을 예측하여 예보를 해 줄 것


* 시각적 QR코드 시스템은 안정적인 상태가 얼마나 지속되고 있는지, 변화의 조짐이 시작되는지의 정보를 시각적으로 간편하게 제공한다.
 예: 맑은 공기가 안정적인 상태가 3일째 지속되고 있었는데, 갑작스럽게 나빠지기 시작했다

* 과거의 축적된 이력데이터 챠트는 그것과 연관지어 사용자 마다 연관된 스토리를 만들어 낼 수 있다. (소셜미디어, 블로그 등)
 예: 어제는 올해 들어 가장 깨끗한 날씨였다

* 미세먼지 예보시스템은 아웃도어 활동 스케쥴을 작성하는데 도움을 줄 수 있다.
 예: 내일 오후에 테니스 모임을 계획하고 싶은데, 미세먼지 상태가 나아질까?


아래 보여주는 챠트는 실제로, 올해 1월 1일 부터 500 시간(약 21일)동안 송도지역의 미세먼지 변동량을 한시간 단위로 저장한 데이터 이며, 상단 예측 그래프는 가장 간단한 ARIMA Model 을 사용하여 예측 샘플을 작성 하였습니다. 물론, 단순히 ARIMA MODEL 만으로 간단히 해결 되는 문제는 아닙니다.






<!-- CONCENTRATION IN DISASTER DEGREE -->
<!-- <img width='500' src="/images/post_img/20190217-042.png"> -->




<!-- PREDICTION 24HOURS-1 -->
<!-- <img width='400' src="/images/post_img/20190217-05-1.png"> -->


<!-- PREDICTION 24HOURS-2 -->
<img width='400' src="/images/post_img/20190217-05-2.png">

<!-- PREDICTION 24HOURS-3 -->
<!-- <img width='400' src="/images/post_img/20190217-05-3.png"> -->





<!-- PM2.5 & PM10 -1 -->
<!-- <img width='700' src="/images/post_img/20190217-09-1.png"> -->

<!-- PM2.5 & PM10 -2 -->
<!-- <img width='700' src="/images/post_img/20190217-09-2.png"> -->
