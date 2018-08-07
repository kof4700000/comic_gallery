  function select_gallery_page(){
    next_page_num = Number($("#gallery_page_select").val())
    window.location.href = window.location.pathname + "?page=" + next_page_num
  }
