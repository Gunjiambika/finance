let output=document.getElementById("output");
let chart;

async function createUser(){
let res=await fetch("/users",{method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({
name:document.getElementById("name").value,
role:document.getElementById("role").value,
active:true
})});
let data=await res.json();
output.innerText=JSON.stringify(data,null,2);
}

async function addRecord(){
let uid=document.getElementById("uid").value;

let res=await fetch(`/records/${uid}`,{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
amount:parseFloat(document.getElementById("amount").value),
type:document.getElementById("type").value,
category:document.getElementById("category").value,
date:"2026-04",
note:"demo"
})
});

let data=await res.json();
output.innerText=JSON.stringify(data,null,2);
}

async function getSummary(){
let uid=document.getElementById("aid").value;
let res=await fetch(`/summary/${uid}`);
let data=await res.json();
output.innerText=JSON.stringify(data,null,2);

drawChart(["Income","Expense"],[data.total_income,data.total_expense],"bar");
}

async function getCategory(){
let uid=document.getElementById("aid").value;
let res=await fetch(`/summary/category/${uid}`);
let data=await res.json();
output.innerText=JSON.stringify(data,null,2);

drawChart(Object.keys(data),Object.values(data),"pie");
}

async function getTrends(){
let uid=document.getElementById("aid").value;
let res=await fetch(`/summary/trends/${uid}`);
let data=await res.json();
output.innerText=JSON.stringify(data,null,2);

drawChart(Object.keys(data),Object.values(data),"line");
}

function drawChart(labels,data,type){
const ctx=document.getElementById("chart").getContext("2d");

if(chart) chart.destroy();

chart=new Chart(ctx,{
type:type,
data:{
labels:labels,
datasets:[{label:"Finance",data:data}]
}
});
}