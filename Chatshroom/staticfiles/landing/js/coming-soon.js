(function($) {
  "use strict"; // Start of use strict

  // Vide - Video Background Settings
  $('body').vide({
    mp4: mp4_location,
    poster: mobile_fallback_location
  }, {
    posterType: 'jpg'
  });

})(jQuery); // End of use strict
