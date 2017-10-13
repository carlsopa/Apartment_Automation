<h3><b>Automated Smart Apartment</b></h3>

<p>I always thought that it would be cool to have a place that knew when I walked through the door and would turn on the lights to greet me, or that when my alarm clock went off would turn on the lights.  So that is where the idea for my smart automated apartment comes from, basically why not.</p>

As the apartment currently stands my network consists of:
<ul>
<li>1 raspberry pi that acts as a central hub that everything connects to</li>
<li>1 alarm clock  built around a raspberry pi</li>
<li>2 relay sensors hooked up to living room and bedroom lamps, these relays are controlled by an Arduino ESP8266 chip.</li>
<li>1 chandelier</li>
<li>1 door sensor that will notify when the door is open and I have the alarm set, as well as turn the lights on when it opens.  This is controlled by an Arduino ESP8266 chip.</li>
</ul>
<p>While it currently is lacking in the full autonamous that I would like to have, all the sensors and relays are connected together.  The controls for the system include a simple webpage that is built using PYTHON FLASK and is hosted on the Raspberry Pi, as well as an android app which was side loaded to my phone.</p>

<p>The next steps for this will be working towards full automation of all my lights, and integration into both Amazon Alexa as well as Google Home.</p>
