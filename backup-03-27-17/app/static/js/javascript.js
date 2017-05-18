$(document).ready(function(){

$(document).foundation();
  //Only run the following on member display page
  var url = "/test-good";

//Only apply to index.html
//Uses body class
  if ($('.page-index').length > 0)
    {
      //Set the focus to the input
      //so that memeber can just walk up and swipe
      $('#member_id').val('').focus();

    }

//Only apply to member.html
//Uses body class
  if ($('.page-member-details-disable').length > 0)
    {
      //Allows page to be displayed for a given length of time
      setTimeout(function () {
        //change page to index
        window.location.replace('/');
      }, 10000); // this number is in milliseconds

    }

    //Only apply to member-not-found.html
    //Uses body class
      if ($('.page-member-not-found-disable').length > 0)
        {

          //Allows page to be dispalyed for a given length of time
          setTimeout(function () {
            //change page to index
            window.location.replace('/');
          }, 4000); // this number is in milliseconds


        }

});
