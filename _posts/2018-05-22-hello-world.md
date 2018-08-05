---
layout: post
title: 첫번째 포스팅 테스트 입니다🌿
comment: false
category: [greeting, hello_world]
tag: [hello, world]
excerpt_separator: <!-- more -->
---
기성용, 휴가 마치고 뉴캐슬로 이번주 내 복귀..손흥민과 맞대결 가능성↑ 포스팅 작성테스트.. 김병학 기자 입력 2018.07.22. 19:36 수정 2018.07.22. 19:52 댓글 4개

[인터풋볼] 김병학 기자= 뉴캐슬로 새 둥지를 튼 기성용(29)이 이번주 내로 훈련에 복귀한다. 자연스럽게 개막전 출전 가능성도 높아지고 있다. 영국 매체 '크로니클 라이브'는 22일(이하 한국시간) "기성용이 휴가를 마친 후 곧 뉴캐슬로 복귀할 예정이다. 현재 월드컵 휴가를 받아 한국에서 개인적으로 훈련을 진행 중이다. 토트넘 홋스퍼와의 개막전에 맞춰 팀과 함께 몸을 만들 것"이라고 보도했다.

자세한 기사는 [[이곳]](https://goo.gl/EbQK5y)을 눌러주세요
<!-- more -->

# 링크를 작성하는 방법


## 1. 링크를 작성하는 방법 `... []()`
> `[링크표시]()`     
> `예시: [[Click Here to Google]](http://www.google.com)`     
> 예시: [[Click Here to Google]](http://www.google.com)     


## 2. 이미지를 링크하는 방법 `... ![]()`
> `![그림로딩 에러시 안내문](이미지 링크)`     
> `예시: ![_그림이 로딩되지 않았을 경우는 이렇게 나타남.._](https://goo.gl/zyQCGJ)`          
> ![_그림이 로딩되지 않았을 경우는 이렇게 나타남.._](https://goo.gl/zyQCGJ)     
> ![_그림이 로딩되지 않았을 경우는 이렇게 나타남.._](https://goo.gl/zyQCGJㅎ)   


## 3. 마크다운은 이미지 리사이징이 불가능 `... <img src="" width="">`
> <img src="https://goo.gl/zyQCGJ" width="150">    
> HTML 테그를 혼용해서 사용 ... `<img src="링크주소" width="픽셀">`    
> 링크는 인용부호 "" 를 감싸는 것을 잊지 말 것

## 4. 표형식으로 작성 하기 `... |:--:|:-----:|`
> 정렬없음 : '--'    
> 좌측정렬 : ':--'    
> 중앙정렬 : ':--:'    

|　　layout　　|post         |remarks|
|:-----------:|:-----------|:--|
| title    | 첫번째 테스트🌿||
| 번호      |  **1**        ||
| 좌측정렬  | \':--\' **2**   ||
| 우측정렬  | \'--:\'         ||
| 중앙정렬  | \':--:\'        ||
| 정렬없음  | \'--\'          ||

<br><br>
# 5.파이썬 코드삽입 태그

```python
import random
import time
import os

GROUND_WIDTH = 50
FILLER = '.'
ORNAMENTS_LIST = ('*' * 3).join('o$@#&')

while True:
    # Blinking Xmas Tree
    for n in range(1, 40, 2):
        if n <= 3:
            string = '*' * n
        else:
            inner = ""
            for x in range(n - 2):
                inner += random.choice(ORNAMENTS_LIST)
            string = '*' + inner + '*'
        print(string.center(GROUND_WIDTH, FILLER))

    # Tree trunk & Stand
    print('W'.center(GROUND_WIDTH, FILLER))
    print('W'.center(GROUND_WIDTH, FILLER))
    print('W'.center(GROUND_WIDTH, FILLER))
    print(('#' * 19).center(GROUND_WIDTH, FILLER))

    # wait 0.3 sec & clear screen
    time.sleep(0.3)
    os.system('cls')
```
