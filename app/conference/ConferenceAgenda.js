var frameModule = require("ui/frame");
var topmost= frameModule.topmost();
var observableArray = require("data/observable-array");
var search_data = require("./Search_data");

exports.pageLoaded = function(args){
    console.log("Welcome Subin!!");
    var page = args.object;
	page.bindingContext = new search_data();

}

exports.toggleFavourite = function(args){
    var session = args.view.bindingContext;
    session.isFavourite = !session.isFavourite;
    var gridview = args.object;
    var img = gridview.getViewById("imgID");

    if(img.src =='res://add_to_fav'){
        gridview.backgroundColor='#19FFFFFF'
        img.src = 'res://add_to_fav_1';
    }
    else{
        gridview.backgroundColor='#00000000'
        img.src = 'res://add_to_fav';
    }
};

exports.goBack = function () {
    topmost.navigate("main-page");
}

exports.doNotShowAndroidKeyboard = function(args) {
    var searchBar = args.object;
    if (searchBar.android) {
        searchBar.android.clearFocus();
    }
}
