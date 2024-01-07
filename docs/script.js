(function () {
    window.addEventListener('DOMContentLoaded', function () {
        // JSONファイルのURL
        const jsonUrl = 'https://raw.githubusercontent.com/Neru-K/PythonCoder/master/docs/blog.json';

        // JSONデータを取得して表示
        fetch(jsonUrl)
            .then(response => response.json())
            .then(data => {
                const contentDiv = document.getElementById('content');
                contentDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
            })
            .catch(error => console.error('Error fetching JSON:', error));
    });
}());