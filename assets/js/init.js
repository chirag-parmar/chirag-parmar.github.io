$(document).ready(function() {
    "use strict";

    /***************************************************************************/
            /* NAVIGATION  */
    /***************************************************************************/
    $('.sidenav').sidenav();
 
    /**************************************************************************
                 SKILL BAR 
    **************************************************************************/

    $(".determinate").each(function(){
      var width = $(this).text();
      $(this).css("width", width)
        .empty()
        .append('<i class="fa fa-circle"></i>');                
    });


    /**************************************************************************
            Style demo
    **************************************************************************/
   
    $('.cv-style-switch').click(function(){
        if($(this).hasClass('open')){
          $(this).removeClass('open');
          $('#switch-style').animate({'right':'0'});
        }else{
          $(this).addClass('open');
          $('#switch-style').animate({'right':'-300'});
        }
    });

  
    /**************************************************************************
             BLOG POST 
    **************************************************************************/
    function dynamicallyLoadScript(url) {
        var script = document.createElement("script"); //Make a script DOM node
        script.src = url; //Set it's src to the provided URL
        document.head.appendChild(script); //Add it to the end of the head section of the page (could change 'head' to 'body' to add it to the end of the body section instead)
    }

    function resetHeight(){
        var div_particle = document.getElementById("particles-js")
        var assign_height = 0

        if (document.body.clientHeight > window.innerHeight){
            assign_height = document.body.clientHeight
        }
        else{
            assign_height = window.innerHeight
        }
        div_particle.style.height = assign_height.toString() + "px"
        
        console.log("height resetted")
    }

    var $masonry = $('.gallery-section');
    $masonry.masonry({
        itemSelector: '.gallery-item',
        columnWidth: '.gallery-item',
    });
    $masonry.imagesLoaded(function() {
        $masonry.masonry('layout');
        resetHeight()
        dynamicallyLoadScript("assets/js/particles.js")
        dynamicallyLoadScript("assets/js/app.js")
    });

    var $masonry2 = $('.bloggy-section');
    $masonry2.masonry({
        itemSelector: '.blog-post',
        columnWidth: '.blog-post',
    });
    $masonry2.imagesLoaded(function() {
        $masonry2.masonry('layout');
        resetHeight()
        dynamicallyLoadScript("assets/js/particles.js")
        dynamicallyLoadScript("assets/js/app.js")
    });

    var $masonry3 = $('.projjy-section');
    $masonry3.masonry({
        itemSelector: '.blog-post',
        columnWidth: '.blog-post',
    });
    $masonry3.imagesLoaded(function() {
        $masonry3.masonry('layout');
        resetHeight()
        dynamicallyLoadScript("assets/js/particles.js")
        dynamicallyLoadScript("assets/js/app.js")
    });


    var height = $('.caption').height();
        if($(window).width()){
          $('#featured').css('height', height);   
          $('#featured img').css('height', height);   
        }


    /*************************************************************************
                TOOLTIP
    **************************************************************************/
    $('.tooltipped').tooltip({delay: 50});

    /**************************************************************************
        WOW INIT
    **************************************************************************/

    var wow = new WOW({ mobile: false });
    wow.init();

    /***************************************************************************
          CONTACT FORM
    ***************************************************************************/

    $("#contactForm").validator().on("submit", function (event) {
        if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formError();
            submitMSG(false, "Did you fill in the form properly?");
        } else {
            // everything looks good!
            event.preventDefault();
            submitForm();
        }
    });
    function submitForm(){
    // Initiate Variables With Form Content
        var name = $("#name").val();
        var email = $("#email").val();
        var message = $("#message").val();
        
        $.ajax({
            type: "POST",
            url: "process.php",
            data: "name=" + name + "&email=" + email + "&message=" + message,
            success : function(text){
                if (text == "success"){
                    formSuccess();
                } else {
                    formError();
                    submitMSG(false,text);
                }
            }
        });
    }
    function formSuccess(){
        $("#contactForm")[0].reset();
        submitMSG(true, "Message Sent!")
    }
    function formError(){
        $("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', 
        function(){
            $(this).removeClass();
        });
    }
    function submitMSG(valid, msg){
        if(valid){
            var msgClasses = "h3 text-center fadeInUp animated text-success";
        } else {
            var msgClasses = "h3 text-center text-danger";
        }
        $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
    }
    
    
    /**************************************************************************
       Projects
    **************************************************************************/
    
    $('.sa-view-project-detail').on('click', function(event) {
        event.preventDefault();
        var href          = $(this).attr('href') + ' ' + $(this).attr('data-action'),
            dataShow      = $('#project-gallery-view'),
            dataShowMeta  = $('#project-gallery-view meta'),
            dataHide      = $('#portfolio-item'),
            preLoader     = $('#loader'),
            backBtn       = $('#back-button'),
            filterBtn     = $('#filter-button');
        console.log(href)
        dataHide.animate( { 'marginLeft':'-120%' }, { duration: 400, queue: false } );
        filterBtn.animate( { 'marginLeft':'-120%' }, { duration: 400, queue: false } );
        dataHide.fadeOut(400);
        filterBtn.fadeOut(400);
        setTimeout( function() { preLoader.show(); }, 400);
        setTimeout( function() {
            dataShow.load( href, function() {
                dataShowMeta.remove();
                preLoader.hide();
                dataShow.fadeIn(600);
                backBtn.fadeIn(600);
            });
        },800);
    });

    $('#back-button').on('click', function(event) {
        event.preventDefault();
        var dataShow    = $('#portfolio-item'),
            dataHide    = $('#project-gallery-view'),
            filterBtn   = $('#filter-button');

        $("[data-animate]").each( function() {
            $(this).addClass($(this).attr('data-animate'));
        });

        dataHide.fadeOut(400);
        $(this).fadeOut(400);
        setTimeout(function(){
            dataShow.animate( { 'marginLeft': '0' }, { duration: 400, queue: false } );
            filterBtn.animate( { 'marginLeft': '0' }, { duration: 400, queue: false } );
            dataShow.fadeIn(400);
            filterBtn.fadeIn(400);
        },400);
        setTimeout(function(){
            dataShow.find('.fadeInRight, .fadeInLeft, .fadeInUp, .fadeInDown').removeClass('fadeInRight').removeClass('fadeInLeft').removeClass('fadeInUp').removeClass('fadeInDown');
        },1500);
    });

});

    /***************************************************************************
                MAP
    ***************************************************************************/

