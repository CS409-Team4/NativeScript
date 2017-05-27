var switchModule = require("ui/switch");
var frameModule = require("ui/frame");
var application = require("application");
var topmost= frameModule.topmost();
exports.checkboxclick = function() {
    var topmost= frameModule.topmost();
    var checkBox = topmost.getViewById('checkbox');
    var password = topmost.getViewById("password");
    if(checkBox.checked == true){
        password.secure = true;
    } else{
        password.secure = false;
    }
};

exports.btnclick = function(){
    var Toast = android.widget.Toast;
    Toast.makeText(application.android.context, "Update Tapped!", Toast.LENGTH_SHORT).show();
}

exports.imgclick = function(){
    var Toast = android.widget.Toast;
    Toast.makeText(application.android.context, "Change Image Tapped!", Toast.LENGTH_SHORT).show();
}

exports.goBack = function () {
    topmost.navigate("main-page");
}