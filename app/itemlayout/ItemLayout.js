var frameModule = require("ui/frame");
var topmost= frameModule.topmost();
var observableArray = require("data/observable-array");
var dataobj = new observableArray.ObservableArray();



var item = (function () {
    function item(imgName, title, author) {
        this.imgName = imgName;
        this.title = title;
        this.author = author;
    }
    return item;
}());

dataobj.dataItems = [
    new item("~/images/paleo1.jpg", "Dried Meat with Spices", "Nice to Meat You"),
    new item("~/images/paleo2.jpg", "Golden Chicken", "Chicken's Heaven", "Chicken's Heaven"),
    new item("~/images/paleo3.jpg", "Pork Steak with Vegetables", "Nice to Meat You"),
    new item("~/images/paleo4.jpg", "Lamb Cotlets", "Nice to Meat You"),
    new item("~/images/paleo5.jpg", "Salmon Stea", "Ron's Fishery"),
    new item("~/images/dessert1.jpg", "These Rolls..", "Le Bakery de Trevi"),
    new item("~/images/dessert2.jpg","Chocolate Cake", "The Sweetest Thing"),
    new item("~/images/dessert3.jpg", "Rainbow Chocolate Pudding","Sweet and Sweeter"),
    new item("~/images/dessert4.jpg", "Ice-cream Sandwich","The Sweetest Thing"),
    new item("~/images/dessert5.jpg", "Le Macarons de Lyon", "Le Bakery de Trevi"),
    new item("~/images/dessert6.jpg", "Le Tiramisu de Treviso", "Sweet and Sweeter"),
    new item("~/images/dessert7.jpg", "Creme Caramel", "The Sweetest Thing"),
    new item("~/images/dessert8.jpg", "Be Fit, Be Healthy Fruit Mix","Sweet and Sweeter"),
    new item("~/images/drink1.jpg", "Ceylon Tea","The Healthy Bar"),
    new item("~/images/drink2.jpg", "Orange Juice, Fresh","The Healthy Bar"),
    new item("~/images/drink3.jpg", "A Glass of Wine","Tonight's Bar"),
    new item("~/images/drink4.jpg", "Barista's Masterpiece","The Cafe Near You"),
    new item("~/images/drink5.jpg", "Coffee", "Sweet and Sweeter"),
    new item("~/images/drink6.jpg", "Watermelon Dream", "The Healthy Bar"),
    new item("~/images/drink7.jpg", "Mojito", "Tonight's Bar"),
    new item("~/images/drink8.jpg", "Raspberry Smoothie", "The Healhy Bar"),
    new item("~/images/drink9.jpg", "Smootie (Different Flavors)", "Sweet and Sweeter"),
    new item("~/images/drink10.jpg", "Soda", "The Healthy Bar"),
    new item("~/images/drink11.jpg", "Lemon Ice Tea", "Sweet and Sweeter"),
    new item("~/images/drink12.jpg", "Crystal Water with Almond Oil", "The Healthy Bar"),
    new item("~/images/breakfast1.jpg", "The Fresh Sandwich", "Sandwiches and More"),
    new item("~/images/breakfast2.jpg", "The Healthy Sandwich", "Sandwiches and More"),
    new item("~/images/breakfast3.jpg", "Crispy Chicken with Avocado Sandwich", "Chicken's Heaven"),
    new item("~/images/breakfast4.jpg", "Beef Sandwich", "Nice to Meat You"),
    new item("~/images/breakfast5.jpg", "Tuna Sandwich", "Ron's Fishery"),
    new item("~/images/breakfast6.jpg", "Fruit Cake", "ReFresh"),
    new item("~/images/main1.jpg", "A Quick Snack Burger", "Nice to Meat You"),
    new item("~/images/main2.jpg", "Chilli Meat Bites", "Nice to Meat You"),
    new item("~/images/main3.jpg", "Your Favourite Ribs", "Nice to Meat You"),
    new item("~/images/main4.jpg", "Burger at the Max", "Burger Queen"),
    new item("~/images/main5.jpg", "Special Burger with Fries", "Burger Queen"),
    new item("~/images/main6.jpg", "Everybody's Dream Hotdog", "Prince Burger"),
    new item("~/images/main7.jpg", "Quinoa Balls", "ReFresh"),
    new item("~/images/main8.jpg", "Bruschetta with Cheese", "Sandwiches and More"),
    new item("~/images/main9.jpg", "Quick Toast with Bacon", "Sandwiches and More"),
    new item("~/images/main10.jpg", "Special Steak with Fries", "Nice to Meat You"),
    new item("~/images/main11.jpg", "Hotdog for Two", "Prince Burger"),
    new item("~/images/main12.jpg", "Bruschetta with Salmon Fish", "Ron's Fishery"),
    new item("~/images/main13.jpg", "Chief's Steak", "Nice to Meat You"),

];




exports.pageLoaded = function(args){
    var page = args.object;
    page.bindingContext = dataobj;

}

exports.onChangeLayoutTap = function(args){
    var actionbtn = args.object;
    var listview_1 = require("nativescript-telerik-ui/listview");
    var radlist = topmost.getViewById("radlistview");
    var GRID_LAYOUT = new listview_1.ListViewGridLayout();
    GRID_LAYOUT.spanCount = 2;
    GRID_LAYOUT.itemHeight = 160;
    var LINEAR_LAYOUT = new listview_1.ListViewLinearLayout();
    console.log(radlist.listViewLayout.spanCount);


    if(actionbtn.icon=="res://ic_listview_layouts_wrap") {
        actionbtn.icon = "res://ic_list_view";
        radlist.listViewLayout = GRID_LAYOUT;

    }else{
        actionbtn.icon ="res://ic_listview_layouts_wrap";
        radlist.listViewLayout = LINEAR_LAYOUT;

    }


}

exports.goBack = function () {
    topmost.navigate("main-page");
}

