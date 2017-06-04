var frameModule = require("ui/frame");
var topmost= frameModule.topmost();

exports.openDrawer = function(args){
	var drawer = topmost.getViewById('drawer');
	drawer.showDrawer();
	var btn = args.object;
	btn.actionBarHidden = true;
}
exports.closeDrawer = function(args){
	var drawer = topmost.getViewById('drawer');
	drawer.closeDrawer();
}
exports.dropMenu = function(args){
	
}
exports.onTapLogo = function(args){
	console.log("onTapLogo");
	var page= args.object.page;
	var webview = page.getViewById("webview");
	webview.reload();
}
exports.onTap = function(args){
	var page = args.object.page;
	var selected_btn = args.object;
	page.getViewById("0").class= 'btn';
	page.getViewById("1").class='btn';
	page.getViewById("2").class='btn';
	page.getViewById("3").class='btn';
	page.getViewById("4").class='btn';
	selected_btn.class='selected-btn';
}
var webviewModule = require("tns-core-modules/ui/web-view");
exports.onTapEmail = function(args){
	var navigationEntry = {
		moduleName: "web_naver/DrawerWeb",
		context: "http://mail.naver.com"
	};
	topmost.navigate(navigationEntry);
}
exports.onTapCafe = function(args){
	var navigationEntry = {
		moduleName: "web_naver/DrawerWeb",
		context: "http://cafe.naver.com"
	};
	topmost.navigate(navigationEntry);
}
exports.onTapBlog = function(args){
	var navigationEntry = {
		moduleName: "web_naver/DrawerWeb",
		context: "http://blog.naver.com"
	};
	topmost.navigate(navigationEntry);
}
exports.onTapKin = function(args){
	var navigationEntry = {
		moduleName: "web_naver/DrawerWeb",
		context: "http://kin.naver.com"
	};
	topmost.navigate(navigationEntry);
}
