// We need this to build our post string
var querystring = require('querystring');
var http = require('http');
var fs = require('fs');

function PostCode(postData) {
	// An object of options to indicate where to post to
	var postData = querystring.stringify(jsonData);
	var accountID = "58a981581756fc834d905a55";
	var APIKEY = "df8a613cd6635b6513d8050b63b13dde";
	var post_options = {
		host: 'api.reimaginebanking.com',
		port: 80,
		path: '/accounts/' + accountID + '/purchases?key=' + APIKEY,
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'Content-Length': Buffer.byteLength(postData)
		}
	};

	// Set up the request
	var post_req = http.request(post_options, function(res) {
		res.setEncoding('utf8');
		res.on('data', (chunk) => {
			console.log('Response: ' + chunk);
		});
		res.on('end', () => {
			console.log('No more data in response.');
		});
	});

	// post the data
	post_req.write(postData);
	post_req.end();

}

// This is an async file read
fs.readFile('out.json', 'utf-8', (err, data) => {
	if (err) {
		console.log("FATAL An error occurred trying to read in the file: " + err);
		process.exit(-2);
	}
	// Make sure there's data before we post it
	if(data) {
		jsonData = JSON.parse(data);
		jsonData.forEach(function (d) { PostCode(d); });
	}
	else {
		console.log("No data to post");
		process.exit(-1);
	}
});
