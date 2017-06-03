var frameModule= require("ui/frame");
var topmost= frameModule.topmost();

exports.pageLoaded = function(args){
	var page = args.object;
	page.bindingContext = page.navigationContext;
	var webview = page.getViewById("webview");
	webview.src = page.navigationContext;
}

exports.goBackWeb = function(args){
	topmost.goBack();
}
