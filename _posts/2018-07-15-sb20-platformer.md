---
layout: post
title: 스크래치 REMIX로 Go!-Invert Platformer by United07 🎴
comments: true
category: [scratch, game]
tag: [Platformer, United07]
excerpt_separator: <!-- more -->
---
<img src="https://goo.gl/iHX8oE" align="right">
이것은 스크래치 리믹스 모음에 대한 간단한 요약글입니다. 플랫포머는 스크래치에서 유행하는 간단한 미로형의 게임포맷으로, 사각형이 마리오 처럼 중력의 영향을 받으며 좌,우,점프를 할 수 있는 미로형 게임포맷인데, 스크래치의 특성을 잘 살려서 간단하게 구현할 수 있어서 많은 사람들이 응용을 하고 있습니다.    
<!-- more -->

<br><br>
# 1.0 본문 제목 : Invert Platformer

본문은 여기부터 시작!@ - 스크래치 플랫포머의 개량 버젼, 미로찾아 나가기
기본적인 플랫포머 아이디어에, United07은 화면을 회전시켜서 미로를 찾아가는 아이디어를 첨부 시켰습니다. 독창적인 아이디어인지 아닌지는 잘 모르니, 일단 판단은 보류합니다. 😄 직접 보고 판단해 봅시다.

>[![스크래치모음]({{site.baseurl}}/images/post_img/20180730-01.png)](https://goo.gl/oFN1wJ)
> 현재의 페이지에서 그대로 열려고 하는 경우 <br>
> 해당 페이지로 가시려면 [[이곳?]](https://goo.gl/oFN1wJ) 을 참조해 주세요
>
> 별도의 페이지에서 새로 열려고 하는 경우 <br>
> 해당 페이지로 가시려면 <a href="https://goo.gl/oFN1wJ" target="_blank">[바로 이곳]</a>
을 참조해 주십시요_
> 본 페이지의 확장자는 md이며, Markdown과 HTML을 혼용하여 사용 하였음.



<br><br>
# 2.0 에디터 모드

플랫포머의 특성상 비교적 간단한 블럭조합으로 구현이 가능한 듯합니다. 블럭 조합이 간단하긴 합니다. 간단한 블럭조합임에도 불구하고, 미로구성을 정교하게 해 놓으면, 상당히 재미있는 게임성을 보여 줍니다. 여기서는 화면회전(**뒤집기**)✨라는 아이디어를 도입했구요. 상당히 신선하긴 합니다. (개인적으로는.. 😃)

>![에디터모드]({{site.baseurl}}/images/post_img/20180730-09.png)
> 에디터로 가려면 아래 페이지를 참조해 주세요 <br>
> 해당 페이지로 가시려면 <a href="https://goo.gl/KbFiUJ" target="_blank">[이곳]</a>
을_ 참조해 주세요



<br><br>
# 2.0 플레이 페이지

<img src="{{site.baseurl}}/images/post_img/20180730-02-intro.png" width="400" alt="인트로">

> * 이곳은 인트로 입니다.
> 1. 슬라이드바를 이용하여 플랫포머의 색깔을 선택 할 수 있습니다..
> 1. 컬러 선택을 마쳤으면 [**Play**] 버튼으로 시작합니다.
> 1. 플랫포머 미로찾기 버전의 Invert (Rotate) 버전입니다.


> <img src="{{site.baseurl}}/images/post_img/20180730-03.png" width="400" alt="레벨1">
> * 레벨1은 몸풀기 준비입니다.
> 1. Rotate 플랫포머가 어떻게 작동하는지 개념을 보여줍니다.
> 1. 방향키 좌/우 = 이동, 상향키= 점프입니다.
> 1. 스페이스 바를 누르면 화면 180도 회전이 일어납니다.
> 1. 화면 반전 (Invert)를 통해서 새로운 길을 만들어 냅니다.
> 1. 붉은색 용암에 빠지면, 다시 처음 시작한 장소로 돌아갑니다.


> <img src="{{site.baseurl}}/images/post_img/20180730-04.png" width="400" alt="레벨2">
> * 레벨2는 점프와 반전이 동시에 작동해야 해결 됩니다.
> 1. 이제 부터는 스스로 미로를 찾아 나아가야 합니다.
> 1. 중간 중간 힌트 메시지가 화면에 나옵니다.
> 1. 메시지에서 힌트를 얻어서 미로를 찾아 나갑니다.

> <img src="{{site.baseurl}}/images/post_img/20180730-05.png" width="400" alt="레벨3">
> * 레벨3는 고립과 반전입니다.
> 1. 더이상 진행이 불가능 할 경우, 'R'로 리셋할 수 있습니다.
> 1. R키를 누르면, 처음부터 다시 시작합니다.

> <img src="{{site.baseurl}}/images/post_img/20180730-06.png" width="400" alt="레벨4">
> * 레벨4는 반전을 일으켜야 되는 장소에 힌트가 있습니다..
> 1. 좀 더 복잡한 미로에 갖혔습니다.
> 1. 좀 더 세밀한 조종이 필요합니다.
> 1. 화면에 나타나는 힌트에 주목해 주십시요.

> <img src="{{site.baseurl}}/images/post_img/20180730-07.png" width="400" alt="레벨5">
> * 레벨5는 좀 더 다양한 미로가 적용됩니다.
> 1. 갖혔어도 갖힌 것이 아닙니다.
> 1. 반전을 적극적으로 이용해 주세요.
> 1. 의도 하지 않았던, 지름길을 찾을 수 도 있습니다.

> <img src="{{site.baseurl}}/images/post_img/20180730-08.png" width="400" alt="레벨6">
> * 레벨6는 글자로 이루어진 미로입니다.
> 1. 어느 위치에서 반전이 이루어져야 탈출할 수 있을까요?
> 1. 좀 더 세밀하게 전진해 주세요.



<br><br>
# 3.0 성벽방어전 (Castle Defence)
성벽 방어전이라는 게임도 만들었네요.. 기존의 탱크게임과 윈터댄스를 융합한 융합버전입니다. 재미는... 모르겠고 😅 구성은 재미있는 시도라고 생각합니다. 폭탄을 들고 대쉬하는 스틱맨, 저지하려는 대포, 성벽방어.. 아직은 초기화 버전이라, 좀 더 게임성을 높여야 할 것 같습니다. **United07** ✨

> <img src="{{site.baseurl}}/images/post_img/20180730-10.png" width="400" alt="성벽방어전">
> * **Two Tanks** 게임의 변형판, **성벽방어전** 도 준비 중입니다.
> 1. 폭탄을 들고 성으로 돌진하는 스틱맨을 막아주세요.
> 1. 오픈 클로즈 베타버젼, 릴리즈 준비중
> 1. 이 모든것은 'United07'이 제작합니다.
> 1. 저는 그냥 바라만 볼 뿐이죠..
> 1. 좀 더 창의력을 발휘해 주세요,



<br><br>
# 4.0 MD를 사용하면 Resize 불가능!

마크다운의 아쉬운 점, 특히 **Kramdown** / 본 페이지는 심각한 블로그용 페이지가 아닙니다. 그냥 **Git page** ✨의 지킬 프레임웍을 테스트 해보기 위해서 (나중에 쓸지도 모를) 만든 페이지 이므로 내용에 성의(?)가 없는 점은 이해 바랍니다. 일종의 아카이브? 나중에 진지하게 블로그 질을 구성해 보겠습니다. 💦

> 마크다운을 사용하면 이미지 리사이즈가 안된다는 단점이 있습니다.
> ![레벨5]({{site.baseurl}}/images/post_img/20180730-07.png)
> * 너무 크고 볼품없어 집니다..
> 1. 본 게시글은 테스트용 샘플입니다.
> 1. 자세한 내용은 본인들이 적어 줬으면 좋겠네요.
> 1. '**힌트**'는 이미 충분히 줬으니까요..
> 1. 마크다운에 금방 익숙해 질 것입니다.
> 1. 익숙 해지면 문서작성 속도가 빨라져요.. 그래서, 편해요~ 🐄