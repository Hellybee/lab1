var serialport = require('serialport');
var SerialPort = serialport.SerialPort;

const port = new SerialPort({ 
  path:'COM3', 
  baudRate: 9600,
   });

console.log(SerialPort);
port.on('open', function(){
  console.log('Serial Port OPEN');
});

port.on('data', function(data){
  console.log("LightSensor Value: ", data.toString());
});

port.on('error', (err) => {
  console.error('오류 발생: ', err);
});