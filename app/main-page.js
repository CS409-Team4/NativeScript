var pageModule = require("ui/page");
var frameModule = require("ui/frame");
var observable = require("data/observable");


exports.pageLoaded = function() {
    console.log("Welcome Subin!!");
};


exports.clickcard = function (eventData) {
    var topmost= frameModule.topmost();
    var str = String(eventData.object).match(/:[0-9][0-9]:/g);
    console.log(str);
    if (str == ":13:"){
        console.log("layouts");
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
    }    
}


exports.openDrawer = function(args){
    var topmost= frameModule.topmost();
    var drawer = topmost.getViewById('drawer');
    drawer.showDrawer();
    var btn = args.object;
    btn.actionBarHidden = true;
}
