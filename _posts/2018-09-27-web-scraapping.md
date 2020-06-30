---
layout: post
title: Web-scrapping the air-quality data with Beautifulsoup😸
comments: true
category: [web-scrapping]
tag: [beautifulsoup, fine-dust,]
excerpt_separator: <!-- more -->
---
<img width="140" style="padding: 0px 10px 0px 0px;" src="/images/post_img/20180927-00.png" align="left">

'<span id="start-ch">Beautiful</span> Soup', A famous Python library for Web-scrapping, originally came from the conversation in 'Alice in Wornderland'. A Programmer seems to have a fandom to 'Alice'. a many name, title, and metaphore come from the book.

<!-- more -->

<br><br>
# Alice in Wonderland

<img width="250" align="left" style="padding: 40px 20px 0px 0px;"
src="/images/post_img/20180927-01.png" />

```
The Mock Turtle sighed deeply, and began,
in a voice sometimes choked with sobs,
to sing this:--
  Beautiful Soup, so rich and green,
  Waiting in a hot tureen!
  Who for such dainties would not stoop?

  Soup of the evening, beautiful Soup!
  Soup of the evening, beautiful Soup!
  Beau--ootiful Soo--oop!
  Beau--ootiful Soo--oop!

  Soo--oop of the e--e--evening,
  Beautiful, beautiful Soup!
```
* Alice in Wonderland : [Beautifulsoup song](https://bit.ly/30Qfmwz) by Mock turtle

<br><br>
# 1.0 National Open-API for Environment data

<span id="start-ch">The</span> Institute of Health and Environment of The Incheon Metropolitan City offers a Air quality sensor data in real time upto 2 days. Incheon Province also run 9 measure points out of hundreds of national measurement points. If you have interest on certain points, you can check those out through the web-site in handy way.

>
| <img src="/images/post_img/20180927-04songdo.png" width="600"> |
|:----------------------------------------------|
| [[Institute of Health and Environment]](https://goo.gl/AuTGRf) the measurement of chemicals |

<span id="start-ch">Here's</span> some examples who they offers the reslt of the measurement for environmental chemical components, which are consist of SO2, NO2, O3, CO, PM2.5 PM1O. As you well aware of, the main targets of interests are PM2.5, PM10 which means the degree of ultra fine dust particles classifying with the diameter in micro meter unit. for example PM2.5 means 2.5 micro meters, and PM10 is 10 micro meters

>
| <img src="/images/post_img/20180927-03scripts.png" width="600"> |
|:----------------------------------------------|
| **Fig.01** - Save the scraped data value in DF format |

<span id="start-ch">To</span> scrapping the values in the web can be proceeded by BS4, a representative python library for web-scrapping, and turns it into a text file(CSV).  and pandas(python) can change it to a preferable data format,'pandas-DataFrame', to analysis. Once you change it to the DataFrame format, you are ready to analyze the data in easy, visual, look into it variety way.


<br><br>
# 2.0 The Data Graph for PM2.5, PM10

>
| <img src="/images/post_img/20180927-01pms.png" width="400"> |
|:----------------------------------------------|
| **Fig.02** - time-series graph of PM2.5 and 10 for 2 dyas |

<span id="start-ch">Overall</span>, if you check the changes in the concentration of fine dust during the two days, you can easily find out that it tends to gradually be improved, and interesting things are the high-peaks are to be shown in a specific time span. (yes, Unfortunately, due to my mistake of making a chart, the left and right sides are reversed, the time goes from right to left in the chart, so I'm telling you that the fine dust concentration is getting improved.)

<span id="start-ch">The</span> fine dust concentration starts to rise from 3:00 am, before the rush-hour, and when it reaches at 9 am, it forms the highest peak. After all, fine dust is considered to be related to the traffic volume. Because SO2 and NO2 come out from exhaust gas of vehicle or other combustions else are known to produce fine dust. Since the relationship between fine dust and the two chemicals is very high, it is a very important compound when measuring the concentration in fine dust.


<br><br>
# 3.0 Other eye-catchings (sulfur dioxide-SO2, nitrogen dioxide-NO2)

<span id="start-ch">Looking</span> at the fluctuation of SO2 and NO2 for two days, it was also found that the most noticeable peak happened around 9 am, but it was not observed repeatedly every day, but just once. so research has to proceed for finding out some reasons if there were other causes.

>
| <img src="/images/post_img/20180927-02chemicals.png" width="400"> |
|:----------------------------------------------|
| **Fig.03** - SO2, NO2 changes |

<span id="start-ch">Other</span> chemical components, such as CO and O3, also have a slight change in the period, but I will not add any further, as no significant changes are observed.

<br><br>
# 4.0 After All

<span id="start-ch">So far</span>, I took two days of fine dust data with simple web scraping and looked at unusual changes during the period. Web scraping is not a reliable method of acquiring data, but it is simply a good way to collect and analyze data temporarily. If you want to continuously collect stable data in order to develop services, then it is more appropriate to get officially provided through the API of the public information portal operated by the country.

In a nutshell, web scraping is suitable if you want to collect various information from various sites in a short time, and it is more appropriate to use OPEN-API if you want to collect stable and formed information for service

** That's a wrap~..**
