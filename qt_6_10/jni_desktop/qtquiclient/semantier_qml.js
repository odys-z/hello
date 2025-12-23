.pragma library

/**
 * ISSUE This function always get xhr.status = 0, and responsteText = '' with GET to jserv-album/login.serv.
 * 
 * The probably reason is that the jserv doesn't response with standard headers:
 * <pre>HTTP/1.1 200 OK
 * Server: Portfolio 0.7
 * Date: Tue, 23 Dec 2025 08:12:43 GMT
 * synode: X29
 * Transfer-Encoding: chunked</pre>
 * which is acceped by Chrome.
 * 
 * @param {object} options
 * @param {string} options.jserv
 * @param {function(MsgCode, AnsonResp): void} options.onPost
 * @param {function(MsgCode, AnsonResp): void} options.onGet
 * @param {function(MsgCode, AnsonResp): void} options.onError
 */
function ping({jserv, onPost, onGet, onError} = {}) {
    let post = false, get = false;
    if (onPost) post = true
    if (onGet) get = true
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.HEADERS_RECEIVED) {
            print('HEADERS_RECEIVED');
        } else if(xhr.readyState === XMLHttpRequest.DONE) {
            print('DONE', xhr.responseText === undefined, xhr.responseText === '', xhr.responseText);
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                console.log(200, data);
            } else {
                console.log("Error: " + xhr.status + " " + xhr.statusText);
            }
            const response = JSON.parse(xhr.responseText.toString());
            if (post)
                onPost(0, response);
            else
                onGet(0, response);
        }
    }

    console.log(post ? "POST" : "GET", jserv);
    xhr.open(post ? "POST" : "GET", jserv);
    xhr.overrideMimeType("text/plain; charset=x-user-defined");
    xhr.send();
}
