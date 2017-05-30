var frameModule= require("ui/frame");
var topmost= frameModule.topmost();

exports.onNavigatingTo = function(args){
	var page = args.object;
	page.bindingContext = page.navigationContext;
}

exports.onToggleFavouriteTap = function(args){
	var page = args.object.page;
	var bindingData = page.bindingContext;

	bindingData['IsFavourite'] = !bindingData['IsFavourite'];
	topmost.goBack();
}
exports.onDeleteTap = function(args){
	var page = args.object.page;
	var bindingData = page.bindingContext;

	bindingData['isDeleted'] = true;
	topmost.goBack();
}

exports.goBack = function () {
	topmost.goBack();
}
