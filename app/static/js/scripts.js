function down() {
    fetch("http://127.0.0.1:5000/down", {method:'GET', redirect: 'follow'})
}

function up() {
    fetch("http://127.0.0.1:5000/up", {method:'GET', redirect: 'follow'})
}