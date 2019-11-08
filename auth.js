var request = require('request');
//Put var payload = "clientid:clientsecret";
var encodedPayload = new Buffer(payload).toString("base64");
var token;

var opts = {
    url: "https://accounts.spotify.com/api/token",
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encodedPayload
    },
    body: "grant_type=client_credentials&scope=playlist-modify-public playlist-modify-private user-modify-playback-state"
};

request.post(opts, function (err, res, body) {
    //console.log('error', err);
    //console.log('mamla');
    //console.log(res);
    console.log('From Spotify: Status: ', res.statusCode);
    //console.log('body', body);
    token = body;


    var opts1 = {
        url: "http://localhost:8080/auth",
        method: "POST",
        body: token
    };

    request.post(opts1, function (err1, res1, body1) {
        //console.log('error', err1);
        console.log('Sent to Flask server: Status: ',res1.statusCode);
        console.log('Recieved from Flask server', body1);
    });
});
