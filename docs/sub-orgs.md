---
layout: default
permalink: /orgs/
---
<h1>ORGS🐴</h1>

<ol>

{% for org_hash in site.data.orgs %}
  {% assign org = org_hash[1] %}
    <li>
      <a href="https://github.com/{{ org.username }}">{{ org.name }}</a>
      ({{ org.members | size }} members)
    </li>

    <ul>
    {% for member in org.members %}
      <li>{{ member.name }} .... <a href="https://github.com/{{ member.github }}">
      https://github.com/{{ member.github }}</a>
      </li>
    {% endfor %}
    </ul>

  <br><br>
{% endfor %}

</ol>
