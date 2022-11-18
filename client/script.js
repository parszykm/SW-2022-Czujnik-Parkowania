axios.get('http://127.0.0.1:5000/plot').then((res) => {
    Plotly.newPlot('plot', [{
        y:[res.data], 
        type: 'line',
    }], {
        xaxis: {
            title: 'Czas [s]',
          },
          yaxis: {
            title: 'Odległość [cm]',
          }
    })
})  

var cnt = 0

setInterval(() => {
    var carImage = document.getElementById('car_img')
    axios.get('http://127.0.0.1:5000/plot').then((res) => {
        Plotly.extendTraces('plot', { y:[[res.data]],}, [0])
        cnt++;

        if(cnt > 10){
            Plotly.relayout('plot', {
                xaxis: {
                    range: [cnt-10, cnt]
                }
            })
        }
        if(res.data < 20){
            carImage.src='./assets/car_red.png'
        }
        else if(res.data < 60){
            carImage.src='./assets/car_orange.png'
        }
        else if(res.data < 100){
            carImage.src='./assets/car_green.png'
        }
        else {
            carImage.src='./assets/car_silent.png'
        }
    }) 

},300)

