function reloadTabs(nameVal){
  //console.log("HELLO! " + nameVal.type + " " + nameVal.msg);
  if(nameVal.type == 'Rent'){
    loadRent();
  }
  else if(nameVal.type == 'Maint'){
    loadMaint();
  }
  else if(nameVal.type == 'Bills'){
    loadBills();
  }
  else if(nameVal.type == 'Taxes'){
    loadTaxes();
  }
  else if(nameVal.type == 'Entry'){
    loadEntry(nameVal.msg);
    //console.log("MADE IT TO loadEntry")
  }
  else{
    //ignore
  }
}
function loadRent(){
  setTabs("Rent");
  setLinks(["Current Rent Status","Year To Date Rent Status","Custom Rent Status"]);
}
function loadMaint(){
  setTabs("Maint");
  setLinks(["Most Recent Month Maintenance", "Year To Date Maintenance", "Custom Maintenance"]);
}
function loadBills(){
  setTabs("Bills");	
  setLinks([]);
}
function loadTaxes(){
  setTabs("Taxes");	
  setLinks([]);
}
function loadEntry(msg){
  if(!msg){
    msg = " ";
  }
  setTabs("Entry");	
  setDownload(msg);
}
function setTabs(uniqueTab){
	var tabs = document.getElementsByClassName("uiTab");
	var i;
	for(i=0; i < tabs.length; i++){
	  tabs[i].style.backgroundColor = "green";
	  tabs[i].style.color = "black";
	}
	var tab = document.getElementById("menuTabs" + uniqueTab);
    tab.style.backgroundColor = "black";
    tab.style.color = "white";
}

function setLinks(links){
	var index;
	var htmlText = "<ul id='tabFunctions'>";
	for(index=0;index<links.length;index++){
		linksFunction = links[index].replace(/\s+/gm,'');
		htmlText += "<li><a onclick = '" + linksFunction +"()'>"
		          + links[index] + "</a></li>"
    }
    document.getElementById("linkTextArea").innerHTML = htmlText;
}

function setDownload(msg){
  console.log("MSG: " + msg);
  htmlText = "<h3>Choose File For Upload</h3>"
           + "<form action='' method='post' enctype='multipart/form-data'>"
           + "<input type='file' name='file'><br />"
           + "<select name='month' class = 'selectClass' id = 'selectMonth'>"
           + "     <option value='JAN'>JAN</option>"
           + "     <option value='FEB'>FEB</option>"
           + "     <option value='MAR'>MAR</option>"
           + "     <option value='APR'>APR</option>"
           + "     <option value='MAY'>MAY</option>"
           + "     <option value='JUN'>JUN</option>"
           + "     <option value='JUL'>JUL</option>"
           + "     <option value='AUG'>AUG</option>"
           + "     <option value='SEP'>SEP</option>"
           + "     <option value='OCT'>OCT</option>"
           + "     <option value='NOV'>NOV</option>"
           + "     <option value='DEC'>DEC</option>"
           + "   </select>"
           + "<select name='year' class = 'selectClass' id = 'selectYear'>"
           + "     <option value='2015'>2015</option>"
           + "     <option value='2014'>2014</option>"
           + "     <option value='2013'>2013</option>"
           + "     <option value='2012'>2012</option>"
           + "     <option value='2011'>2011</option>"
           + "     <option value='2010'>2010</option>"
           + "     <option value='2009'>2009</option>"
           + "     <option value='2008'>2008</option>"
           + "     <option value='2007'>2007</option>"
           + "     <option value='2006'>2006</option>"
           + "     <option value='2005'>2005</option>"
           + "     <option value='2004'>2004</option>"
           + "   </select><br />"
           + "<input type='submit' value='Upload'></form>"
           + "<br />" + msg + "<br />";
  //console.log(htmlText + "\n That is the HTML \n");
  document.getElementById("linkTextArea").innerHTML = htmlText;
}

function CurrentRentStatus(){}
function YearToDateRentStatus(){}
function CustomRentStatus(){}
function MostRecentMonthMaintenance(){}
function YearToDateMaintenance(){}
function CustomMaintenance(){}

function getCharts(){
  document.getElementById('d3ChartsID').innerHTML = "CHARTS";
}
function getComments(){
  document.getElementById('commentsID').innerHTML = "COMMENTS";
}
function getFooter(){
  document.getElementById('footer').innerHTML = "RJL1 LLC 2004-2015";
}
