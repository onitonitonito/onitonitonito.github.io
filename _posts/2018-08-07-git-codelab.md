---
layout: post
title: To Practice Co-operative working process w/ GitHub (Part-1)💑
comments: true
category: [git,]
tag: [github, commit, co-work]
excerpt_separator: <!-- more -->
---
<img src="/images/post_img/20180806-0.png" width="140" align="left" style="padding: 0px 10px 0px 0px;">

<span id="start-ch">Let's</span> practice the process of collaborative on GitHub in the Atom editor. Since I'v been develop the code always by myself and am familiar with making it alone, it is necessary to practice the process first. and the most curious thing for beginner would be update management in the'Merge' process. Especially when the collision, Conflict, occurring.
<!-- more -->

<br>
<img style="padding: 20px 0px 0px 30px;" align="right" width="300" src="/images/post_img/20180806-000.png">
* __Fig.01__ - This is a practice course based on the Git Study training materials shared by individuals.

> * This is a practice course based on the Git Study training materials shared by an individual.
> * View original source :
[<a href="https://github.com/owo-sbsoft/lotto" target="new">owo-sbsoft : git codelab</a>]



<br><br>

| <img src="/images/post_img/20180806-0000.png" width="550"> |
|:-----------------------------------------:|
| __Fig.02__ - pair programming is beautiful! 😲 |

* Beautiful instructions and collaboration presented as examples. [[View Commit]](https://github.com/owo-sbsoft/lotto/commits/master)
* <strike>When will I be able to do such a beautiful collaboration?.. </strike>

<br><br>
# 1.0 Frequently used branches (in brief)

<img src="/images/post_img/20180806-002.png" width="550">

<!-- * __'develop'__ : 개발중인 프로그램의 소스를 총 관리하는 브랜치 -->
<!-- * __'feature'__ : 프로그램의 기능 단위로 나누어 개발하는 브랜치 -->
<!-- * __'release'__ : 출시 직전의 소스를 관리하는 브랜치 (베타 버전) -->
<!-- * __'hotfix'__ : 출시 이후, 발생한 버그를 긴급수정 Master에 바로 반영해야 하는 경우 -->
<!-- * __'master'__ : 상용화 되는(혹은 출시하는) 버전의 소스를 관리하는 브랜치 -->

* __'develop'__: A branch that manages the source of the program being developed.
* __'feature'__: A branch that break the features into functional units for develop.
* __'release'__: A branch that manages the source just before release (beta version)
* __'hotfix'__: When bugs that have occurred after release need to be fixed in the Emergency and is immediately updated to Master branch.
* __'master'__: A branch that manages the commercially available (or released) version of the code.


<br><br>
## 1.1 O.K! Let's Practive!

<!-- * 원본의 기능을 개선해 보자 .. 디자인 개선 -->
<!-- * 단색 보다는, 진짜 로또공 같은 <strike>생생한</strike> 컬러를 입혀보자 -->
* Improve the features from the origianl .. improvement on Design.
* instead of boring sole color, let's give it multiple vivid colors on the balls like real one!

| <img src="/images/post_img/20180806-006.png" width="550"> |
|:-----------------------------------------:|
| __Fig.03__ - I prepared 48 colors for you because I don't know what would you like! |

<!-- * 한 땀, 한 땀 수작업으로 Color pick 을 해서 무지개색 파렛트를 준비 -->
<!-- * 컬러감각이 처음 치고는 나쁘지 않은 듯 (~*뿌듯*~) -->
<!-- * 48개의 파렛트에서 랜덤으로 컬러를 뽑아 쓰기로 했다 -->
<!-- * 루프안에서 48개의 색상을 무작위로 선택해 주자 -->

> * Prepare a rainbow-colored pallet by color picking by hand with one stitch and one stitch
> * The sense of color seemed to be not bad for the first time (~*proud*~)
> * Each colors are selected randomly from 48-color pallets
> * Each colors are Randomly piecked from 48-colors in the loop

{% highlight JavaScript linenos %}
/* random color picking \*/
  let strings
  let html_lotto = "";

  for(var i=0; i<lottoNumbers.length; i++) {
    colorPick = Math.round(Math.random() * 48);
    strings = `<b style="background: {lottoColors[colorPick]}">` + \
              `{lottoNumbers[i]}</b>`;  
    html_lotto += strings
  }

  document.getElementById("NUMBERS").innerHTML = html_lotto;
{% endhighlight %}

- Add code that randomly selects a color from the list



<img src="/images/post_img/20180806-003.png" width="550">

- I worked hard to commit code and published it from __'develop'__ to __'release'__ and finally to __'master'__ branch, but ...
 to the branch,
- I found a small mistake on my code that the size of numbers are marked as 47 but have to be corrected to 48, because it is counted from 0.

<!-- > * 마스터에서 긴급수정이 발생해서, `'git checkout -b hotfix'` 로 분기 시킴
> * `'hotfix'` 브랜치에서 긴급 에러를 수정하고, __'Master'__ 와 __'Develop'__ 에서 각각 __'Merge'__ 시킨다
> * 여기까지 __'git push'__ 를 하면 아래와 같이 __'Network'__ '챠트'가 완성된다.
<<<<<<< HEAD
> * __'Master'__ 와 __'Develop'__ 에서 각각 __'Merge'__ 를 했기 떄문에 3개의 브랜치(마스터, 디벨롭, 핫픽스)가 나란히 같은 위치에 자리를 잡았습니다. -->

> * An emergency fix occurred in the __'Master'__ branch, so I branched to __'git checkout -b hotfix'__.
> * Fix the error urgently in the'hotfix' branch, and __'Merge'__ in __'Master'__ and __'Develop'__ respectively.
> * If you do __‘git push’__ so far, the __‘Network chart’__ is completed.
> * Since we __‘Merge’__ in __‘Master’__ and __‘Develop’__ respectively, the three branches (__‘Master’__, __‘Develop’__, and __‘Hotfix’__) are located in the same position side by side.

| <img src="/images/post_img/20180806-001.png" width="550"> |
|:-----------------------------------------:|
| __Fig.04__ - The three __branches__ are all neatly gathered in a row! |


<!--
> * 새로운 포스트(draft)를 추가 하기 위해서 __'Develop'__ commit 을 1단계 진행 하고, push 합니다.
> * 그러면, __'Master'__ 와 __'HotFix'__ 를 뒤로하고, __'Develop'__ 브랜치가 한단계 앞으로 치고 나가게 됩니다. -->

> * In order to add a new post (draft), proceed with the ‘Develop’ commit one step further, and push.
> * Then, ‘Master’ and ‘HotFix’ are left behind, and the ‘Develop’ branch goes one step further.



| <img src="/images/post_img/20180806-004.png" width="550"> |
|:---------------------------------------------------------:|
| __Fig.05__ - 이제 __'Develop'__* brench is proceeding a step ahead~!! |



<br><br>
# PART.02 ... To be continued ...

- something confused in the network chart,
- I guess something might be wrong in 'HotFix' branch.
- So, I tried to correct this problem using forced __'Stash' & 'Clear'__ then...

| <img src="/images/post_img/20180806-005.png" width="550"> |
|:---------------------------------------------------------:|
| __Fig.06__ - Something turn to be confused more seriously??!! did I correct? |

<!-- - 해보니, 종종 __'git push'__ 뒤에 __'--all'__ 을 잊는다
- '핫픽스(HotFix)' 후 '배포(release)'와 '개발(develop)'에 보내는 것도 종종 잊는다.
- 이것도 손에 익으려면, 얼마간의 적응기간이 필요 할 듯... <strike> 어차피 온자 하지만.. </strike> -->

* As it turns out, I often forget ‘–all’ option after ‘git push’
* I often forget to send it to ‘release’ and ‘develop’ after ‘HotFix’.
* In order to learn this, it seems that it will take some time to adapt to this system. altough I'm not seemed to be having a chance to co-working anyway, but...

[<a target="new" href="{{base_url}}/css-lotto/">View whole code of 6-ball picking</a>]

~~ __That's a quick wrap!__~~
