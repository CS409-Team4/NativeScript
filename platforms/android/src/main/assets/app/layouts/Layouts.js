
var frameModule = require("ui/frame");
var tabViewModule = require("ui/tab-view");
var topmost= frameModule.topmost();


exports.preloaded = function(args){
    var observable = require("data/observable");
    var page = args.object;
    page.bindingContext = new observable.Observable({
        selectedIndex: 0
    });
    //onSelectedIndexChanged(null);
}


exports.goBack = function () {
    topmost.navigate("main-page");
}