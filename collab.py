{% if messages %}
<div class="messages">
    {% for message in messages %}
        <div class="alert {% if message.tags %}alert-{{ message.tags }}{% endif %}">
            {{ message }}
            {% if message.tags == 'success' and file_path %}
            <br>
            <span>File path: {{ file_path }}</span>
            <button class="btn btn-link" onclick="openFileExplorer('{{ file_path }}')">Open</button>
            {% endif %}
        </div>
    {% endfor %}
</div>
{% endif %}
