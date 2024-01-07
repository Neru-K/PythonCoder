(function () {
    window.addEventListener('DOMContentLoaded', async function () {
        const jsonUrl = 'https://raw.githubusercontent.com/Neru-K/PythonCoder/master/docs/blog.json';
        try {
            const contents = await fetchJson(jsonUrl);
            if (contents) {
                createToppageContent(JSON.parse(contents));
            }
        } catch (error) {
            console.error('Error in fetching or processing JSON:', error);
        }
    });
}());

function fetchJson(url) {
    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => JSON.stringify(data, null, 2))
        .catch(error => {
            console.error('Error fetching JSON:', error);
            throw error;
        });
}


function createToppageContent(obj) {
    const array = obj.dir;
    const table = document.getElementById('content');
    array.forEach(element => {
        const dirname = element.dirname;
        const tr = document.createElement('tr');
        const th = document.createElement('th');
        th.textContent = dirname;
        tr.appendChild(th);
        table.appendChild(tr);
    });
}