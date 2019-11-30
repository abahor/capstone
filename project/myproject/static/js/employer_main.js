function keep(id){
        var xh = new XMLHttpRequest();
        xh.onreadystatechange = function() {
          if (this.status == 200 && this.readyState == 4 ){
            console.log('sad');
              $('#'+id+'_keep').remove()

          }
        }
        xh.open('POST','/keep_job?job_id='+ id )
        xh.send()
}
function delete_post(id) {
    var xh = new XMLHttpRequest();
    xh.onreadystatechange = function(){
    var o = document.getElementById(id);
    $('#'+id).remove()

}
    xh.open('POST','/delete_this_job?job_id='+id)
    xh.send()
}
