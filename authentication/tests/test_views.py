import email
from http import client
from urllib import response
import pytest
from rest_framework.test import APIClient
import users

client=APIClient()
@pytest.mark.django_db
def test_users_register():
    payload=dict(
        username="hossam",
        email="h@h.com",
        password1="123456",
        password2="123456",
        
    )
    response=client.post("/api/register",payload)
    data=response.data
    assert data["username"]== payload["username"]
    assert data["email"]== payload["email"]
    assert "password" not in data
    assert response.status_code==201
@pytest.mark.django_db
def test_users_username_required():
    payload=dict(
        email="h@h.com",
        password1="123456",
        password2="123456",
        
    )
    response=client.post("/api/register",payload)
    data=response.data
    assert response.status_code==400
@pytest.mark.django_db
def test_users_email_required():
    payload=dict(
        username="hoss",
       
        password1="123456",
        password2="123456",
        
    )
    response=client.post("/api/register",payload)
    data=response.data
    assert response.status_code==400
@pytest.mark.django_db
def test_users_passwor_not_match():
    payload=dict(
        username="hoooasm",
        email="h@h.com",
        password1="1234sa56",
        password2="123456",
        
    )
    response=client.post("/api/register",payload)
    data=response.data
    assert response.status_code==400
@pytest.mark.django_db
def test_users_user():
    payload=dict(
        username="hossam",
        email="h@h.com",
        password1="123456",
        password2="123456",
        
    )
    response=client.post("/api/register",payload)
    data=response.data
    assert data["username"]== payload["username"]
    assert data["email"]== payload["email"]
    assert "password" not in data  
    response=client.post("/api/login",dict(username="hossam",password="123456"))
    assert response.status_code==200
@pytest.mark.django_db
def test_login_user_login():
    payload=dict(
        username="hossam",
        email="h@h.com",
        password1="123456",
        password2="123456",
        
    )
    client.post("/api/register",payload)
    response=client.post("/api/login",dict(username="hossam",password="123456"))
    assert response.status_code==200
@pytest.mark.django_db
def test_login_user_fail():
    response=client.post("/api/login",dict(username="ali",password="123456"))
    assert response.status_code==400
    

@pytest.mark.django_db
def test_logout_fail():
    response=client.post("/api/logout")
    assert response.status_code==404
    