function confirmDelete(url) {
    if (confirm('Are you sure you want to delete this?')) {
        window.location.href = url;
    }
}

function showEditForm(formId) {
    document.getElementById(formId).style.display = 'block';
}

function hideEditForm(formId) {
    document.getElementById(formId).style.display = 'none';
}
