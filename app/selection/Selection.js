
var frameModule= require("ui/frame");
var selection_data = require("./Selection_data");
var gestures = require("ui/gestures");
var labelModule = require("ui/label");
var topmost= frameModule.topmost();

exports.pageLoaded = function(args){
	var page = args.object;
	page.bindingContext = new selection_data();
	var label = new labelModule.Label();
}

exports.goBack = function () {	
	topmost.goBack();
    //topmost.navigate("main-page");
}
exports.onItemTap = function(args){
	var page = args.object.page;
	var pageBindingContext =page.bindingContext;
	var navigationEntry = {
		moduleName: "selection/Detail_Page",
		context: pageBindingContext.posts[args.itemIndex],
	};
	topmost.navigate(navigationEntry);
}
exports.onLongPress = function(){
	console.log("onLongPress");
}
