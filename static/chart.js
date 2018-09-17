var chartData = window.chartData;

var elm = document.getElementById("myChart").getContext('2d');
var maxLabel = chartData[chartData.length - 1].x;
var labels = [];
for (var i = 0; i < chartData.length; i++) {
    labels.push((maxLabel / chartData.length) * i + 1)
}
new Chart(elm, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            data: chartData,
            label: "x/y",
            borderColor: "#8e5ea2",
            fill: false
        }
        ]
    }

});
