---
layout: default
permalink: /albums/
---
# 1.0 test albums
> 1. this[1] = {{site.albums[1]}}
> 1. that.ex01 = {{site.albums.ex01}}
> 1. that.title = {{site.albums.title}}
> * -

{% for album in site.albums %}
  this= {{ album }}
  <h2>{{ album.title }}</h2>

  <p>Performed by {{ album.artist }}
    {% if album.director %}
      , directed by {{ album.director }}
    {% endif %}
  </p>

  {% for work in album.works %}
    <h3>{{ work.title }}</h3>
    <p>Composed by {{ work.composer }}</p>
    <ul>
      {% for track in work.tracks %}
        <li>{{ track.title }} ({{ track.duration }})</li>
      {% endfor %}
    </ul>
  {% endfor %}
{% endfor %}
