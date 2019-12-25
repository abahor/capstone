var country = document.getElementById('country')
var province = document.getElementById('province')

country.addEventListener('change',function () {
  var y = new XMLHttpRequest();
  y.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    console.log(this.response)
    my(this.response);
    }
  };
  y.open("GET", "/get_province_for_country?country="+ country.value );
  y.send();
});


function my(list) {
  // console.log(list);
  // list = list.response
  list = JSON.parse(list)
//  console.log(typeof list);
//  console.log(list['states']);
console.log(list)
  province.options.length = 0
  for (var variable of list) {
    // if (province.options.length == 0 ) {
    // province.options[province.options.length] = new Option(variable,variable,false,false)
    // } else {
    console.log(variable['state']);
      province.options[province.options.length] = new Option(variable['translate'], variable['state'],false,false)
    };
    // province.options[province.options.length + 1] = new Option(variable,variable,false,false)
  }
// }






















var scroller = document.getElementById('sad')
var main = document.getElementById('accordionExample')
var search_button = document.getElementById('search_button')
search_button.addEventListener('click',function () {
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
