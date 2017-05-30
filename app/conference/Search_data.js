var Observable= require("data/observable").Observable;
class Date {
    constructor(year,month, day, hour, min)
    {
        this.year = year;
        this.month = month;
        this.day = day;
        this.hour = hour;
        this.min = min;
    }
    getTime(){
        return this.hour+":"+this.min;
    };
};


class Session {
    constructor (title, start, end ,room, isFavourite) {
        this.title = title;
        this._start = start;
        this._end = end;
        this.start = this._start.getTime();
        this.end = this._end.getTime();
        this.room = room;
        this.isFavourite = isFavourite;
        this.selectedDay = start.day;
    };
};

allsessions = [
    // Day 1
    new Session("NativeScript Deep Dive 1", new Date(2015, 5, 3, 9, 30), new Date(2015, 5, 3, 12, 30), "room 1", true),
    new Session("Smart Design for Smartphones", new Date(2015, 5, 3, 9, 30), new Date(2015, 5, 3, 12, 30), "room 2", false),
    new Session("Build, Deploy, and Scale your Mobile Backend with Node.js and Modulus", new Date(2015, 5, 3, 9, 30), new Date(2015, 5, 3, 12, 30), "room 3", false),
    new Session("NativeScript Deep Dive 2", new Date(2015, 5, 3, 13, 30), new Date(2015, 5, 3, 16, 30), "room 1", true),
    new Session("Smart Design for Smartphones", new Date(2015, 5, 3, 13, 30), new Date(2015, 5, 3, 16, 30), "room 2", false),
    new Session("Responsive Apps with Telerik DevCraft", new Date(2015, 5, 3, 13, 30), new Date(2015, 5, 3, 16, 30), "room 3", false),
    // Day 2
    new Session("Telerik Keynote - Mobilizing and Modernizing", new Date(2015, 5, 4, 9, 30), new Date(2015, 5, 4, 12, 30), "room 1", true),
    new Session("A Lap Around NativeScript", new Date(2015, 5, 4, 10, 45), new Date(2015, 5, 4, 11, 30), "room 1", true),
    new Session("Kendo UI Building Blocks", new Date(2015, 5, 4, 10, 45), new Date(2015, 5, 4, 11, 30), "room 2", false),
    new Session("AngularJS 2.0", new Date(2015, 5, 4, 11, 45), new Date(2015, 5, 4, 12, 30), "room 1", true),
    new Session("Getting Started with ScreenBuilder", new Date(2015, 5, 4, 11, 45), new Date(2015, 5, 4, 12, 30), "room 2", false),
    new Session("NativeScript Extensibility", new Date(2015, 5, 4, 13, 30), new Date(2015, 5, 4, 14, 15), "room 1", true),
    new Session("AngularJS and Kendo UI ", new Date(2015, 5, 4, 13, 30), new Date(2015, 5, 4, 14, 15), "room 2", false),
    new Session("Building a CRM Portal in 45 Minutes", new Date(2015, 5, 4, 14, 30), new Date(2015, 5, 4, 15, 15), "room 1", false),
    new Session("JavaScript Beyond the Basics", new Date(2015, 5, 4, 14, 30), new Date(2015, 5, 4, 15, 15), "room 2", true),
    // Day 3
    new Session("Sitefinity Keynote", new Date(2015, 5, 5, 9, 30), new Date(2015, 5, 5, 12, 30), "room 1", true),
    new Session("Introduction to Mobile Testing & Device Cloud", new Date(2015, 5, 5, 10, 45), new Date(2015, 5, 5, 11, 30), "room 1", true),
    new Session("Using Kendo UI in SharePoint/Office 365", new Date(2015, 5, 5, 10, 45), new Date(2015, 5, 5, 11, 30), "room 2", false),
    new Session("Improving Applications with Telerik Analytics", new Date(2015, 5, 5, 11, 45), new Date(2015, 5, 5, 12, 30), "room 1", true),
    new Session("Building Offline Ready Mobile Apps", new Date(2015, 5, 5, 11, 45), new Date(2015, 5, 5, 12, 30), "room 2", false),
    new Session("Debugging with Fiddler", new Date(2015, 5, 5, 13, 30), new Date(2015, 5, 5, 14, 15), "room 1", true),
    new Session("Performance Tuning Your Mobile Web Apps", new Date(2015, 5, 5, 13, 30), new Date(2015, 5, 5, 14, 15), "room 2", false),
    new Session("Cross platform Telerik Native Mobile UI", new Date(2015, 5, 5, 14, 30), new Date(2015, 5, 5, 15, 15), "room 1", false),
    new Session("Advanced Kendo UI", new Date(2015, 5, 5, 14, 30), new Date(2015, 5, 5, 15, 15), "room 2", true),
];


module.exports = function() {
    var observable = new Observable();
    observable.sessions = allsessions; 
    observable.items    = _refilter();
    observable.search   = "";
	observable.selectedDay = 0;

    function _refilter() {
        var items = allsessions;
        var filter = observable.search;
		var selectedDay = observable.selectedDay==NaN? 0: observable.selectedDay;
        var ret = [];
        if(filter =='' || filter==undefined){
			for(var i in items){
				if(items[i]._start.day == selectedDay+3){
					ret.push(items[i]);
				}
			}
			return ret;
		}
        
		for(var i in items){
            if(items[i].title.toLowerCase().includes(filter.toLowerCase()) && items[i]._start.day == selectedDay+3){
                ret.push(items[i]);
            }
        }
        return ret;
    }

    observable.on(Observable.propertyChangeEvent, function(args) {
        if (args.propertyName == "search" || args.propertyName == "selectedDay") {
			observable.set("sessions", _refilter());
		}
    });
    return observable;
};
