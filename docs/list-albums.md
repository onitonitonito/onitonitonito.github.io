---
layout: default
permalink: /albums/
---
{% for album in site.albums %}

<a href="{{album.music}}">
  <img src="{{album.img}}" width="300"></a>
  <h1> {{ album.title }} </h1>

  <p>[Arist] Performed by ... {{ album.artist }}<br>
    {% if album.director %}
    [Direct] Directed by ... {{ album.director }}
    {% endif %}

  <br>
    {% for work in album.works %}
      <h1> {{ work.title }} </h1>
      <p> [Compose] Composed by ... {{ work.composer }}</p>
      <ol>
        {% for track in work.tracks %}
          <li>{{ track.title }} ({{ track.duration }})</li>
        {% endfor %}
      </ol>
    {% endfor %}
  </p>
  <br><br>
{% endfor %}
