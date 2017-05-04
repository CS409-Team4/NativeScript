var pageModule = require("ui/page");
var frameModule = require("ui/frame");


exports.pageLoaded = function() {
    console.log("Welcome Subin!!");
};


function clickcard(eventData) {
    var topmost= frameModule.topmost();
    var str = String(eventData.object).match(/:[0-9][0-9]:/g);
    if (str == ":10:"){
        console.log("layouts");
        topmost.navigate("layouts/Layouts");
    }
    else if(str == ":14:"){
        console.log("user profile");
        topmost.navigate("user_profile/UserProfile");
    }
    else if(str == ":18:"){
        console.log("conference agenda");
        topmost.navigate("conference/ConferenceAgenda");
    }
    else if(str == ":22:"){
        console.log("Item layouts");
        topmost.navigate("itemlayout/ItemLayout");
    }
    else if(str == ":26:"){
        console.log("hello");
    }
    else if(str == ":30:"){
        console.log("selection");
    }    
}
exports.clickcard = clickcard;