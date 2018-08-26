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
      oTable.columns(3).search($(this).val()).draw() ;
    }

  })
})
