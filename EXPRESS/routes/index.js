var express = require('express');
var router = express.Router();
var Client = require('node-rest-client').Client;
var client = new Client();



router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/lastMonth', function(req, res, next) {
  var r;
  var customer_id = req.body.customer_id;

  var now = new Date();
  var day = now.getDate();
  var month = now.getMonth();
  var year = now.getFullYear().toString();
  if(day<10){
    day="0"+day.toString();
  }
  else{
    day=day.toString();
  }
  if(month<9){
    var final_date=year+"-0"+(month+1).toString()+"-"+day;
    var init_date=year+"-0"+(month).toString()+"-"+day;
  }
  else if(month==9){
    var final_date=year+"-"+(month+1).toString()+"-"+day;
    var init_date=year+"-0"+(month).toString()+"-"+day;
  }
  else{
    var final_date=year+"-"+(month+1).toString()+"-"+day;
    var init_date=year+"-"+(month).toString()+"-"+day;
  }
  var argsPost= {
             data: { "init_date": init_date , "final_date": final_date, "customer_id" : customer_id.toString() },
             headers: { "Content-Type": "application/json" }
             };
  client.post("https://python-exam-hectordavid1228.c9users.io:8082/orderList", argsPost , function (data, response) {
    r = data.result;
    res.render('lastMonth', { title: 'Express' , orderList : r, client : customer_id});
    
  });

});

module.exports = router;
