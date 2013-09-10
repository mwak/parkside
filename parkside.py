import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return html


html = """
<html>
<head>
   <title>Parkside, Brooklyn</title>
   
   <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
		
   <style>
   html, body, #map {
      height:100%;
      width:100%;
      padding:0px;
      margin:0px;
   } 
   </style>
   
   <link rel="stylesheet" href="static/leaflet.css" />
   <!--[if lte IE 8]><link rel="stylesheet" href="static/leaflet.ie.css" /><![endif]-->
   
   <script src="static/leaflet.js"></script>
   
   <script language="javascript">
      function init() {
         var map = new L.Map('map');                       
              
      	 L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
            maxZoom: 18
         }).addTo(map);
         map.attributionControl.setPrefix(''); // Don't show the 'Powered by Leaflet' text.

         var parkside = new L.LatLng(40.65602, -73.96197); 
         map.setView(parkside, 15);
      }
   </script>
   
</head>
<body onLoad="javascript:init();">
   <div id="map"></div>
   <div id="explanation">Go fullscreen by size the div in CSS. You must also size
   the html and body elements, setting each of them to 100% width and height
   </div>
</body>                                                                                                                          
</html>

"""