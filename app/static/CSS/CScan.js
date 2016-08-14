
$(function () {

  $('.deleteAgencyButton').click(function() {
      event.preventDefault();
      var $tr = $(this).closest('tr')
      var index = $tr.find('input[name="index"]').val();
      data = {
          'index'  : index,
      }

      $.ajax({
          type: 'POST',
          url: '/deleteAgency',
          datatype : "json",
          contentType: "application/json; charset=utf-8",
          data : JSON.stringify(data)
      }).done(function(data, textStatus, jqXHR){
          $tr.remove();
          console.log('Success!');
      }).fail(function(data) {
          alert('Failed!');
      }).complete(function(data) {
          console.log('completed');
      });
    });

});
