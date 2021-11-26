from fastapi import APIRouter, Body


router = APIRouter()


@router.get('/')
def index():
    return {'status': 'OK'}


@router.post('/login', name='user:login')
def login(user_form=Body(..., embed=True)):
    return {'status': 'OK'}
