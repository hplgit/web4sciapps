<p>
{% if result != None %}
  {% if type(result) == type("") and
        result[:-4] == '.png' or  result[:-4] == '.gif' or
        result[:-4] == '.jpg' %}
<img src="{{ result }}">
  {% else %}
{{ str(result) }}
  {% endif %}
{% endif %}
</p>
