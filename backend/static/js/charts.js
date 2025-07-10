const ctxHR = document.getElementById('chart-hr').getContext('2d');
const ctxSpO2 = document.getElementById('chart-spo2').getContext('2d');
const ctxTemp = document.getElementById('chart-temp').getContext('2d');
const ctxAlcohol = document.getElementById('chart-alcohol').getContext('2d');

let labels = [];
let hrData = [], spo2Data = [], tempData = [], alcoholData = [];

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: { title: { display: true, text: 'Time' } },
    y: { beginAtZero: true }
  }
};

const chartHR = new Chart(ctxHR, {
  type: 'line',
  data: {
    labels: labels,
    datasets: [{
      label: 'Heart Rate (BPM)',
      data: hrData,
      borderColor: 'red',
      fill: false
    }]
  },
  options: chartOptions
});

const chartSpO2 = new Chart(ctxSpO2, {
  type: 'line',
  data: {
    labels: labels,
    datasets: [{
      label: 'SpO₂ (%)',
      data: spo2Data,
      borderColor: 'blue',
      fill: false
    }]
  },
  options: chartOptions
});

const chartTemp = new Chart(ctxTemp, {
  type: 'line',
  data: {
    labels: labels,
    datasets: [{
      label: 'Temperature (°F)',
      data: tempData,
      borderColor: 'orange',
      fill: false
    }]
  },
  options: chartOptions
});

const chartAlcohol = new Chart(ctxAlcohol, {
  type: 'line',
  data: {
    labels: labels,
    datasets: [{
      label: 'Alcohol Level (%)',
      data: alcoholData,
      borderColor: 'green',
      fill: false
    }]
  },
  options: chartOptions
});

async function fetchVitals() {
  const patientId = document.getElementById('patientSelect').value;
  const timeRange = document.getElementById('timeRange').value;

  let url = `/api/vitals?range=${timeRange}`;
  if (patientId) {
    url += `&patient_id=${patientId}`;
  }

  const res = await fetch(url);
  const data = await res.json();

  labels.length = hrData.length = spo2Data.length = tempData.length = alcoholData.length = 0;

  data.forEach(entry => {
    const t = new Date(entry.timestamp).toLocaleTimeString();
    labels.push(t);
    hrData.push(entry.heart_rate);
    spo2Data.push(entry.spo2);
    tempData.push(entry.temperature);
    alcoholData.push(entry.alcohol_level);
  });

  chartHR.update();
  chartSpO2.update();
  chartTemp.update();
  chartAlcohol.update();
}

fetchVitals();
setInterval(fetchVitals, 15000);
