var pageModule = require("ui/page");
var frameModule = require("ui/frame");
var topmost= frameModule.topmost();


exports.pageLoaded = function() {
    console.log("Hello World3!");
};

exports.goBack = function () {
    topmost.navigate("main-page");
}