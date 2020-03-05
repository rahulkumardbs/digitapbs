import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import { Card } from "react-bootstrap";
import {centerContent, errorButton, primaryButton, primaryCard, primaryCardTitle} from '../AppStyle';
import { UserAction } from "./utils/appUtil";

const QuestionComponent = () => {
    const [userQuestion, setUserQuestion] = useState('What as your child hood area pincode? (e.g.101010)');
    const [userAnswer, setUserAnswer] = useState('');
    const handleSubmit = () => {
        UserAction('question', userAnswer);
    }    
    const handleCancel = () => {
        window.location.href = "/";
    }
    const handleChange = (e) => {
        let value = e.target.value;
        setUserAnswer(value);
    }
    return (
    <div style={centerContent}>
        <Card style={primaryCard}>
            <Card.Body>
                <Card.Title style={primaryCardTitle}>User Action Required</Card.Title>
                <Form>
                    <Form.Group controlId="formBasicEmail">
                        <Form.Label>HDFC Bank wants you to answer this security question: {userQuestion} </Form.Label>
                        <Form.Control type="text" placeholder="Enter answer here" value={userAnswer} name='setUserAnswer' onChange={handleChange} />
                    </Form.Group>
                </Form>
                <ButtonToolbar>
                <Button variant="outline-secondary" style={primaryButton}  onClick={handleSubmit}>Submit</Button>
                    <Button variant="outline-error" style={errorButton} onClick={handleCancel}>Cancel</Button>
                </ButtonToolbar>
            </Card.Body>
        </Card>
    </div>
  );
};

export default QuestionComponent;