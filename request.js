var Request = require("request");

Request.get("https://api.bitso.com/v3/available_books/", (error, response, body) => {
    if(error) {
        return console.dir(error);
    }
    console.dir(JSON.parse(body));
});