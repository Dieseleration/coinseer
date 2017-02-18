const WebSocket = require('ws');
const gdax = require('gdax');

const ws = new WebSocket('http://localhost:3003');
ws.on('open', () => console.log('socket open'));
const pub = new gdax.PublicClient();
setInterval(() => {
pub.getProductHistoricRates({ granularity: 100 }, (err, res, data) => {
  ws.send(data);
  console.log(data);
});
}, 1000);
