$(document).ready(function(){


  //Only run the following on member display page
  var url = "/test-good";

//Only apply to index.html
//Uses body class
  if ($('.page-index').length > 0)
    {
      // alert('Inside of Index.');
      //Set the focus to the input
      //so that memeber can just walk up and swipe
      $('#member_id').val('').focus();

    }

//Only apply to member.html
//Uses body class
  if ($('.page-member-details').length > 0)
    {
      // alert('Inside of member page.');
      //Allows page to be displayed for a given length of time
      setTimeout(function () {
        //change page to index
        window.location.replace('/');
      }, 15000); // this number is in milliseconds

    }

    //Only apply to member-not-found.html
    //Uses body class
      if ($('.page-member-not-found').length > 0)
        {

          //Allows page to be dispalyed for a given length of time
          setTimeout(function () {
            //change page to index
            window.location.replace('/');
          }, 4000); // this number is in milliseconds


        }

//   alert(top.location.pathname)
//   if (top.location.pathname === '/test-good')
// {
//     /* magic ... */
//     alert('hello')
// }

  // $(location).attr('href',url);

//   $("#ref_in_five").click(function(){setTimeout(function() {
// location.reload()
//  },5000);
//    });

});
