var country = document.getElementById('country')
var province = document.getElementById('province')

country.addEventListener('change',function () {
  var y = new XMLHttpRequest();
  y.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    myFunction(this);
    }
  };
  y.open("GET", "/get_province_for_country?country="+ country.value );
  y.send();
});


function myFunction(list) {
  // console.log(list);
  // list = list.response
  list = JSON.parse(list.response)
  console.log(typeof list);
  console.log(list['states']);
  province.options.length = 0
  for (var variable in list['states']) {
    // if (province.options.length == 0 ) {
    // province.options[province.options.length] = new Option(variable,variable,false,false)
    // } else {
    console.log(list['states'][variable]);
      province.options[province.options.length] = new Option(list['states'][variable],list['states'][variable],false,false)
    };
    // province.options[province.options.length + 1] = new Option(variable,variable,false,false)
  }
// }
