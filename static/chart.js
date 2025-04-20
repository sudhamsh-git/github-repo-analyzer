function updateCharts(data) {
    const contributorsCanvas = document.getElementById('contributors-chart');
    const commitsCanvas = document.getElementById('commits-chart');

    const contributorsChart = new Chart(contributorsCanvas, {
        type: 'bar',
        data: {
            labels: data.contributors.map(contributor => contributor.login),
            datasets: [{
                label: 'Contributors',
                data: data.contributors.map(contributor => contributor.contributions),
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const commitsChart = new Chart(commitsCanvas, {
        type: 'line',
        data: {
            labels: data.commits.map(commit => commit.commit.author.date),
            datasets: [{
                label: 'Commits',
                data: data.commits.map(commit => commit.commit.author.date.length),
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}