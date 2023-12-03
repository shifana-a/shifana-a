
   var departmenObject = {
  "Btech": ["cse", "eee", "civil"],
  "Commerce": ["Bcom", "Mcom", "CA"],
  "Arts": ["Drawing", "Singing", "Dancing"],
};

window.onload = function() {
  var departmentSel = document.getElementById("department");
  var coursesSel = document.getElementById("courses");

  for (var x in departmenObject) {
    departmentSel.options[departmentSel.options.length] = new Option(x, x);
  }

  departmentSel.onchange = function() {
    //empty Courses dropdown
    coursesSel.length = 1;

    //display correct values
    for (var y of departmenObject[this.value]) {
      coursesSel.options[coursesSel.options.length] = new Option(y, y);
    }
  };
};
