/**
 * Creates /updates the cookie content
 * @param {string} name - Name of the cookie
 * @param {*} value - Content of the cookie
 * @param {*} days - Cookie expiring  
 */
function setCookie(name, value, days) {
    const expires = new Date(Date.now() + days*864e5).toUTCString();
    document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
}
/**
 * Read the cookie content
 * @param {string} name - Name of the cookie
 * @returns 
 */

function getCookie(name) {
    return document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=');
        return parts[0] === name ? decodeURIComponent(parts[1]) : r;
    }, '');
}

/**
 * Empty the cookie content
 */
function clearCookies()
{
    document.getElementById('username').value = '';
    document.getElementById('gameSessionId').value = '';
    
    setCookie('username', '', 1);
    setCookie('gameSessionId', '', 1);
}