jQuery(document).ready(function() {
    var SideNav = $('.side-nav'),
        NavTrigger = $('.nav-trigger'),
        Content = $('.content'),
        MainContent = $('.main-content');
    var ApartmentAlarm = $('#Alarm'),
        Chandelier = $('#Chandelier'),
        BedLights = $('#BedroomLights'),
        AlarmClock = $('#AlarmClock');

    NavTrigger.on('click', function(event) {
        event.preventDefault();
        //alert("click works");
        $([SideNav, NavTrigger]).toggleClass('nav-visible');
    });
    ApartmentAlarm.on('click', function() {
        //event.preventDefault();
        Content.load('ApartmentAlarm');
        $([SideNav, NavTrigger]).toggleClass('nav-visible');
    });
    Chandelier.on('click', function() {
        //event.preventDefault();
        Content.load('/Chandelier');
        $([SideNav, NavTrigger]).toggleClass('nav-visible');
    });
    BedLights.on('click', function() {
        //event.preventDefault();
        Content.load('/bedroomlight');
        $([SideNav, NavTrigger]).toggleClass('nav-visible');
    });
    AlarmClock.on('click', function() {
        //event.preventDefault();
        Content.load('/alarmclock');
        $([SideNav, NavTrigger]).toggleClass('nav-visible');
    });
    console.log("hello michelle")
    //$('.ui-flipswitch').click(function(){console.log($(this).hasClass('ui-flipswitch-active')? 'On' : 'Off')})
});
