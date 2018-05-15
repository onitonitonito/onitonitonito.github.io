---
layout: default
permalink: /blog/
---
# 블로그 테스트의 목록

<!-- blog post contents : described as { { content } } -->
<article class="post">

<!-- strftime format : http://strftime.org -->
  {% for post in site.posts %}
    <li>
      {{ post.date | date: "%Y. %m/%d" }} ...
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a><br>
    </li>  
  {% endfor %}


<br><br>


  {% for post in site.posts %}
      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
      <div class="post-list">{{ post.excerpt }}</div>
      <div class="read-more">{{ post.date | date: "%Y. %-m/%-d (%a)" }}
        ... [<a href="{{ site.baseurl }}{{ post.url }}">Read More</a>]</div>
  {% endfor %}

</article>
