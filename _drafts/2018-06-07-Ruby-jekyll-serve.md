---
layout: post
title: Ruby지킬 가상서버(Jekyll serve)실행하기💎
comments : true
category: [ruby, jekyll]
tag: [ruby, jekyll, serve]
excerpt_separator: <!-- more -->
---
<img alt="클라우드" width="110" align="left" style="padding: 0px 10px 0px 10px;" src="/images/post_img/20180607-0ruby.png" >

Gitpage는 정적 웹프레임워크 인 **RUBY기반** 의 지킬(jkyll)을 지원 합니다. 처음 부터 루비를 좀 배워서 기초부터 셋업을 잡는 것도 좋은 방법이겠지만, 지킬(jekyll)을 쓰려고 루비를 깊이 알 필요은 없을것 같고, 기본셋업이 되있는 Github의 Jekyll-now를 🍴(포크) 해 와서 사용합니다. **Ruby** 는 최소한의 명령어만 익혀서, Git push 전에 실시간으로 수정사항을 점검하기 위해서 가상서버를 실행합니다.💂
<!-- more -->

<br><br>
## 1.0 루비 설치하기 (윈도우즈 64bit with devkit) 💎

윈도우즈 [[**루비 인스톨러**]](https://rubyinstaller.org/downloads/) 사이트에서 ruby 2.5.1 x64 with devkit 을 다운로드하여 설치 한다.     

>
| <img src="{{ site.baseurl }}/images\post_img\20180607_000.png" width="600"> |
|:----------------------------------------------|
| [**fig.01** 루비] |



<br><br>
## 2.0 셋업은 잘 모르겠으면 [NEXT]

디폴트 셋팅, [NEXT]를 누르면 기본은 합니다. 기본적으로 devkit을 포함하는 인스톨을 합니다.

>
| <img src="{{ site.baseurl }}/images\post_img\20180607_001.png" width="600"> |
|:----------------------------------------------|
| **fig.02** 인스톨 창 |

>
| <img src="{{ site.baseurl }}/images\post_img\20180607_002.png" width="600"> |
|:----------------------------------------------|
| **fig.03** 이런 식으로 종료하게 됩니다. |


>
| <img src="{{ site.baseurl }}/images\post_img\20180607_003.png" width="600"> |
|:----------------------------------------------|
| **fig.02** 3번 MinGW 개발키트 를 설치 합니다. |

>
| <img src="{{ site.baseurl }}/images\post_img\20180607_004.png" width="600"> |
|:----------------------------------------------|
| **fig.04** 인스톨이 완료되면, GEM 이라고 실행 했을때 화면 |


<br><br>
## 3.0 나머지는 Jekyll-now 의 README를..

지킬-나우를 포크해 오는 방법은 [[**이곳**]]({{ site.baseurl}}/jekyll-now/) 을 참고 하셔서 순서대로 끌어다 쓰시면 되겠습니다. 가상 서버를 실행시킬 때는,

1. gem install jekyll
1. gem install bundler

두 개를 설치하신 후에, bundle 를 실행시키면, 의존성 화일들을 자동으로 전부 설치해 줍니다.
의존성 화일 설치가 다 끝나면, Bash 창에..

**jekyll serve**

를 실행 시키시면, 제대로 설치가 끝났다면, localhost:4000 / 127.0.0.1:4000 으로 접속하라는 메시지를 보실 수 있습니다. ...그렇게 접속 하시면 됩니다..

**HAVE FUN with JEKYLL!**


<br><br>
## 4.0 근데, 그렇게 안되셨을 거예요..

왜냐면 Jekyll-now와 번들러로 설치한 최신 패키지와 버젼이 맞지 않아서 중복된다는 메시지를 보셨을 겁니다.

그냥,

gem uninstall ...

로 중복 충돌되는 버젼을 다 삭제하시면 됩니다.  


그리고, Bash 창에..

**jekyll serve**

를 실행 시키시면, 제대로 설치가 끝났다면, localhost:4000 / 127.0.0.1:4000 으로 접속하라는 메시지를 보실 수 있습니다. ...그렇게 접속 하시면 됩니다..

**HAVE FUN with JEKYLL!**

<br><br>
## 4.0 근데, 그렇게 안되셨을 거예요..

왜냐면, 중복 충돌 나는게 한두개가 아닐겁니다.
충돌나는게, 기억나는데로 보면, public_suffix, kramdown, rouge, jekyll.. 등등

에러메시지 안뜰때 까지 계속 삭제하시면 됩니다.

그리고, Bash 창에..

**jekyll serve**

를 실행 시키시면, 제대로 설치가 끝났다면, localhost:4000 / 127.0.0.1:4000 으로 접속하라는 메시지를 보실 수 있습니다. ...그렇게 접속 하시면 됩니다..

**HAVE FUN with JEKYLL!**

<br><br><br>
<img src="{{site.baseurl}}/images/system/ruby_on_rails.jpg" width=""/>

<br><br><br><br><br>.
