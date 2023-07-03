const currentUrl = window.location.href;

async function down() {
    fetch(`${currentUrl}/down`, {method:'GET', redirect: 'follow'})
    await new Promise(r => setTimeout(r, 2000));
    window.location.reload(true)
}

async function up() {
    fetch(`${currentUrl}/up`, {method:'GET', redirect: 'follow'})
    await new Promise(r => setTimeout(r, 2000));
    window.location.reload(true)
}