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
# Chart.js with Jupyter book - 6

## Test with random data generation

<div>
  <canvas id="addableChart"></canvas>
</div>
<div class="slidecontainer">
  Max length (30-100): <input type="range" min="30" max="100" value="30" class="slider" id="input">
</div>

<script>
  function addDigit(){
    var inputValue = parseInt(document.getElementById('input').value);
    while(myChart.data.datasets[0].data.length+1 > inputValue){
      myChart.data.datasets[0].data.shift();
      myChart.data.labels.shift();
      console.log(myChart.data.labels);
    }
    myChart.data.datasets[0].data.push(getRandomInt(0,50));
    myChart.data.labels.push(myChart.data.labels.length+1);
    myChart.update();
  }
  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
  }


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
    }],
    options: {
      animation: {
        duration: 0
      }
    }
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };
  const myChart = new Chart(
    document.getElementById('addableChart'),
    config
  );

  setInterval(addDigit, 100);
</script>
