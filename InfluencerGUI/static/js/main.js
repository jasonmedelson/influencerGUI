$("#home").css("min-height", screen.height-270)
$(document).ready(function() {

  var oTable = $('#myTable').DataTable(
    {"dom": 'lrtip'}
  );   //pay attention to capital D, which is mandatory to retrieve "api" datatables' object, as @Lionel said
  $('#myInputTextField').keyup(function(){
    column = $('#inputGroupSelect01').val()
    if(column=='0'){
      oTable.search($(this).val()).draw() ;
    }
    else if(column=='1'){
      oTable.columns(0).search($(this).val()).draw() ;
    }
    else if(column=='2'){
      oTable.columns(1).search($(this).val()).draw() ;
    }
    else if(column=='3'){
      oTable.columns(2).search($(this).val()).draw() ;
    }
    else if(column=='4'){
      oTable.columns(3).search($(this).val()).draw() ;
    }
    else if(column=='5'){
      oTable.columns(4).search($(this).val()).draw() ;
    }
    else if(column=='6'){
      oTable.columns(5).search($(this).val()).draw() ;
    }
    else if(column=='7'){
      oTable.columns(7).search($(this).val()).draw() ;
    }
    else if(column=='8'){
      oTable.columns(8).search($(this).val()).draw() ;
    }
    else if(column=='9'){
      oTable.columns(9).search($(this).val()).draw() ;
    }
    else if(column=='10'){
      oTable.columns(10).search($(this).val()).draw() ;
    }
    else if(column=='11'){
      oTable.columns(11).search($(this).val()).draw() ;
    }
    else if(column=='12'){
      oTable.columns(12).search($(this).val()).draw() ;
    }

  })
  $('#inputGroupSelect01').change(function(){
    oTable.search('').draw() ;
    column = $('#inputGroupSelect01').val()
    if(column=='0'){
      oTable.search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='1'){
      oTable.columns(0).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='2'){
      oTable.columns(1).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='3'){
      oTable.columns(2).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='4'){
      oTable.columns(3).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='5'){
      oTable.columns(4).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='6'){
      oTable.columns(5).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='7'){
      oTable.columns(7).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='8'){
      oTable.columns(8).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='9'){
      oTable.columns(9).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='10'){
      oTable.columns(10).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='11'){
      oTable.columns(11).search($('#myInputTextField').val()).draw() ;
    }
    else if(column=='12'){
      oTable.columns(12).search($('#myInputTextField').val()).draw() ;
    }

  })

})
