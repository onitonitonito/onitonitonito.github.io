---
layout: default
permalink: /test/
excerpt_separator: <!-- more -->
---
<h1>JEKYLL-TEST🎃</h1>

<!-- more -->
# 1.0 site variable - Global
> 1. site.time = {{site.time}}
> 1. site.static_files = {.{site.static_files}}
<!-- 스테틱화일 데이터 / 주소값 반환 -->


```ruby
site.static_files => [
    #<Jekyll::StaticFile:0x00000000082d58b8>,
    #<Jekyll::StaticFile:0x00000000082d43a0>,
    #<Jekyll::StaticFile:0x00000000082cff58>,
    #<Jekyll::StaticFile:0x0000000006f09208>,
    #<Jekyll::StaticFile:0x00000000082d5b60>,
    #<Jekyll::StaticFile:0x00000000082d54a8>,
    #<Jekyll::StaticFile:0x0000000006e866a0>,
    #<Jekyll::StaticFile:0x0000000006da10c8>,
    #<Jekyll::StaticFile:0x0000000006da0e48>,
    ...,
  ]
```


<br><br>
<!-- 사이트 콜렉션으로 가져오는 값 = 폴더별 저장된 화일 -->
# 2.0 site.collections = {.{site.collections}}

```ruby
site.collections => {
  [
    #<Jekyll::Document _albums/fkj.md collection=albums>,
    #<Jekyll::Document _albums/josquin.md collection=albums>,
  ],

  [
    #<Jekyll::Document _posts/2018-05-22-hello-world.md collection=posts>,
    #<Jekyll::Document _posts/2018-06-07-Ruby-jekyll-serve.md collection=posts>,
    #<Jekyll::Document _posts/2018-07-06-jupyter-wdcloud.md collection=posts>,
    #<Jekyll::Document _posts/2018-08-04-sb20-platformer.md collection=posts>,

    #<Jekyll::Document _drafts/heated-data-center-MS.md collection=posts>,
    #<Jekyll::Document _drafts/the-first-day-of-year.md collection=posts>,
  ]
}
```



<br><br>
# 3.0 config.yml 화일에 정의된 값을 가져온다.
> 1. site.favicon1 = {{site.favicon1}}
> 1. site.favicon2 = {{site.favicon2}}
> 1. site.favicon3 = {{site.favicon3}}



<br><br>
# 4.0 태그, 카테고리 문서 HTML 전체를 가져온다.
> 1. site.categories.python = {.{site.categories.python}}
> 1. site.tags.game = {.{site.tags.game}}


<br><br>
# 5.0 페이지 레이아웃으로 정의된 문서 HTML 전체를 가져온다
> 1. site.pages = {.{site.pages}}
> 1. site.html_pages = {.{site.html_pages}}

<br><br>
# 6.0 데이터 태그..

> 1. site.data = {.{site.data}}

```ruby
{
  “members”=>
    [
      {“name”=>”Nassir Malik”, “github”=>”nassir-malik”, “repo”=>”IOT-Pi3-Alexa-Automation”},
      {“name”=>”R Studio Github”, “github”=>”rstudio”, “repo”=>”RStartHere”},
      {“name”=>”United07”, “github”=>”FunXD”, “repo”=>”Arduino_on_Github”},
      {“name”=>”Mintpepper Park”, “github”=>”unins”, “repo”=>”K-Mooc”},
      {“name”=>”2nd Kay Park”, “github”=>”onito”, “repo”=>”hello_python”}
    ],

  “orgs”=>
    {
      “jekyll”=>
        {
          “username”=>”jekyll”, “name”=>”Jekyll”, “members”=>
            [
              {“name”=>”Tom Preston-Werner”, “github”=>”mojombo”},
              {“name”=>”John Doe”, “github”=>”jdoe”},
              {“name”=>”Parker Moore”, “github”=>”parkr”},
              {“name”=>”Mintpepper Park”, “github”=>”unins”},
              {“name”=>”United07”, “github”=>”FunXD”},
              {“name”=>”2nd Kay Park”, “github”=>”onito”}
            ]
        },

      “rstudio”=>
        {
          “username”=>”rstudio”, “name”=>”R-Studio”, “members”=>
          [
            {“name”=>”2nd Kay Park”, “github”=>”onito”},
            {“name”=>”John Doe”, “github”=>”jdoe”}
          ]
        }
    }
}
```


<br><br>
# 7.0 그밖의 태그들..
> 1. site.html_files = {{site.html_files}} # nothing
> 1. site.documets = {{site.documets}}     # nothing


<br><br>
# 8.0 라즈베리파이 GPIO 수위센서 코딩
> 1. 비접속 수위센서 코딩
> 1.RPi.GPIO modul - Digital INPUT.
> 1. DFRobot Non-contact Liquid Level Sensor XKC-Y25-T12V SKU: SEN0204
> 1. port 20,16,12 : Arduino Water level sensor

|<img src="https://goo.gl/DaAWpp" width="300">　|<img src="https://goo.gl/qSr1E6" width="250">|
|:-------:|:-------:|
| **fig.01** - on pipes | **fig.02** - on valves |

<br><br><br>
```python
#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
'''  RPi.GPIO modul - Digital INPUT.
 DFRobot Non-contact Liquid Level Sensor XKC-Y25-T12V SKU: SEN0204
 # 20,16,12 : Arduino Water level sensor
'''

SENS = []
SENS.extend((14, 15, 18))       # Arduino Sensors
SENS.extend((23, 24))           # Blank
SENS.extend((25, 8, 7, 1))      # XKC-Y25-T12V SKU: SEN0204

PORTS = len(SENS)

def setup():
    # BroadCom Chip Pin# Set
    GPIO.setmode(GPIO.BCM)
    for n in range(PORTS):
        GPIO.setup(SENS[n], GPIO.IN)

def loop():
    COUNT = 1
    while True:
        print('-------------- count: %s' % COUNT)

        for n in range(PORTS):
            num_bcm = str()
            read_bcm = GPIO.input(SENS[n])

            if SENS[n] >= 10:
                num_bcm = str(SENS[n])
            else:
                num_bcm = '0' + str(SENS[n])
            print('GPIO# %s = %s' % (num_bcm, read_bcm))

        print()
        time.sleep(1)
        COUNT += 1


def main():
    setup()

    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
```
<!--
-->
