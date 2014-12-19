<script>
// Import data.
window.pocData = {};
window.pocData.data_points = [];
{% for d in data_points %}
window.pocData.data_points.push({{d.json|safe}});{% endfor %}
window.pocData.milestones = [];
{% for m in milestones %}
window.pocData.milestones.push({{m.json|safe}});{% endfor %}
</script>