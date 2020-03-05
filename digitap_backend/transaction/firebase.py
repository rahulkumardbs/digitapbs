import pyrebase

config = {
    "apiKey": "AIzaSyDFKwkBwwDvzy-Tx87VJaXxlkFo-fQnc6Y",
    "authDomain": "digitapbs-8865a.firebaseapp.com",
    "databaseURL": "https://digitapbs-8865a.firebaseio.com",
    "storageBucket": "digitapbs-8865a.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def firebase_obj_generation(traxn_id, creq, curl, oreq, qreq, question, traxn_status, error_msg):
    """captcha_required, captcha_url, otp_required, question_rquired, question, transaction_status, error_msg"""
    traxn_id = str(traxn_id)
    traxn_data = {
        "traxn_data":{
            "captcha_required": creq,            
            "captcha_url": curl,
            "otp_required": oreq,
            "question_required": qreq,
            "question": question,
            "traxn_status":traxn_status,
            "error_msg":error_msg
        }
    }
    fdb = db.child(traxn_id)
    fdb.update(traxn_data)
