(function () {
    window.addEventListener('DOMContentLoaded', async function () {
        let contents = null;
        const jsonUrl = 'blog.json';
        try {
            contents = await fetchJson(jsonUrl);
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
            let str = "";
            let th = "<th>" + contest.name + "</th>";

            const problemset = contest.problemset;
            let tds = "";
            problemset.forEach(rank => {

                if (contest.problems[rank]) {
                    tds += "<td><span>" + contest.problems[rank].title + "</span></td>";
                } else {
                    tds += "<td><span>" + rank.toUpperCase() + "</span></td>";
                }
            });


            str += "<tr>" + th + tds + "</tr>";
        });
        table.insertAdjacentHTML("beforeend", str);
    });
}