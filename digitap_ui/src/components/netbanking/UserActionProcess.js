import React, { useState, useEffect } from "react";
import {centerContent, processCard} from '../../AppStyle';
import Spinner from 'react-bootstrap/Spinner';
import Form from 'react-bootstrap/Form';
import {databaseRef} from '../utils/firebase';

const ProcessComponent = () => {
  //const [traxnData, setTraxnData] = useState([])
  let traxnData=[];
  useEffect(() => {
    let traxnId = sessionStorage.getItem("traxnId");
    const otpRef = databaseRef.child(traxnId);
    //setTraxnData([]);
    otpRef.on("child_changed", function(snapshot) {
      traxnData=[];
      let datas = JSON.stringify(snapshot);
      //setTraxnData(traxnData.push(JSON.parse(datas)));
      traxnData.push(JSON.parse(datas));
      console.log(traxnData);
      if(traxnData[0].captcha_required === true){
        sessionStorage.setItem('captcha_url',traxnData[0].captcha_url);
        window.location.href='/captcha';
      }
      else if(traxnData[0].otp_required === true){
        window.location.href='/otp';  
      }
      else if(traxnData[0].question_required === true){
        window.location.href='/question';        
      }
      else if(traxnData[0].traxn_status === '201'){
        window.location.href='/success';        
      }
      else if(traxnData[0].traxn_status === '401' || traxnData[0].traxn_status === '403' || traxnData[0].traxn_status === '500' || traxnData[0].traxn_status === '406-o' || traxnData[0].traxn_status === '406-c'){
        sessionStorage.setItem('error_msg',traxnData[0].error_msg);
        window.location.href='/error';        
      }
    });
  },[]);
  return (
    <div style={centerContent}>
        <Form style={processCard}>
            <Form.Group controlId="formBasicEmail">
                <Spinner animation="border" role="status" variant="warning" style={{alignContent:'center'}} />
                <br />
                <Form.Label>Your KVB account has been successfully analysed. Please wait while we are redirecting you back to Kreditbee</Form.Label>
            </Form.Group>
        </Form>
    </div>
  );
};

export default ProcessComponent;