
var frameModule= require("ui/frame");
var selection_data = require("./Selection_data");
var labelModule = require("ui/label");
var topmost= frameModule.topmost();

exports.pageLoaded = function(args){
	var page = args.object;
	page.bindingContext = new selection_data();
}
exports.SegTap = function(){
	console.log("hello");
}
