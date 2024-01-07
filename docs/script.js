(function () {
    window.addEventListener('DOMContentLoaded', async function () {
        let response = null;
        const jsonUrl = 'blog.json';
        try {
            response = await fetchJson(jsonUrl);
            if (response) {
                const obj = JSON.parse(response);
                createListContents(obj);
                createDetailContents(obj);
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


function createListContents(obj) {
    const dir = obj.dir;
    const table = document.getElementById('content');
    dir.forEach((contestgenre, i) => {
        let str = "";
        contestgenre.contests.forEach((contest, j) => {
            let th = "<th>" + contest.name + "</th>";

            const problemset = contest.problemset;
            let tds = "";
            problemset.forEach(rank => {

                if (contest.problems[rank]) {
                    tds += '<td><span data-idx="' + i + '-' + j + '-' + rank + '">' + contest.problems[rank].title + '</span></td>';
                } else {
                    tds += "<td>" + rank.toUpperCase() + "</td>";
                }
            });


            str += "<tr>" + th + tds + "</tr>";
        });
        table.insertAdjacentHTML("beforeend", str);
    });
}

function createDetailContents(obj) {
    const table = document.getElementById('content');
    const details = document.getElementById('details');
    const spans = document.querySelectorAll('[data-idx]');
    spans.forEach(span => {
        span.addEventListener('click', function () {
            table.style.display = "none";
            details.style.display = "block";
            const attr = span.getAttribute('data-idx').split('-');
            console.log(attr);
            const contestgenre = obj.dir[attr[0]].contestgenre;
            const title = obj.dir[attr[0]].contests[attr[1]].problems[attr[2]].title;
            const body = obj.dir[attr[0]].contests[attr[1]].problems[attr[2]].body;
            console.log(contestgenre);
            console.log(title);
            console.log(body);
            let str = "<h1>" + title + "</h1>";
            body.forEach(el => {
                if (el.tag == "code") {
                    str += '<pre><code class="language-python">' + el.text + '</code></pre>';
                } else {
                    str += "<" + el.code + ">" + el.text + "</" + el.code + ">";
                }
            });
            details.insertAdjacentHTML('beforeend', str);
            hljs.highlightAll();
        });
    });

}