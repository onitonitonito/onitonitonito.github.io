---
layout: default
permalink: /members/
---
# 1.0 Ordered list tag 를 이용하여 작성하는 경우

<ol>
{% for member in site.data.members %}
  <li>{{ member.name }} .... <a href="https://github.com/{{ member.github }}">
  https://github.com/{{ member.github }}</a> ::
  <a href="https://github.com/{{ member.github }}/{{ member.repo}}">{{ member.repo}}</a>
  </li>
{% endfor %}
</ol>



<br><br>
# 2.0 테이블을 이용해서 반복 작성하는 경우

<table>
  <!-- _data 폴더의 members.yml 기록내용을 가져오는 경우 (name, github, repo) -->
  {% for member in site.data.members %}
  <tr>
    <td>
      {% increment my_num %}.{{ member.name }}　
    </td>

    <td>
    <a href="https://github.com/{{ member.github }}">https://github.com/{{ member.github }}</a>　
    </td>

    <td>
      <a href="https://github.com/{{ member.github }}/{{ member.repo}}">{{ member.repo}}</a>
    </td>
  </tr>  
{% endfor %}
</table>
