---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# Chart.js with Jupyter book - 5

## Testing on dynamic data
```
<div>
  <canvas id="addableChart"></canvas>
</div>

<script>
  const labels = [
    1,2,3,4,5,6,7
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'Test dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };
</script>

<script>
  const myChart = new Chart(
    document.getElementById('addableChart'),
    config
  );
</script>
<script>
function addDigit(){
  myChart.data.labels.push(myChart.data.labels.length+1);
  myChart.data.datasets[0].data.push(0);
  myChart.update();
}
</script>
<button id='btn' onClick='addDigit()'>Add</button>

```
<div>
  <canvas id="addableChart"></canvas>
</div>

<script>
  const labels = [
    1,2,3,4,5,6,7
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'Test dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };
</script>

<script>
  const myChart = new Chart(
    document.getElementById('addableChart'),
    config
  );
</script>
<script>
function addDigit(){
  myChart.data.labels.push(myChart.data.labels.length+1);
  myChart.data.datasets[0].data.push(0);
  myChart.update();
}
</script>
<button id='btn' onClick='addDigit()'>Add</button>
