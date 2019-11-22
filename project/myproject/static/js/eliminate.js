var country = document.getElementById('address_country')
var province = document.getElementById('address_province')

d.addEventListener('Change',function () {
  var y = new XMLHttpRequest();
  y.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    myFunction(this);
    }
  };
  y.open("GET", "/get_province_for_country?country="+ d.value );
  y.send();
});


function myFunctio(list) {
  province.options.length = 0
  for (var variable in list) {
    province.options[province.options.length + 1] = new Option(variable['province'],variable['key'],false,false)
  }
}
