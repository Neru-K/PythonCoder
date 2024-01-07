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
    const dir = obj.dir;
    const table = document.getElementById('content');
    dir.forEach(contestgenre => {
        contestgenre.contests.forEach(contest => {
            const dirname = contest.name;
            const tr = document.createElement('tr');
            const th = document.createElement('th');
            th.textContent = dirname;
            tr.appendChild(th);


            const problemset = contest.problemset;
            problemset.forEach(rank => {


                const td = document.createElement('td');
                if (contest.problems[rank]) {
                    const span = document.createElement('span');
                    span.textContent = contest.problems[rank].title;
                    span.addEventListener('click', function () {
                        console.log('span tag clicked');
                    });
                    td.appendChild(span);
                } else {
                    td.textContent = rank.toUpperCase();
                }
                tr.appendChild(td);
            });


            table.appendChild(tr);
        });

    });
}