
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

    $('.editAgencyButton').click(function(){
        event.preventDefault();

        var $tr = $(this).closest('.agency');
        var index = $tr.find('input[name="index"]').val();
        var agencyname = $tr.find('input[name="agencyname"]').val();
        var website = $tr.find('input[name="website"]').val();
        var location = $tr.find('input[name="location"]').val();
        var description = $tr.find('input[name="description"]').val();
        var agencyString = "#agency_".concat(index);

        var div_data = "<input type='hidden' name='index' value=" + index +"><td class='left aligned'>"+ index +"</td><td class='left aligned'><input class='' type='text' name='agencyname' value="+ agencyname +"></td><td><input class='' type='text' name='website' value="+ website +"></td><td><input class='' type='text' name='location' value="+ location +"></td><td><textarea cols='50' class='' name='description' style='width:100%'>"+ description +"</textarea></td><td><button type='button' class='agencyEditSubmitButton ui button'>Done</button></td>";

        $(agencyString).html(div_data);

        return false;
    });

    $('.agency').on("click", ".agencyEditSubmitButton", function() {
        event.preventDefault();

        var $tr = $(this).closest('.agency');
        var index = $tr.find('input[name="index"]').val();
        var agencyname = $tr.find('input[name="agencyname"]').val();
        var website = $tr.find('input[name="website"]').val();
        var location = $tr.find('input[name="location"]').val();
        var description = $tr.find('textarea[name="description"]').val();
        var agencyString = "#agency_".concat(index);

        data = {
            'index'      : index,
            'agencyname' : agencyname,
            'website'    : website,
            'location'   : location,
            'description': description
        };

        $.ajax({
            type       : 'POST',
            url        : '/editAgency',
            datatype   : "json",
            contentType: "application/json; charset=utf-8",
            data       : JSON.stringify(data)
        }).done(function(data, textStatus, jqXHR){
            window.location.reload();
            //$tr.load()
            console.log('Success!');
        }).fail(function(data) {
            alert('Failed!');
        }).complete(function(data) {
            console.log('completed');
        });
    });

});
