from firebase_admin import firestore, initialize_app

initialize_app()

def get_firestore_client():

    db = firestore.client()
    return db