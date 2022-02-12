#!/usr/bin/env python
# coding: utf-8

# # Chart.js with Jupyter book - 6
# 
# ## Test with random data generation
# 
# <div>
#   <canvas id="addableChart"></canvas>
# </div>
# Max length: <input id="input" value=10 />
# 
# <script>
#   function addDigit(){
#     var inputValue = parseInt(document.getElementById('input').value);
#     console.log(myChart.data.labels.length > inputValue, myChart.data.labels.length, inputValue)
#     if(myChart.data.labels.length > inputValue){
#       myChart.data.datasets[0].data.shift();
#       myChart.data.labels.shift();
#       console.log(myChart.data.labels);
#     }
#     myChart.data.datasets[0].data.push(getRandomInt(0,50));
#     myChart.data.labels.push(myChart.data.labels.length+1);
#     myChart.update();
#   }
#   function getRandomInt(min, max) {
#     min = Math.ceil(min);
#     max = Math.floor(max);
#     return Math.floor(Math.random() * (max - min) + min);
#   }
# 
# 
#   const labels = [
#     1,2,3,4,5,6,7
#   ];
#   const data = {
#     labels: labels,
#     datasets: [{
#       label: 'Test dataset',
#       backgroundColor: 'rgb(255, 99, 132)',
#       borderColor: 'rgb(255, 99, 132)',
#       data: [0, 10, 5, 2, 20, 30, 45],
#     }]
#   };
# 
#   const config = {
#     type: 'line',
#     data: data,
#     options: {}
#   };
#   const myChart = new Chart(
#     document.getElementById('addableChart'),
#     config
#   );
# 
#   setInterval(addDigit, 1000);
# </script>
