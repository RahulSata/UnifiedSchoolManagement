$(function(){
    $("#table_all").on("click", ".js-update-for-all", function () {
        console.log("AAAA");
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-all").modal("show");
            },
            success: function (data) {
              //  $("#table_all").refresh();
                $("#modal-all .modal-content").html(data.html_form);
            }
        });
    });
});


//After the clicking of create Department,.....
$(function(){
    $(".js-add-field").click(function () 
    {
        console.log("Ready to add Department");
        $.ajax({
            url: '/profiler/add_dept/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-all").modal("show");
        },
        success:function(data)
        {
            $("#modal-all .modal-content").html(data.html_form);
        }
    }); 
    });
});



$(function(){
    $("#modal-all").on("submit", ".js-all-update-form", function () {
    console.log("It is just before updationnn");
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data:form.serialize(),
      type:form.attr("method"),
      dataType:'json',
      success:function (data) {
        if (data.form_is_valid) {
          $("#table_all tbody").html(data.html_book_list);
          $("#modal-all").modal("hide");
        }
        else {
          $("#modal-all .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });
});    

// After PopUp form submitted

$("#modal-all").on("submit", ".js-created-form-submit", function () {
            var form = $(this);
            var referrer =  location.href;
            if(referrer == "http://127.0.0.1:8000/profiler/control_panel/add_student/")
            {
            $.ajax({
                url: form.attr("action"),
                data: form.serialize(),
                type: form.attr("method"),
                dataType: 'json',
                success: function (data) {
                if (data.form_is_valid) {
                        $("#cur_db").html(data.html_dropdown_list);
                        $('#modal-all').modal('toggle');
                }
                else {
                    $("modal-all .modal-content").html(data.html_form);
                    }
                }
                });
            }
            else
            {
                $.ajax({
                url: form.attr("action"),
                data: form.serialize(),
                type: form.attr("method"),
                dataType: 'json',
                success: function (data) {
                if (data.form_is_valid) {
                    $("#table_all tbody").html(data.html_table_list);
                    $('#modal-all').modal('toggle');
                }
                else {
                    $("modal-all .modal-content").html(data.html_form);
                    }
                }   
                });
            }    
    return false;
  });



//Add address using dropdownnnnn +

$(function(){
    $(".js-add-address").click(function () 
    {
        console.log("Readyuuuuuu to add Address");
        $.ajax({
            url: '/profiler/add_add/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-all").modal("show");
            },
            success:function(data)
            {
                $("#modal-all .modal-content").html(data.html_form);
            }
    }); 
    });
});


$("#modal-all").on("submit", ".js-created-address-form", function () {
            var form = $(this);
            console.log("Added Just Address");
            var referrer =  location.href;
            console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            console.log(referrer);
            if(referrer == "http://127.0.0.1:8000/profiler/control_panel/add_student/")
            {
            $.ajax({
                url: form.attr("action"),
                data: form.serialize(),
                type: form.attr("method"),
                dataType: 'json',
                success: function (data) {
                    if (data.form_is_valid) {
                        $("#address_db").html(data.html_dropdown_list);
                        $('#modal-all').modal('toggle');
                }
                else {
                    $("modal-all .modal-content").html(data.html_form);
                    }
                }
                });
            }
            else
            {
                console.log("AAAAAAAA");
                $.ajax({
                url: form.attr("action"),
                data: form.serialize(),
                type: form.attr("method"),
                dataType: 'json',
                success: function (data) {
                if (data.form_is_valid) {
                    $("#table_all tbody").html(data.html_table_list);
                    $('#modal-all').modal('toggle');
                }
                else {
                    $("modal-all .modal-content").html(data.html_form);
                    }
                }   
                });
            }
            console.log("BBB");    
    return false;
  });

