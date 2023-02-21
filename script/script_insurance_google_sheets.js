function onOpen(){
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Propensity Score') 
    .addItem('Get Prediction', 'PredictAll')
    .addToUi();
}

host_production = 'cross-sell-health-insurance.onrender.com'

//// Helper Functions ////

/// API Call /////
function ApiCall( data, endpoint){
  var url = 'https://' + host_production + endpoint;
  var payload = JSON.stringify(data); //transoforming string in fomart Json

  var options= {'method': 'POST', 'contentType' : 'application/json', 'payload': payload}; // method and type application
  

  //Logger.log(url)
  //Logger.log(options)
  
  var response = UrlFetchApp.fetch( url, options);

  // get response 
  var rc = response.getResponseCode(); // variable status code
  var responseText = response.getContentText();

  if ( rc !== 200 ){ 
    Logger.log( 'Response (%s) %s', rc, responseText );
  }
  else {
    prediction = JSON.parse( responseText );
  }

  return prediction

};
  

/// Health Insurace Proptensity Score Prediction 
/// This functions is to make list of json
function PredictAll(){
  var ss = SpreadsheetApp.getActiveSheet();
  var titleColumns = ss.getRange('A1:L1').getValues()[0];
  var lastRow = ss.getLastRow();
  var data = ss.getRange('A2' + ':' + 'L'+ lastRow).getValues();
  var spreadsheet = SpreadsheetApp.getActive();
  
  // run over all rows
  for (row in data){
    var json = new Object();
    
    // run over all columns (colecting title and value by row)
    for (var j =0; j < titleColumns.length; j++ ){
      json[titleColumns[j]] = data[row][j];
      Logger.log(lastRow)
      Logger.log(titleColumns)
    };

    //Json file to send
    var json_send = new Object();
    json_send['id'] = json['id']
    json_send['gender'] = json['gender']
    json_send['age'] =  json['age']
    json_send['region_code'] = parseInt(json['region_code'])
    json_send['policy_sales_channel'] = parseInt(json['policy_sales_channel'])
    json_send['driving_license'] = json['driving_license']
    json_send['vehicle_age'] = json['vehicle_age']
    json_send['vehicle_damage'] = json['vehicle_damage']
    json_send['previously_insured'] = json['previously_insured']
    json_send['annual_premium'] = parseInt(json['annual_premium'])
    json_send['vintage'] = json['vintage']

    //json['annual_premium'] = parseInt(json['annual_premium'])
    //json['region_code'] = parseInt(json['region_code'])
    //json['policy_sales_channel'] = parseInt(json['policy_sales_channel'])

    Logger.log( json_send);
    pred = ApiCall( json_send, '/predict' );

    // send back to google sheets
    ss.getRange( Number (row) + 2 , 12).setValue(pred[0]['proba'] )

    //Logger.log( pred )
    
    
  };

  //Orderned the columns with colum L ( prediction )
  //Spreadsheet.getRange('L:L').activate();
  //Spreadsheet.getActiveSheet().sort(12, false);
  spreadsheet.getRange('L:L').activate();
  spreadsheet.getActiveSheet().sort(12, false);

  // Fomart in 2 decimal
  spreadsheet.getActiveRangeList().setNumberFormat('0.00')

};
