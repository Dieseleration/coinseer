/*!
 * express
 * Copyright(c) 2009-2013 TJ Holowaychuk
 * Copyright(c) 2013 Roman Shtylman
 * Copyright(c) 2014-2015 Douglas Christopher Wilson
 * MIT Licensed
 */

'use strict';

module.exports = require('./lib/express');

var gdax = require('gdax');
var http = require('http');
//var fs = require('fs');

var pubclient = new gdax.PublicClient(); //init client
var getgdaxdata = function(err, response, data) {
	console.log('called getgdaxdata function');
	console.log(data);
};

var output = pubclient.getProductTicker(getgdaxdata);
//console.log(output);





//fs.writeFile("/testfile.txt", output, function(err) {
	//console.log('file saved');
//});
//console.log(data);



