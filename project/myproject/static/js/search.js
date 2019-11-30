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
//  console.log(typeof list);
//  console.log(list['states']);
  province.options.length = 0
  for (var variable in list['states']) {
    // if (province.options.length == 0 ) {
    // province.options[province.options.length] = new Option(variable,variable,false,false)
    // } else {
    console.log(list['states'][variable]);
      province.options[province.options.length] = new Option(list['states'][variable],list['states'][variable],false,false)
    };
    // province.options[province.options.length + 1] = new Option(variable,variable,false,false)
  };
// }





















var scroller = document.getElementById('sad')
var main = document.getElementById('accordionExample')
province.addEventListener('change',function () {
  var xm = new XMLHttpRequest();
  xm.onreadystatechange = function (){
    if (this.readyState == 4 && this.status == 200) {
    console.log('it works');
    myFunction(this);
    }
    if (this.status == 404) {
      main.innerText = ''
    }
  }
  xm.open('GET','/get_job?city='+ province.value )
  xm.send()
});

function myFunction (data) {
    var ter = JSON.parse(data.response)
    console.log(ter)
    main.innerText = ''
    try {
      for (i of ter) {
              let template_clone = scroller.content.cloneNode(true);
              template_clone.querySelector('.btn-link').innerHTML = i.title
              template_clone.querySelector('.card-body').innerHTML = i.text
              template_clone.querySelector('.link').href = i.link
              main.appendChild(template_clone);
      }
    } catch (e) {
      return main.innerHTML = '';
    }  finally {

    }


}
