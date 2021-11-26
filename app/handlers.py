from fastapi import APIRouter, Body, Depends

from app.forms import UserLoginForm
from app.models import connect_db


router = APIRouter()


@router.get('/')
def index():
    return {'status': 'OK'}


@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), database=Depends(connect_db)):
    # user_form.email and user_form.password
    return {'status': 'OK'}
