{% if messages %}
<div class="messages">
    {% for message in messages %}
        <div class="alert {% if message.tags %}alert-{{ message.tags }}{% endif %}">
            {{ message }}
        </div>
    {% endfor %}
</div>
{% endif %}
