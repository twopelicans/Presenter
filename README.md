Presenter
=========

Hopefully delivering a Remote controlled presentation solution using
Impress.j as the presentation framework with Python (Flask, Server Sent Events)
for control.
SSEs are implemented in all recent browsers less IE.  for older browsers
you can use pollyfills eg eventsource.js or jquery.eventsource.
SSE was chosen over Web Sockets to KISS as I can use std Http for the presenter 
and slide changes pushed to the clients via SSE.  all in one app and the standard
http ports which for me is key