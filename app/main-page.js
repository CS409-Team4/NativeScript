var pageModule = require("ui/page");
var frameModule = require("ui/frame");

exports.pageLoaded = function() {
	var topmost= frameModule.topmost();
    console.log("Welcome Subin!!");
    topmost.navigate("web_naver/WebNaver");
};


exports.clickcard = function (eventData) {
	var topmost= frameModule.topmost();
    var str = String(eventData.object).match(/:[0-9][0-9]:/g);
    console.log(str);
    if (str == ":13:"){
        console.log("layout2s");
        topmost.navigate("layouts/Layouts");
    }
    else if(str == ":17:"){
        console.log("user profile");
        topmost.navigate("user_profile/UserProfile");
    }
    else if(str == ":21:"){
        console.log("conference agenda");
        topmost.navigate("conference/ConferenceAgenda");
    }
    else if(str == ":25:"){
        console.log("Item layouts");
        topmost.navigate("itemlayout/ItemLayout");
    }
    else if(str == ":29:"){
		console.log('naver');
        topmost.navigate("web_naver/WebNaver");
    }
    else if(str == ":33:"){
        console.log("selection");
        topmost.navigate("selection/Selection");
    }
}


exports.openDrawer = function(args){
    var topmost= frameModule.topmost();
    var drawer = topmost.getViewById('drawer');
    drawer.showDrawer();
    var btn = args.object;
    btn.actionBarHidden = true;
}
