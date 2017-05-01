
var frameModule = require("ui/frame");
var tabViewModule = require("ui/tab-view");
var topmost= frameModule.topmost();

exports.selectedIndexChanged = function (args) {
    var page = args.object;
    var tabview = page.getViewById("tabview");
    var idx = tabview.selectedIndex;

    var stack = tabview.items[0];
    stack.iconSource = idx == 0 ? "res://stack1" : "res://stack";

    var grid = tabview.items[1];
    grid.iconSource = idx == 1 ? "res://grid1" : "res://grid";

    var wrap = tabview.items[2];
    wrap.iconSource = idx == 2 ? "res://wrap1" :"res://wrap";

    var dock = tabview.items[3];
    dock.iconSource = idx == 3 ? "res://dock1" :"res://dock";

    var absolute = tabview.items[4];
    absolute.iconSource = idx == 3 ? "res://absolute1":"res://absolute";
}

exports.goBack = function () {
    topmost.navigate("main-page");
}