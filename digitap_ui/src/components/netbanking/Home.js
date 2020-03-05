import React, { useState, useEffect } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import { MdAccountBalance, MdAccountCircle } from "react-icons/md";
import { GiUnlocking } from "react-icons/gi";
import {appHome, primaryButton, errorButton, homeInfo, homeIcon, homeContent, dispContent, hideContent} from '../../AppStyle';
import axios from 'axios';
import {controllerUrl} from '../../Config';
import { VerifyCredential } from "../utils/appUtil";
//import { Col, Row } from "react-bootstrap";

const sessionToken = sessionStorage.getItem('token');
const headers = {
    'Content-Type': 'application/json',
    'Authorization': sessionToken
}

const Home = () => {
    const [userText, setUserText] = useState('Username');
    const [pswText, setPswText] = useState('Password');
    const [userName, setUserName] = useState('');
    const [pswdText, setPswdText] = useState('');
    const [bankId, setBankId] = useState('');
    //const [bottomInfoText, setBottomInfoText] = useState('To give you the best possible, we need to analyse your transaction for the last 6months. Once analysed we delete your details.');
    const [infoTitle, setInfoTitle] = useState('Your Credentials Are Never Stored!');
    const [infoText, setInfoText] = useState('To give you the best possible, we need to analyse your transaction for the last 6months. Once analysed we delete your details');
    const [contentDisp, setContentDisp] = useState(hideContent);
    const [bankList, setBankList] = useState([]);

    useEffect(()=>{
        let traxnId='';
        let token='';
        let bankId='';
        var promise = new Promise( (resolve, reject) => {
            let url_string = window.location.href;
            let url = new URL(url_string);
            let params = url.searchParams.get("gl", "");
            if (params) {
                params = params.split('_');
                token = params[0];
                traxnId = params[1];
                sessionStorage.setItem('token',token);
                sessionStorage.setItem('traxnId', traxnId);
                resolve("Token Found");
            }
            else {
                
                token = sessionStorage.getItem('token');
                traxnId = sessionStorage.getItem('traxnId');
                bankId = sessionStorage.getItem('bankId');
                if(token){
                    resolve("Token Found");
                }
                else{
                    reject(Error("Token Not exists"));
                }             
                
            }
        });
        promise.then( result => {
            const bankId = sessionStorage.getItem('bankId', '');            
            axios({
                method: 'get',
                url: controllerUrl+'/bankrequest/?traxn_id='+traxnId+'&bank_id='+bankId
            }).then((response) => {
                let bankData=[];
                for(let i=0;i<response.data.length;i++){
                    bankData.push({
                        "bank_id":response.data[i].bank_id,
                        "bank_name":response.data[i].bank_name,
                        "id":response.data[i].id,
                        "username":response.data[i].username_text
                    });
                }
                setBankList(bankData);
            })
            .catch((error) => {
                const status=error.status;
                sessionStorage.setItem['errorMsg']=error.msg;
                if(status===401 || status===404 || status===403){
                    window.location.href='/transactionError';
                }
                else{
                    sessionStorage.clear();
                    //window.location.href='/appError';
                    window.location.href='/transactionError';
                }
            });
           }, function(error) {
                window.location.href='/wrongurl';
           });
    
    },[]);
    const handleBankSelect = (event) =>{
        let bank_id = event.target.value;
        setBankId(bank_id);
        bankList.findIndex((item)=>{
            if(item.bank_id=== bank_id){
                setUserText(item.username);
                setContentDisp(dispContent);
            }
        })
    }
    const handleChange = (e) => {
        let value = e.target.value;
        let nt = e.target.name;
        if(nt==='setUserName'){
            setUserName(value);
        }
        else if(nt==='setPswdText'){
            setPswdText(value);
        }
    }
    const handleSubmit = () => {
        var traxnId = sessionStorage.getItem("traxnId");
        VerifyCredential(userName, pswdText, bankId, traxnId);
    }
    return (
        <div style={appHome}>
            <div style={homeInfo}>
                <b>{infoTitle} </b>
                <br />
                {infoText}
            </div>
            <div>
                <Form style={homeContent}>
                    <Form.Group controlId="formGridState">
                        <MdAccountBalance style={homeIcon}></MdAccountBalance><Form.Label>Bank</Form.Label>
                        <Form.Control as="select" onChange={handleBankSelect}>
                            <option value="-1">Select Bank</option>
                            {bankList.map((item)=>{
                                return <option key={item.id} value={item.bank_id}>{item.bank_name}</option>
                            })}
                        </Form.Control>
                    </Form.Group>
                    <div style={contentDisp}>
                        <Form.Group controlId="formBasicEmail">
                            <MdAccountCircle style={homeIcon}></MdAccountCircle><Form.Label>{userText}</Form.Label>
                            <Form.Control type="text" placeholder={userText} value={userName} name='setUserName' onChange={handleChange} required />
                        </Form.Group>
                        <Form.Group controlId="formBasicPassword">
                            <GiUnlocking style={homeIcon}></GiUnlocking><Form.Label>{pswText}</Form.Label>
                            <Form.Control type="password" placeholder="Password" value={pswdText} name='setPswdText' onChange={handleChange} required />
                            {/* <Form.Text className="text-muted">
                                {bottomInfoText}
                                <br />
                                By clicking Next you agree to our <a href='https://www.krazybee.com/terms-condition'>T&C</a>
                            </Form.Text> */}
                        </Form.Group>
                        <Form.Group controlId="formBasicCheckbox">
                            <Form.Check type="checkbox" label="I agree to the terms of use & the privacy policy" />
                        </Form.Group>                    
                        <ButtonToolbar>
                            <Button variant="outline-secondary" style={errorButton}>Cancel</Button>
                            <Button variant="outline-primary" style={primaryButton} onClick={handleSubmit}>Next</Button>
                        </ButtonToolbar>
                    </div>
                </Form>
            </div>
        </div>
    );
};

export default Home;