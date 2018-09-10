$("#home").css("min-height", screen.height-270)
$(document).ready(function() {

  var oTable = $('#myTable').DataTable(
    {"dom": 'lrtip'}
  );   //pay attention to capital D, which is mandatory to retrieve "api" datatables' object, as @Lionel said
  $('#myInputTextField').keyup(function(){
    column = $('#inputGroupSelect01').val()
    if(column=='0'){
      oTable.search($(this).val()).draw() ; //all
    }
    else if(column=='1'){
      oTable.columns(0).search($(this).val()).draw() ;//handle col 0
    }
    else if(column=='2'){
      oTable.columns(1).search($(this).val()).draw() ;//name col 1
    }
    else if(column=='3'){
      oTable.columns(2).search($(this).val()).draw() ;//email col2
    }
    else if(column=='4'){
      oTable.columns(3).search($(this).val()).draw() ;//twitch
    }
    else if(column=='5'){
      oTable.columns(4).search($(this).val()).draw() ;//twitter
    }
    else if(column=='6'){
      oTable.columns(5).search($(this).val()).draw() ;//country
    }
    else if(column=='7'){
      oTable.columns(6).search($(this).val()).draw() ;//shirt
    }
    else if(column=='8'){
      oTable.columns(8).search($(this).val()).draw() ;//update
    }
    else if(column=='9'){
      oTable.columns(9).search($(this).val()).draw() ;//mailing_address
    }
    else if(column=='10'){
      oTable.columns(10).search($(this).val()).draw() ;//phone
    }
    else if(column=='11'){
      oTable.columns(11).search($(this).val()).draw() ;//youtube
    }
    else if(column=='12'){
      oTable.columns(12).search($(this).val()).draw() ;//mixer
    }
    else if(column=='13'){
      oTable.columns(13).search($(this).val()).draw() ;//tags
    }
    else if(column=='14'){
      oTable.columns(14).search($(this).val()).draw() ;//events
    }
    else if(column=='15'){
      oTable.columns(15).search($(this).val()).draw() ;//lists
    }

  })
  $('#inputGroupSelect01').change(function(){
    oTable.search('').draw() ;
    column = $('#inputGroupSelect01').val()
    if(column=='0'){
      oTable.search($('#myInputTextField').val()).draw() ; //all
    }
    else if(column=='1'){
      oTable.columns(0).search($('#myInputTextField').val()).draw() ;//handle col 0
    }
    else if(column=='2'){
      oTable.columns(1).search($('#myInputTextField').val()).draw() ;//name col 1
    }
    else if(column=='3'){
      oTable.columns(2).search($('#myInputTextField').val()).draw() ;//email col2
    }
    else if(column=='4'){
      oTable.columns(3).search($('#myInputTextField').val()).draw() ;//twitch
    }
    else if(column=='5'){
      oTable.columns(4).search($('#myInputTextField').val()).draw() ;//twitter
    }
    else if(column=='6'){
      oTable.columns(5).search($('#myInputTextField').val()).draw() ;//country
    }
    else if(column=='7'){
      oTable.columns(6).search($('#myInputTextField').val()).draw() ;//shirt
    }
    else if(column=='8'){
      oTable.columns(8).search($('#myInputTextField').val()).draw() ;//update
    }
    else if(column=='9'){
      oTable.columns(9).search($('#myInputTextField').val()).draw() ;//mailing_address
    }
    else if(column=='10'){
      oTable.columns(10).search($('#myInputTextField').val()).draw() ;//phone
    }
    else if(column=='11'){
      oTable.columns(11).search($('#myInputTextField').val()).draw() ;//youtube
    }
    else if(column=='12'){
      oTable.columns(12).search($('#myInputTextField').val()).draw() ;//mixer
    }
    else if(column=='13'){
      oTable.columns(13).search($('#myInputTextField').val()).draw() ;//tags
    }
    else if(column=='14'){
      oTable.columns(14).search($('#myInputTextField').val()).draw() ;//events
    }
    else if(column=='15'){
      oTable.columns(15).search($('#myInputTextField').val()).draw() ;//lists
    }
  })

})
function tags_filter(){
  var item;
  var input = document.getElementById('search-tags');
  var filter = input.value.toUpperCase();
  var list_items = document.getElementById("id_tags").childNodes
  for(var i=1; i<list_items.length; i+=2){
    item = list_items[i];
    if(item.textContent.toUpperCase().indexOf(filter) == -1){
      list_items[i].style.display = "none";
    }
    else{
      list_items[i].style.display = '';
    }
  }
}
function events_filter(){
  var item;
  var input = document.getElementById('search-events');
  var filter = input.value.toUpperCase();
  var list_items = document.getElementById("id_events").childNodes
  for(var i=1; i<list_items.length; i+=2){
    item = list_items[i];
    if(item.textContent.toUpperCase().indexOf(filter) == -1){
      list_items[i].style.display = "none";
    }
    else{
      list_items[i].style.display = '';
    }
  }
}
if ( $( "#id_tags" ).length ) {
    $( "#id_tags" ).before("<input type='text' id='search-tags' onkeyup='tags_filter()' placeholder='Search for Tags'></input>");
}
if ( $( "#id_events" ).length ) {
    $( "#id_events" ).before("<input type='text' id='search-events' onkeyup='events_filter()' placeholder='Search for Events'></input>");
}
