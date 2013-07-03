/*
 
If you want more control over impress.js, the first thing is to change the way you call it. The demo
initializes impress.js like this:
 
<script src="js/impress.js"></script>
<script>impress().init();</script>
 
You want to change this to the following:
 
<script src="js/impress.js"></script>
<script>
var api = impress();
api.init();
</script>
 
The key difference here is that you now have a JavaScript variable called api that you can call
impress's methods on. The full documentation is in impress's index.html, but in short, you now have
api.next(), api.prev(), and api.goto() for moving around the slideshow.
 
For timing the transitions between slides, you can use two functions that are part of JavaScript
itself; no need for jQuery or anything. These functions are setInterval() and setTimeout(). They both
take two arguments: a thing to call, and a delay (in milliseconds) to wait before calling it.
setInterval() will call your thing over and over again; setTimeout() will call it once.
 
 
For instance, if you make the changes above, the simplest thing you can add is an auto-advancing
interval, like so:
 
setInterval(api.next, 5000);
 
That will move to the next slide every 3 seconds.

from the impress.js source code

 `api.init()` - initializes the presentation,
`api.next()` - moves to next step of the presentation,
`api.prev()` - moves to previous step of the presentation,
`api.goto( idx | id | element, [duration] )` - moves the presentation to the step given by its index number
id or the DOM element; second parameter can be used to define duration of the transition in ms,
but it's optional - if not provided default transition duration for the presentation will be used.

*/
