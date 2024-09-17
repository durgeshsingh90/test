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





<script>
function openFileExplorer(filePath) {
    // Sending a POST request to a Django view to open the file explorer
    fetch("{% url 'binblock:open_file_explorer' %}", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: JSON.stringify({ 'file_path': filePath })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('File explorer opened successfully.');
        } else {
            alert('Failed to open file explorer: ' + data.error);
        }
    });
}
</script>

