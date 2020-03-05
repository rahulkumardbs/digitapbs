import {controllerUrl} from '../../Config';
import axios from 'axios';

const sessionToken = sessionStorage.getItem('token');
const traxnId = sessionStorage.getItem('traxnId');
const bankId = sessionStorage.getItem('bankId');
const headers = {
    'Content-Type': 'application/json',
    'Authorization': sessionToken
}

export const VerifyToken = () =>{
    // const data={
    //     token:token,
    // }
    // axios({
    //     method: 'get',
    //     url: controllerUrl+'/verifyToken/?token='+sessionToken,
    //   }).then((res) => {
    //         sessionStorage.setItem['token']=res.data.token;
    //     })
    //     .catch((error) => {
    //          console.log(error);
    //          const status=error.status;
    //          sessionStorage.setItem['errorMsg']=error.msg;
    //          if(status===403){
    //              window.location.href='/transactionError';
    //          }
    //          else if(status===500){
    //              sessionStorage.clear();
    //              window.location.href='/appError';
    //          }
    //          else{
    //              console.log("Not proper response");
    //          }
    //     });

    const flag = true;
    if(sessionToken){
        if(flag){
            console.log('1');
            return true;
        }
        else{
            console.log('2');
            return false;
        }
    }
    else{
        return false;
    }
}

export const VerifyCredential = (userName, pswdText, bankId, traxnId) =>{
    console.log(userName, pswdText, bankId, traxnId);
    sessionStorage.setItem('bankId',bankId);
    const data={
        username:userName,
        password:pswdText,
        bankId:bankId,
        traxnId:traxnId 
    }

    axios({
        method: 'post',
        url: controllerUrl+'/verifybankcustomer/',
        data: data,
        headers:headers
      }).then((res) => {
          window.location.href='/process';
        })
        .catch((error) => {
             console.log(error);
             const status=error.status;
             sessionStorage.setItem['errorMsg']=error.msg;
             if(status===401 || status===404 || status===403){
                 window.location.href='/transactionError';
             }
             else if(status===500){
                 sessionStorage.clear();
                 window.location.href='/appError';
             }
             else{
                 console.log("Not proper response");
             }
        });
}


export const UserAction = (traxnType, traxnText) =>{
    console.log(traxnId);
    
    const data={
        traxnId:traxnId,
        traxnType:traxnType,
        traxnText:traxnText
    }

    axios({
        method: 'post',
        url: controllerUrl+'/useraction/',
        data: data
    }).then((response) => {
            window.location.href='/process';
    })
    .catch((error) => {
        console.log(error);
        const status=error.status;
        sessionStorage.setItem['errorMsg']=error.msg;
        if(status===401 || status===404 || status===403){
            window.location.href='/transactionError';
        }
        else if(status===500){
            sessionStorage.clear();
            window.location.href='/appError';
        }
        else{
            console.log("Not proper response");
        }
    });
}


export const CheckSession = () =>{
    // const data={
    //     customerId:customerId,
    //     password:password,
    //     bankName:bankName
    // }

}

export const CloseSession = () =>{
    const sessionToken = sessionStorage.getItem('token');
}


export const ValidateInput = (event) =>{
    // const data={
    //     customerId:customerId,
    //     password:password,
    //     bankName:bankName
    // }

}

export const getBankList = () => {

    axios({
        method: 'get',
        url: controllerUrl+'/bankrequest/?traxn_id='+traxnId+'&bank_id='+bankId
    }).then((response) => {
        console.log("response");
        return response
    })
    .catch((error) => {
        console.log(error);
        const status=error.status;
        sessionStorage.setItem['errorMsg']=error.msg;
        if(status===401 || status===404 || status===403){
            window.location.href='/transactionError';
        }
        else if(status===500){
            sessionStorage.clear();
            window.location.href='/appError';
        }
        else{
            console.log("Not proper response");
        }
    });    
}