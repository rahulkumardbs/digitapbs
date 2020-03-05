import React from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import { Card } from "react-bootstrap";
import { CardHeader } from "@material-ui/core";
import { CardBody } from "react-bootstrap/Card";
import { MdAccountBalance, MdAccountCircle } from "react-icons/md";
import { GiUnlocking } from "react-icons/gi";
import captcha from '../static/images/captcha.png';
import {centerContent} from '../AppStyle';

const CaptchaComponent = () => {
   const captchaImage=captcha;
  return (
    <div style={centerContent}>
        <Card style={{alignItems:'center' }}>

            <Card.Body>
                <Card.Img variant="top" src={captchaImage} />
                <Form style={{paddingTop:20}}>
                    <Form.Group controlId="formBasicEmail">
                        <Form.Control type="text" placeholder="0989" contentEditable='false' />
                    </Form.Group>
                </Form>
                <Button variant="primary">Next</Button>
            </Card.Body>
        </Card>
    </div>
  );
};

export default CaptchaComponent;