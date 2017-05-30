var Observable= require("data/observable").Observable;
var L

class BlogPostItemData {
	constructor(title, content, summary, fav, id){
		this.Title= title;
		this.Content = content;
		this.Summary = summary;
		this.IsFavourite = fav;
		this.ID = id;
		this.reorderActive = false;
		this.isSelected = false;
		this.isDeleted = false;
	}
};


allposts = [
        new BlogPostItemData("Master the Essentials of UI Test Automation: Chapter One", "Chapter One: Introduction The goal of this series is to help you understand the right questions to ask of you, your team and your organization. There won't be any Best Practices; there won't be any silver bullets. What we hope is to convey the right information to help you get started on the right foot and get through some of the most common problems teams hit when starting out with UI test automation.", "Chapter One: Introduction The goal of this series is to help you understand the right questions to ask of you, your team and your organization. There won't be any Best Practices; there won't be any silver bullets.", false, 1), 
        new BlogPostItemData("Send Data to Apple Watch with Core Data and Telerik UI for iOS in Swift", "The Apple Watch has been a long rumored device which finally appeared in September, followed by a Watch SDK, called WatchKit, in November. The introduction of the SDK maybe raised more questions than it answered, and we like everybody else are looking into the future for answers from Apple. One such question is: how can I send data, larger than what is allowed for a push notification, from the iPhone to the Watch?", "The Apple Watch has been a long rumored device which finally appeared in September, followed by a Watch SDK, called WatchKit, in November.", true, 2), 
        new BlogPostItemData("6 Key Steps to Successful Agile Testing Projects", "Application teams are continuously adopting agile software techniques as the principal method of building applications. Agile methodologies, such as Scrum, Extreme Programming, Feature-Driven Development and Test-Driven Development offer the ability to iteratively develop applications.", "Application teams are continuously adopting agile software techniques as the principal method of building applications. Agile methodologies, such as Scrum, Extreme Programming, Feature-Driven Development and Test-Driven Development offer the ability to iteratively develop applications.", true, 3), 
        new BlogPostItemData("Increase Your Mobile App Engagement. Become Part of the Web of Apps.", "Mobile developers are facing some severe limitations when it comes to app distribution: app content is almost invisible to browser search, app-to-app connections are scarce, and app updates need to go through a tedious re-submission process on the relevant marketplace. How can Google App Indexing, deep linking and Google Tag Manager for mobile apps help in the process of overcoming these limitations?", "Mobile developers are facing some severe limitations when it comes to app distribution: app content is almost invisible to browser search, app-to-app connections are scarce, and app updates need to go through a tedious re-submission process on the relevant marketplace.", true, 4), 
		new BlogPostItemData("Building a Seismograph App with CoreMotion, Swift and Telerik UI for iOS", "Data visualizations are important, especially on small screen areas, where Excel files or other tables are difficult to read and comprehend. Visualizations are even more important when you add the various sensors that an iPhone device offers, not to mention the different certified third-party devices. Today, I will show you how you can set up the Telerik Chart for iOS to live-stream data coming from the accelerometer sensor using the CoreMotion API.", "Data visualizations are important, especially on small screen areas, where Excel files or other tables are difficult to read and comprehend.", false, 5),
		new BlogPostItemData("Application Performance Monitoring with the Crittercism Cordova Plugin", "As hybrid mobile apps scale to massive amounts of users and tremendous amount of data, developers need to monitor and trace the app’s performance. Crittercism is the world's first mobile application performance management (mAPM) solution, offering both error monitoring and service monitoring solutions. The Crittercism service monitors every aspect of mobile app performance, allowing Developers and IT Operations to deliver high performing, highly reliable, highly available mobile apps.", "As hybrid mobile apps scale to massive amounts of users and tremendous amount of data, developers need to monitor and trace the app’s performance.", false, 6),
];



module.exports = function() {
    var observable = new Observable();
    observable.posts = allposts; 
	
	observable.isReorderActive = false;
	observable.reorderActive = false;
	observable.onActivateReorderTap = function(args){
		observable.set("isReorderActive", true);	
		for(var i in observable.posts){
			observable.posts[i].reorderActive = true;
		}
		observable.set("posts", observable.posts);
	}
/*	
	observable.on(Observable.propertyChangeEvent, function(args) {
		if(args.propertyName == "isReorderActive"){
			observable.set("posts", observable.posts);
		}
	});
*/
	function _show_list(){
		var all_favorite = observable.all_favorite;
		ret = [];
		for(var i in allposts){
			if(allposts[i].isDeleted == false){
				if(all_favorite == allposts[i].IsFavourite && all_favorite == 1){
					ret.push(allposts[i]);
				}
				if(all_favorite == 0 || all_favorite == undefined) {
					return allposts;
				}
			}
		}
		
		return ret;
	}
	var gestures = require("ui/gestures");
	observable.on(Observable.propertyChangeEvent, function(args) {
		if(args.propertyName =="all_favorite"){
			observable.set("posts", _show_list());
		}
	});

    return observable;
};

