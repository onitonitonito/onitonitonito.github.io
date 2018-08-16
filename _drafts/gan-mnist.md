---
layout: post
title: 위조범과 경찰관 - 머신러닝 GAN Model 구현하기
comments: true
category: [ML]
tag: [GAN, MNIST]
excerpt_separator: <!-- more -->
---
<img alt="잡았다요놈!" src="https://goo.gl/V8Zi79" width="170" align="left" style="padding: 0px 30px 0px 10px;">
GAN(Generative Adversarial Nets) 모델은 대립하는 두개의 신경망을 서로 경쟁시켜 결과물을 생성하는 방법을 학습하게 하는 모델입니다.

_"Adversarial"이란 단어의 사전적 의미를 보면 대립하는, 적대하는 란 뜻을 갖습니다. 대립하려면 어찌 되었든 상대가 있어야하니 GAN은 크게 두 부분으로 나누어져 있다는 것을 먼저 직관적으로 알 수 있습니다._
<!-- more -->

<br><br>
## By Tim O'Shea, O'Shea Research.

> Some of the generative work done in the past year or two using generative adversarial networks (GANs) has been pretty exciting and demonstrated some very impressive results.  The general idea is that you train two models, one (G) to generate some sort of output example given random noise as input, and one (A) to discern generated model examples from real examples.  Then, by training A to be an effective discriminator, we can stack G and A to form our GAN, freeze the weights in the adversarial part of the network, and train the generative network weights to push random noisy inputs towards the “real” example class output of the adversarial half.


| <img src="https://goo.gl/QFXkEq" width="550"> |
|:----------------------------------------------|
| **Fig.00** - GAN 모델을 구성하는 개념도 |
|[출처]: [MNIST Generative Adversarial Model in Keras](https://goo.gl/JL2KNs)|



<br><br>
# 1.0 점점 지능화 되가는 위조지폐범

GAN 모델을 제안한 이안 굿펠로우(Ian Goodfellow)가 논문에 제시한 비유에 의하면, 위조지폐범(생성자 신경망)과 경찰관(구분자 신경망)을 상호 대립시켜, 경찰은 감별하려고 노력하고, 위조지폐범은 위조방법을 고도화 하는 관계를 통해서 진짜와 구분하기 어려운 고도의 위조지폐를 만들수 있도록 학습 하게 하는 것 입니다.




<br><br>
# 2.0 MNIST 를 이용한 GAN모델 작성
* 처음에는 의미를 알 수 없는 노이즈를 발생 시키지만
* 학습의 단계를 거치면서, 점점 위조모방이 구체화 되어 가는 것을 볼 수 있다.

| <img src="/images/post_img/20180917-gan-001.png" width="550"> |
|:-----------------------------------------|
| **Fig.01** - 처음 제너레이터는 아무거나, 막던져보는 식.. 그냥, 노이즈 일 뿐! |




<br><br>

| <img src="/images/post_img/20180917-gan-010.png" width="550"> |
|:-----------------------------------------|
| **Fig.02** - 이터레이션이 반복될 수록 모방은 점점 정교해진다. |




<br><br>

| <img src="/images/post_img/20180917-gan-030.png" width="550"> |
|:-----------------------------------------|
| **Fig.02** - 상당히 정교해 졌다.. 이제 겨우 300번 반복 학습 |



<br><br>

| <img src="/images/post_img/20180917-gan-200.png" width="550"> |
|:-----------------------------------------|
| **Fig.03** - 이미 1,000회를 넘었을때 정교화 과정은 끝났다. |




<br><br>
# 3.0 원본 EXAMPLE 과 위조 결과물 비교
* 사실, 여기서 보여주는 손글씨는 __MNIST__ 에 없는 **전혀 새로운** 모방된 손글씨 데이터다.
* __세상에 없는 창조 된 데이터!__

| <img src="https://goo.gl/NKGeaJ" width="300">　 　| <img src="https://goo.gl/i7uChu" width="300"> |
|:----------------:|:----------------:|
|**01.원본 이미지** | **02.위조 이미지**|



<br><br>
# 2.0 전체 모방이 진행되는 과정
* 각, 이미지당 100회의 학습을 거쳐서 교정이 이루어 졌다
* 약 1,000회를 넘었을때 이미 정교화 과정은 끝난듯~ (품질이 비슷)


| <img src="/images/post_img/20180917-gan-000.png" width="550"> |
|:-----------------------------------------|
| **Fig.04** - 기계학습, 피드백을 받아 손글씨를 모방하는 과정 |



# 3.0 참고자료
1. [MNIST Generative Adversarial Model in Keras](https://goo.gl/JL2KNs)
1. [Jaejun Yoo's Playground](https://goo.gl/ZvSvtm): 초짜 대학원생이 이해하는 Generative Adversarial Nets
1. [골빈해커의 3분 딥러닝](https://goo.gl/rZF2Rx) - 텐서플로우 맛 .... ( 한빛미디어 / 김진중 )
