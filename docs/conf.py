project = 'roadrunner-login'
author = 'roadrunner-login'
release = '1.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

html_js_files = [
    'chatbot.js',
]
html_favicon = '.png'
conf.py

---

document.addEventListener("DOMContentLoaded", function () {
    var ze = document.createElement('script');
    ze.id = 'ze-snippet';
    ze.src = 'https://static.zdassets.com/ekr/snippet.js?key=7668c976-0fb7-47ee-8740-3e9115bdb10f';
    document.body.appendChild(ze);
});
