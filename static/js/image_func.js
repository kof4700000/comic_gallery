  $(document).ready(function(){
    var base_url = window.location.href + "1"
    $.get(base_url, function(data){
      src = "/static/" + data
      $("#image").attr('src', src)
    })
    var max_page = $("#max_page").text()
    for (var i=2;i<=max_page;i++){
      $("#page_select").append("<option value='" + i + "'>" + i + "</option>");
    }
  })
  function next_page(){
    //page_num = parseInt($("#current_page").text())
    page_num = Number($("#current_page").text())
    next_page_num = page_num + 1
    if (Number($("#max_page").text()) < next_page_num){
      alert("max_page!")
      return
    }
    var next_page_url = window.location.href + next_page_num
    $.get(next_page_url, function(data){
      src = "/static/" + data
      $("#image").attr('src', src)
    })
    $("#current_page").text(next_page_num)
    $("#page_select").val(next_page_num)
  }
  function pre_page(){
    page_num = Number($("#current_page").text())
    next_page_num = page_num - 1
    if (1 > next_page_num){
      alert("min_page!")
      return
    }
    var next_page_url = window.location.href + next_page_num
    $.get(next_page_url, function(data){
      src = "/static/" + data
      $("#image").attr('src', src)
    })
    $("#current_page").text(next_page_num)
    $("#page_select").val(next_page_num)
  }
  function select_page(){
    next_page_num = Number($("#page_select").val())
    var next_page_url = window.location.href + next_page_num
    $.get(next_page_url, function(data){
      src = "/static/" + data
      $("#image").attr('src', src)
    })
    $("#current_page").text(next_page_num)
    $("#page_select").val(next_page_num)
  }
