---
layout: default
permalink: /orgs/
---
<h1>ORGS🐴</h1>

<ol>

{% for org_hash in site.data.orgs %}
  {% assign org = org_hash[1] %}
    <li>
      <a href="https://github.com/{{ org.username }}" target="new">{{ org.name }}</a>
      ({{ org.members | size }} members)
    </li>

    <ul>
    {% for member in org.members %}
      <li>{{ member.name }} .... <a href="https://github.com/{{ member.github }}" target="new">
      https://github.com/{{ member.github }}</a>
      </li>
    {% endfor %}
    </ul>
  <hr>  

  <br><br>
{% endfor %}

</ol>
