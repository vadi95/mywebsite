 $(window).on("load", function () {
            $('#intro-wrap').hide();
            $('#intro-wrap').fadeIn(2000, function () {
                // First Animation complete
                setTimeout(function(){$('#intro-wrap').fadeOut(2000, function () {
                    // Second Animation complete
                });
                },2000);// Wait for 2 Seconds
            });
         });