---
layout: post
title: (초안) 깃허브 협업 프로세스 구축하기 (연습)💑
comments: true
category: [github]
tag: [develop, co-work]
excerpt_separator: <!-- more -->
---
GitHub에서 협업하는 과정을 아톰 에디터에서 연습해 봅니다.. 항상 혼자 만드는 것이 익숙한 입장에서 처음에는 적응하는 과정이 필요하기 때문에, 그리고 제일 궁금했던 것은 과연 **'Merge'** 과정에서 업데이트 관리와 처음 접하는 사람을 힘들게 만드는 것, **Conflict** 가 발생 하는 과정을 확인해 보기 위함 입니다.
<!-- more -->

<br><br>
# 1.0 자주 쓰는 Branch (요약)

<img src="/images/post_img/20180806-002.png" width="550">

* **'develop'** : 개발중인 프로그램의 소스를 총 관리하는 브랜치
* **'feature'** : 프로그램의 기능 단위로 나누어 개발하는 브랜치
* **'release'** : 출시 직전의 소스를 관리하는 브랜치 (베타 버전)
* **'hotfix'** : 출시 이후, 발생한 버그를 긴급수정 Master에 바로 반영해야 하는 경우
* **'master'** : 상용화 되는(혹은 출시하는) 버전의 소스를 관리하는 브랜치

<br><br>
## 1.1 O.K! 연습하자!

<img src="/images/post_img/20180806-003.png" width="550">

> * 마스터에서 긴급수정이 발생해서, `'git checkout -b hotfix'` 로 분기 시킴
> * `'hotfix'` 브랜치에서 긴급 에러를 수정하고, **'Master'** 와 **'Develop'** 에서 각각 **'Merge'** 시킨다
> * 여기까지 **'git push'** 를 하면 아래와 같이 **'Network'** '챠트'가 완성된다.

| <img src="/images/post_img/20180806-001.png" width="550"> |
|:--:|
| **Fig.01** - 세 **브랜치*** 가 나란히 정렬! |


> * **'Master'** 와 **'Develop'** 에서 각각 **'Merge'** 를 했기 떄문에 3개의 브랜치가 나란히 자리를 잡았습니다.
