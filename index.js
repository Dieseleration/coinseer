/*!
 * express
 * Copyright(c) 2009-2013 TJ Holowaychuk
 * Copyright(c) 2013 Roman Shtylman
 * Copyright(c) 2014-2015 Douglas Christopher Wilson
 * MIT Licensed
 */

'use strict';

module.exports = require('./lib/express');

var gdax = require('gdax');	//gdax
var http = require('http');	//http
var socket = require('ws');	//websocket
var fs = require('fs');		//filesystem ops


var pub = new gdax.PublicClient(); //init client

/*
var getgdaxdata = function(err, response, data) {
	console.log('called getgdaxdata function');
	console.log(data);
	
};
*/

//Product Data Grabber callback
var grabfunc = function(err, response, data) {
	console.log('pinging GDAX');
	console.log(data);
}

var hBTC = pub.getProductHistoricRates({'granularity': 50}, grabfunc);
var ws = new socket('marquiseIP/socketnum');
ws.on('open', function open() {
	ws.send(pub.getProductHistoricRates{'granularity': 300}, grabfunc);
});

